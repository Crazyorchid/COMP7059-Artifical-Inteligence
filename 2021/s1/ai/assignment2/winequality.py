from collections import Counter
from math import log
import argparse
import re
from collections import Counter


all_features = ['f_acid', 'v_acid', 'c_acid', 'res_sugar', 'chlorides', 'fs_dioxide', 'ts_dioxide', 'density', 'pH',
               'sulphates', 'alcohol', 'quality']

x_features = all_features[:-1]


def load_train_data(path):
    with open(path, "r") as f:
        data = f.read().split("\n")

    X = []
    y = []

    for i, item in enumerate(data):
        if item == "" or i == 0:
            continue

        item = re.sub(r' +', " ", item)
        item = item.strip().split()

        sample = []
        for value in range(len(all_features) - 1):
            sample.append(float(item[value]))

        output = item[len(all_features) - 1]

        X.append(sample)
        y.append(output)
    return X, y


def load_test_data(path):
    with open(path, "r") as f:
        data = f.read().split("\n")

    X = []

    for i, item in enumerate(data):
        if item == "" or i == 0:
            continue

        item = re.sub(r' +', " ", item)
        item = item.strip().split()

        sample = []
        for value in range(len(all_features) - 1):
            sample.append(float(item[value]))

        X.append(sample)
    return X


def cal_entropy(labels):
    counter = Counter(labels)
    p_list = [float(counter[k]) / len(labels) for k in counter.keys()]
    entropy = - sum([p * log(p) for p in p_list])

    return entropy


def cal_information_gain(X, y, attr_no, split_val):
    little_y = []
    large_y = []
    for i, sample in enumerate(X):
        if sample[attr_no] <= split_val:
            little_y.append(y[i])
        else:
            large_y.append(y[i])

    conditional_entropy = sum([float(len(item)) / len(y) * cal_entropy(item) for item in [little_y, large_y]])

    return cal_entropy(y) - conditional_entropy


class Node:
    def __init__(self):
        self.attr_no = None
        self.split_val = None
        self.left = None
        self.right = None
        self.label = None


class DecisionTree:
    def __init__(self, X, y, min_leaf, attrs):
        self.X = X
        self.y = y
        self.min_leaf = min_leaf
        self.attrs = attrs

        self.root = self.decision_tree_learning(self.X, self.y)

    @staticmethod
    def is_same(y):
        y = map(str, y)
        c = Counter(y)

        if len(c) == 1:
            return True
        else:
            return False

    def get_frequent_value(self, y):
        c = Counter(y)

        return max(c.items(), key=lambda x: x[1])[0]


    def decision_tree_learning(self, X, y):
        N = len(X)
        if N <= self.min_leaf or self.is_same(y) or self.is_same(X):
            node = Node()

            node.label = self.get_frequent_value(y)

            return node

        attr_no, split_val = self.choose_split(X, y)
        node = Node()
        node.attr_no = attr_no
        node.split_val = split_val

        little_X, little_y, large_X, large_y = self.get_value_sample(X, y, attr_no, split_val)

        node.left = self.decision_tree_learning(little_X, little_y)

        node.right = self.decision_tree_learning(large_X, large_y)

        return node


    def choose_split(self, X, y):
        best_gain = 0
        best_split_val = 0
        best_attr_no = 0

        for attr_no in range(len(self.attrs)):
            sorted_attr_value = self.get_sorted_attr_value(X, attr_no)
            for i in range(len(sorted_attr_value) - 1):
                split_val = float(sorted_attr_value[i] + sorted_attr_value[i + 1]) / 2
                gain = cal_information_gain(X, y, attr_no, split_val)
                if gain > best_gain:
                    best_gain = gain
                    best_split_val = split_val
                    best_attr_no = attr_no

        return best_attr_no, best_split_val


    @staticmethod
    def get_sorted_attr_value(X, attr_no):
        attr_value = []
        for sample in X:
            attr_value.append(sample[attr_no])

        return sorted(attr_value)


    def predict(self, x):
        node = self.root

        while node.label is None:
            if x[node.attr_no] <= node.split_val:
                node = node.left
            else:
                node = node.right

        return node.label


    @staticmethod
    def get_value_sample(X, y, attr_no, split_val):
        little_X = []
        little_y = []
        large_X = []
        large_y = []
        for i, item in enumerate(X):
            if item[attr_no] <= split_val:
                little_X.append(item)
                little_y.append(y[i])
            else:
                large_X.append(item)
                large_y.append(y[i])

        return little_X, little_y, large_X, large_y




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("train", type=str, default="data/train")
    parser.add_argument("test", type=str, default="data/test-sample")
    parser.add_argument("min_leaf", type=int, default=3)

    args = parser.parse_args()

    X, y = load_train_data(args.train)

    tree = DecisionTree(X, y, min_leaf=args.min_leaf, attrs=x_features)

    test_X = load_test_data(args.test)

    labels = []

    for x in test_X:
        label = tree.predict(x)
        labels.append(label)

    print " ".join(labels)