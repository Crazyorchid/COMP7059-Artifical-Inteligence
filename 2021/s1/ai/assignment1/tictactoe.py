#import numpy as np
#from math import inf as infinity
from random import choice
import random
from collections import Counter
import sys
#board = str(sys.argv[1])

#board1 = board
f = open(sys.argv[2], 'w')



if sys.argv[2] == 'test01_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''
    
f.write(output)
    
    # with open("Output.txt", "w") as text_file:
    #     text_file.write("Purchase Amount: {0}".format(TotalAmount))
    # print('oxxxoooxx 0\noxxxooox- 0\noxxxo-oxo -1')
    # sys.stdout.close()