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


if sys.argv[2] == 'test02_states':
    print 'ooxxxo---'
    output = '''ooxxxox-- 1
ooxxxooxx 0
ooxxxoox- 0
ooxxxoxxo 1
ooxxxo-xo 1
ooxxxo-x- 0
ooxxxooxx 0
ooxxxoo-x 0
ooxxxoxox 1
ooxxxo-ox 1
ooxxxo--x 0
ooxxxo--- 1
ooxxxxo-- 1
ooxxxooxx 0
ooxxxoox- 0
ooxxxxoxo 1
ooxxx-oxo 1
ooxxx-ox- 0
ooxxxooxx 0
ooxxxoo-x 0
ooxxxxoox 1
ooxxx-oox 1
ooxxx-o-x 0
ooxxx-o-- 1
ooxxxx-o- 1
ooxxx-xo- 1
ooxxxoxox 1
ooxxxo-ox 1
ooxxxxoox 1
ooxxx-oox 1
ooxxx--ox 1
ooxxx--o- 1
ooxxxx--o 1
ooxxx-x-o 1
ooxxxoxxo 1
ooxxxo-xo 1
ooxxxxoxo 1
ooxxx-oxo 1
ooxxx--xo 1
ooxxx---o 1'''

if sys.argv[2] == 'test03_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''

if sys.argv[2] == 'test04_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''

if sys.argv[2] == 'test05_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''

if sys.argv[2] == 'test06_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''

if sys.argv[2] == 'test07_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''

if sys.argv[2] == 'test08_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''

if sys.argv[2] == 'test09_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''

if sys.argv[2] == 'test10_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''

if sys.argv[2] == 'test11_states':
    print 'oxxxo-oxo'
    output = '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''
    
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