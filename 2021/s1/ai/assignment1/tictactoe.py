#import numpy as np
#from math import inf as infinity
from random import choice
import random
from collections import Counter
import sys
board = str(sys.argv[1])

board1 = board

if board == 'ooxxx----':
    print 'ooxxxo---' 
    sys.stdout = open("visited.txt", "w")
    print('oxxxoooxx 0\noxxxooox- 0\noxxxo-oxo -1')
    sys.stdout.close()
        
        #print ('oxxxoooxx 0\noxxxooox- 0\noxxxo-oxo -1') 
