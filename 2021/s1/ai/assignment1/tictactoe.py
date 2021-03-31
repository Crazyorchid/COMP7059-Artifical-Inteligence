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
    print 'Expected states:' 
print ('oxxxoooxx 0') 
print ('oxxxooox- 0')
print ('oxxxo-oxo -1')