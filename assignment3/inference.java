import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.regex.Matcher;
import java.util.regex.Pattern;




public class inference {

    static class Utils {
        static Map<String,List<String>> copy(Map<String,List<String>> original){
            Map<String,List<String>> copy = new HashMap<>();
            for (Map.Entry<String,List<String>> entry: original.entrySet())
                copy.put(entry.getKey(), new ArrayList<>(entry.getValue()));
            return copy;
        }
    }

    Graph graph;
    static class Graph {
        ArrayList<String> vars = new ArrayList<>();
        // use children more often
        Map<String,ArrayList<String>> children = new LinkedHashMap<>();
        Map<String,List<String>> parents = new LinkedHashMap<>();
        Map<String,ArrayList<Float>> parentTrueProbs = new HashMap<>();
        int nodeSize(){
            return vars.size();
        }
        void setVars(String[] vars){
            this.vars.addAll( Arrays.asList(vars) );
            for(String var: vars){
                children.put(var, new ArrayList<>());
                parents.put(var, new LinkedList<>());
                parentTrueProbs.put(var, new ArrayList<>());
            }
        }
        void addEdge(int matI, int matJ){
            // matrix index i,j
            String parent = vars.get(matI);
            String child = vars.get(matJ);
            children.get(parent).add(child);
            parents.get(child).add(parent);
        }
        int childCount(String node){
            return children.get(node).size();
        }
        int parentCount(String node){
            return parents.get(node).size();
        }
        void setParentTrueProb(String node, int parIdx, float trueProb){
            parentTrueProbs.get(node).add(trueProb);
        }

        ArrayList<String> getTopologicalOrder(){
            ArrayList<String> topo = new ArrayList<>();
            Map<String,List<String>> parents = Utils.copy(this.parents);
            while(!parents.isEmpty()){
                for(String key: parents.keySet()){
                    if(parents.get(key).isEmpty()){
                        topo.add(key);
                        parents.remove(key);
                        for(List<String> value: parents.values()){
                            if(value.contains(key)){
                                value.remove(key);
                            }
                        }
                        break;
                    }
                }
            }
            return topo;
        }

        void queryingWith(String node, Sample sample){
            String parentIdxStr = "";
            for(String parent: parents.get(node)){
                Boolean evidence = sample.getEvidence(parent);
                assert(evidence != null);
                char evi = evidence ? '1' : '0';
                parentIdxStr += evi;
            }
            if("".equals(parentIdxStr))
                parentIdxStr = "0";
            int parentIdx = Integer.valueOf(parentIdxStr, 2);
            float trueProb = parentTrueProbs.get(node).get(parentIdx);
            float newWeight = trueProb;
            if(!sample.getEvidence(node))
                newWeight = 1 - newWeight;
            sample.updateWeight(newWeight);
            // System.out.println("update weight (querying "+ node +") by "+newWeight);
        }

        void samplingWith(String node, Sample sample){
            // System.out.print(node);
            // System.out.print(' ');
            // System.out.println(parents.get(node));
            String parentIdxStr = "";
            for(String parent: parents.get(node)){
                Boolean evidence = sample.getEvidence(parent);
                assert(evidence != null);
                char evi = evidence ? '1' : '0';
                parentIdxStr += evi;
            }
            if("".equals(parentIdxStr))
                parentIdxStr = "0";
            int parentIdx = Integer.valueOf(parentIdxStr, 2);
            float trueProb = parentTrueProbs.get(node).get(parentIdx);
            double rand = Math.random();
            boolean newEvidence = rand < trueProb;
            sample.setEvidence(node, newEvidence);
            // System.out.println("sample "+node+" to "+newEvidence);
        }

        @Override
        public String toString(){
            StringBuilder sb = new StringBuilder();
            for(Entry<String,List<String>> entry: parents.entrySet()){
                String child = entry.getKey();
                List<String> parent = entry.getValue();
                sb.append(child);
                sb.append(" <- ");
                if(parent.size() > 0)
                    sb.append(String.join(",", parent));
                else
                    sb.append("(null)");
                sb.append('\n');
                ArrayList<Float> trueProbs = parentTrueProbs.get(child);
                int parentExp = trueProbs.size();
                int bCount = Integer.bitCount(parentExp-1);
                for(int k = 0; k < parentExp; k++){
                    sb.append("    ");
                    float trueProb = trueProbs.get(k);
                    if(parentExp > 1){
                        String fmt = "%"+bCount+"s";
                        String bitIdx = String.format(fmt, Integer.toBinaryString(k));
                        bitIdx = bitIdx.replace(" ", "0");
                        String boolIdx = bitIdx.replace("0", "F").replace("1", "T");
                        sb.append(boolIdx);
                    }
                    else{
                        sb.append(' ');
                    }
                    sb.append(" - ");
                    sb.append(trueProb);
                    sb.append('\n');
                }
            }
            return sb.substring(0, sb.length()-1);
        }
    }
    void parseGraph(String graphFile){
        graph = new Graph();
        BufferedReader reader = null;
        try{
            reader = new BufferedReader(new FileReader(graphFile));

            String line = reader.readLine().trim(); // the variable N
            reader.readLine();                      // blank separate

            line = reader.readLine().trim();        // symbol array
            graph.setVars(line.split(" "));
            reader.readLine();                      // blank separate

            for(int i = 0; i < graph.nodeSize(); i++){      // 01 matrix
                line = reader.readLine().trim();
                String[] adjs = line.split(" ");
                for(int j = 0; j < graph.nodeSize(); j++)
                    if("1".equals(adjs[j]))
                        graph.addEdge(i, j);
            }

            for(int k = 0; k < graph.nodeSize(); k++){      // CPT matrices
                reader.readLine().trim();           // blank separate
                String node = graph.vars.get(k);
                int parentCount = graph.parentCount(node);
                int rows = (int)Math.pow(2, parentCount);
                for(int i = 0; i < rows; i++){
                    line = reader.readLine().trim();
                    String trueProbStr = line.split(" ")[0];
                    float trueProb = Float.parseFloat(trueProbStr);
                    graph.setParentTrueProb(node, k, trueProb);
                }
            }
        } catch(IOException ioe){
            System.err.println("no such query file: "+graphFile);
            System.exit(-1);
        } finally {
            try{
                if(reader != null)
                    reader.close();
            } catch(IOException ioe) {}
        } 
    }

    Query query;
    static class Query {
        String queryVar;
        Map<String,Boolean> evidenceVars = new LinkedHashMap<>();
        void setQueryVar(String queryVar){
            this.queryVar = queryVar;
        }
        void addEvidenceVar(String evidenceVar, boolean evidence){
            evidenceVars.put(evidenceVar, evidence);
        }
        @Override
        public String toString(){
            StringBuilder sb = new StringBuilder();
            sb.append("P(");
            sb.append(queryVar);
            sb.append(" | ");
            for(Entry<String,Boolean> entry: evidenceVars.entrySet()){
                sb.append(entry.getKey());
                sb.append('=');
                sb.append(entry.getValue());
                sb.append(", ");
            }
            sb.setCharAt(sb.length()-2, ')');
            return sb.substring(0, sb.length()-1);
        }
    }
    void parseQuery(String queryFile){
        query = new Query();
        BufferedReader reader = null;
        try{
            reader = new BufferedReader(new FileReader(queryFile));
            String line = reader.readLine().trim();
            Pattern p = Pattern.compile("P\\((\\w+) \\| (.*?)\\)");
            Matcher m = p.matcher(line);
            if(m.find()){
                query.setQueryVar( m.group(1) );
                p = Pattern.compile("(\\w+)=(true|false)");
                m = p.matcher(m.group(2));
                while(m.find()){
                    boolean evidence = "true".equals( m.group(2) );
                    query.addEvidenceVar( m.group(1) , evidence );
                }
            }
        } catch(IOException ioe){
            System.err.println("no such query file: "+queryFile);
            System.exit(-1);
        } finally {
            try{
                if(reader != null)
                    reader.close();
            } catch(IOException ioe) {}
        }
    }




    static class Sample {
        float weight = 1f;
        Map<String,Boolean> variables = new LinkedHashMap<>();

        void setEvidence(String variable, boolean value){
            variables.put(variable, value);
        }
        void updateWeight(float factor){
            weight *= factor;
        }
        boolean isEvidence(String variable){
            return variables.containsKey(variable);
        }
        boolean getEvidence(String variable){
            return variables.get(variable);
        }
        @Override
        public String toString(){
            StringBuilder sb = new StringBuilder();
            for(Entry<String,Boolean> entry: variables.entrySet()){
                char v = entry.getValue() ? '+' : '-';
                sb.append(v);
                sb.append(entry.getKey());
                sb.append(',');
            }
            String sampleStr = sb.substring(0, sb.length()-1);
            return String.format("{%s} (w=%f)", sampleStr, weight);
        }
        @Override
        public int hashCode(){
            return toString().hashCode();
        }
        @Override
        public boolean equals(Object object){
            return object!=null && hashCode()==object.hashCode();
        }
    }

    Sample sampleByLikelihoodWeighting(List<String> nodeOrder){
        Sample sample = new Sample();
        for(Entry<String,Boolean> entry: query.evidenceVars.entrySet())
            sample.setEvidence(entry.getKey(), entry.getValue());
        for(String node: nodeOrder){
            if(sample.isEvidence(node))
                graph.queryingWith(node, sample);
            else
                graph.samplingWith(node, sample);
        }
        return sample;
    }


    private static final int TRIALS = 100000;

    // returns P(query=true|evidence) and P(query=false|evidence)
    // performs likelihood weighting sampling
    float[] solve(){
        ArrayList<String> topo = graph.getTopologicalOrder();
        Map<Sample,Integer> sampleCount = new HashMap<>();
        int i = 0;
        while(i++ < TRIALS){
            Sample sample = sampleByLikelihoodWeighting(topo);
            if(!sampleCount.containsKey(sample))
                sampleCount.put(sample, 0);
            int count = sampleCount.get(sample);
            sampleCount.put(sample, count+1);
        }

        float relevantRate = 0, irrelevantRate = 0;
        String queryVar = query.queryVar;
        for(Sample sample: sampleCount.keySet()){
            int count = sampleCount.get(sample);
            if(sample.getEvidence(queryVar))
                relevantRate += count*sample.weight;
            else
                irrelevantRate += count*sample.weight;
        }

        // System.out.println(relevantRate + " " + irrelevantRate);
        return new float[]{
            relevantRate/(relevantRate+irrelevantRate),
            irrelevantRate/(relevantRate+irrelevantRate)
        };
    }



    public static void main(String[] args){
        inference instance = new inference();

        instance.parseGraph(args[0]);
        // System.out.println(instance.graph);

        instance.parseQuery(args[1]);
        // System.out.println(instance.query);

        float[] result = instance.solve();
        System.out.println(result[0]+" "+result[1]);
    }

}
