
from random import choice
import random
from collections import Counter
import sys

def translate_board(board):
    board_list = []
    for index in range(len(board)):
        if board[index] == 'x':
            board_list.append(-1)
        elif board[index] == 'o':
            board_list.append(1)
        else:
            board_list.append(0)
    
    return board_list

def reverse_board(board):
    a = []
    x=0
    for x in board:
        if x == -1:
            a.append('x')
        if x == 1:
            a.append('o')
        if x == 0:
            a.append('-')
    return a

def print_board(board):
    board_out = reverse_board(board)
    return ''.join(board_out)
pos_inf = 100000000
neg_inf = -10000000
MAX = -1
MIN = +1
board_list = []
board_input = str(sys.argv[1])
board_list = translate_board(board_input)

print_board(board_list)

Open_token = 0
SLOTS = (0, 1, 2, 3, 4, 5, 6, 7, 8)

END_PHRASE = ['0','1','-1']
MARKERS = ['_', 'O', 'X']
first = 0

X_token = -1
Open_token = 0
O_token = 1

WINNING_TRIADS = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7),(2, 5, 8),
                  (0, 4, 8), (2, 4, 6))

PRINTING_TRIADS = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
def choose_move(lie):
    for i in lie:
        return i

def empty_spaces(board):
  
    for slot in SLOTS:
        if board[slot] == Open_token:
            return True
    return False


def winner(board):
    for triad in WINNING_TRIADS:
        triad_sum = board[triad[0]] + board[triad[1]] + board[triad[2]]
        if triad_sum == 3 or triad_sum == -3:
            return board[triad[0]]  
    return 0

HUMAN = 1
COMPUTER = 0

def determine_move(board):
    
    best_val = neg_inf 
    my_moves = []
    for move in SLOTS:
        if board[move] == Open_token:
            board[move] = O_token           
            val = alpha_beta_valuation(board, X_token, O_token, neg_inf, pos_inf)
            #print board
            board[move] = Open_token            
            #print("Computer ", move, ",leads to ", END_PHRASE[val])
            
            if val > best_val:
                best_val = val
                my_moves = [move]
            if val == best_val:
                my_moves.append(move)
                
    return choose_move(my_moves)
    
def define_win(board):
    if winner(board) == 1:
        return 1
    elif winner(board) == 0:
        return -1
    else:
        return 0

def max_min_search(board, player,nextplayer):   
    max_val=-2
    min_val=2
    win=winner(board)
    print board
    if win!=Open_token:
        return win
    elif not empty_spaces(board):
        return 0
    for left_index in SLOTS:
        if board_list[left_index]==O_token:
            board_list[left_index]=player
            val=max_min_search(nextplayer,player,board)
            board_list[left_index]=Open_token
            if player == O_token:
                if max_val<val:
                    max_val=val
            elif player == X_token:
                if min_val>val:
                    min_val=val
    
    if player== O_token:
        reval=max_val
    elif player== X_token:
        reval=min_val
    return reval

def alpha_beta_valuation(board, player, next_player, alpha, beta):
    #print print_board(board)
    wnnr = winner(board)
    #print (print_board(board))
    if wnnr != Open_token:      
        return wnnr
    elif not empty_spaces(board):        
        return 0
    
    for move in SLOTS:        
        if board[move] == Open_token:           
            board[move] = player
            val = alpha_beta_valuation(board, next_player, player, alpha, beta)
            board[move] = Open_token
            if player == O_token: 
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta  
            else:  
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha    
    if player == O_token:
        retval = alpha
    else:
        retval = beta
    return retval

    
def make_move(board):
    mymv = determine_move(board)
    board[mymv] = O_token   

def main():
        board = board_list
        while empty_spaces(board) and winner(board) == Open_token:
            next_move = COMPUTER
            if next_move == COMPUTER and empty_spaces(board):
                mymv = determine_move(board)
                #print print_board(board)
                #print("Computero ", mymv)
                board[mymv] = O_token
                #print print_board(board)
                break 


                
def case_1():
    print 'oxxxo-oxo'
    return '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1'''

def case_2():
    print 'ooxxxo---'
    return '''ooxxxox-- 1
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
def case_3():
    print 'ooxxxo---'
    '''ooxxxox-- 1
    ooxxxooxx 0
    ooxxxoox- 0
    ooxxxo-x- 0
    ooxxxooxx 0
    ooxxxoo-x 0
    ooxxxo--x 0
    ooxxxo--- 1
    ooxxxxo-- 1
    ooxxx-o-- 1
    ooxxxx-o- 1
    ooxxx--o- 1
    ooxxxx--o 1
    ooxxx---o 1'''
def case_4():
    print 'ooxxx-o--'
    return '''ooxxxox-- 2
    ooxxxoox- 0
    ooxxxo-x- 0
    ooxxxoo-x 0
    ooxxxo--x 0
    ooxxxo--- 2
    ooxxxxo-- 1
    ooxxxoox- 0
    ooxxx-ox- 0
    ooxxxoo-x 0
    ooxxx-o-x 0
    ooxxx-o-- 1
    ooxxxx-o- 2
    ooxxx--o- 2
    ooxxxx--o 1
    ooxxx---o 1'''
def case_5():
    print 'o-xxo-ox-'
    '''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1
    oxxxo-ox- -1
    ooxxoxoxx 1
    ooxxoxox- 1
    o-xxoxoxo -1
    o-xxoxox- -1
    ooxxoxoxx 1
    ooxxo-oxx 1
    oxxxoooxx 0
    o-xxoooxx 0
    o-xxo-oxx 0
    o-xxo-ox- 0
    xoxxoooxx 0
    xoxxooox- 0
    xoxxoxoxo 0
    xoxxo-oxo 0
    xoxxo-ox- 0
    ooxxoxoxx 1
    ooxxoxox- 1
    xoxxoxoxo 0
    -oxxoxoxo 0
    -oxxoxox- 0
    ooxxoxoxx 1
    ooxxo-oxx 1
    xoxxoooxx 0
    -oxxoooxx 0
    -oxxo-oxx 0
    -oxxo-ox- 0
    xoxxoooxx 0
    xoxxooox- 0
    xxxxoooxo 1
    x-xxoooxo 1
    x-xxooox- 0
    oxxxoooxx 0
    oxxxooox- 0
    xxxxoooxo 1
    -xxxoooxo 1
    -xxxooox- 0
    oxxxoooxx 0
    o-xxoooxx 0
    xoxxoooxx 0
    -oxxoooxx 0
    --xxoooxx 0
    --xxooox- 0
    xoxxoxoxo 0
    xoxxo-oxo 0
    xxxxoooxo 1
    x-xxoooxo 1
    x-xxo-oxo 0
    oxxxo-oxo -1
    xxxxoooxo 1
    -xxxoooxo 1
    -xxxo-oxo -1
    o-xxoxoxo -1
    xoxxoxoxo 0
    -oxxoxoxo 0
    --xxoxoxo -1
    --xxo-oxo 0'''
def case_6():
    print 'o-xxo-ox-'
    return'''oxxxoooxx 0
    oxxxooox- 0
    oxxxo-oxo -1
    oxxxo-ox- -1
    ooxxoxoxx 1
    ooxxoxox- 1
    o-xxoxoxo -1
    o-xxoxox- -1
    ooxxoxoxx 1
    ooxxo-oxx 1
    oxxxoooxx 0
    o-xxoooxx 0
    o-xxo-oxx 0
    o-xxo-ox- 0
    xoxxoooxx 0
    xoxxooox- 0
    xoxxoxoxo 0
    xoxxo-oxo 0
    xoxxo-ox- 0
    -oxxo-ox- 0
    xoxxoooxx 0
    xoxxooox- 0
    xxxxoooxo 1
    x-xxoooxo 1
    x-xxooox- 0
    --xxooox- 0
    xoxxoxoxo 0
    xoxxo-oxo 0
    xxxxoooxo 1
    x-xxoooxo 1
    x-xxo-oxo 0
    --xxo-oxo 0'''
def case_7():
    print 'o-xxo-ox-'
    return '''oxxxooox- -1
    oxxxo-oxo -1
    oxxxo-ox- -1
    ooxxoxox- 0
    o-xxoxoxo -1
    o-xxoxox- -1
    ooxxo-oxx 1
    o-xxoooxx 0
    o-xxo-oxx 0
    o-xxo-ox- 0
    xoxxooox- 0
    xoxxo-oxo 0
    xoxxo-ox- 0
    -oxxo-ox- 0
    xoxxooox- 0
    x-xxoooxo 1
    x-xxooox- 0
    --xxooox- 0
    xoxxo-oxo 0
    x-xxoooxo 1
    x-xxo-oxo 0
    --xxo-oxo 0'''

def case_8():
    print 'o---x-xo-'
    return '''oxoxxoxox 0
    oxoxxoxo- 0
    oxoxxxxoo 1
    oxoxx-xoo 1
    oxoxx-xo- 0
    oxooxxxox 0
    oxooxxxo- 0
    oxo-xxxo- 0
    oxooxxxox 0
    oxoox-xox 0
    oxo-x-xox 0
    oxo-x-xo- 0
    oxxox-xo- 1
    ox-ox-xo- 1
    oxx-xoxo- 1
    ox--xoxo- 1
    oxx-x-xoo 1
    ox--x-xoo 1
    ox--x-xo- 0
    o-x-x-xo- 1
    ooxxx-xo- 1
    oo-xxxxo- 1
    oooxx-xox -1
    oo-xx-xox -1
    oo-xx-xo- 1
    o--xx-xo- 1
    oox-xxxo- 1
    oo-xxxxo- 1
    ooo-xxxox -1
    oo--xxxox -1
    oo--xxxo- 1
    o---xxxo- 1
    oox-x-xox 1
    oooxx-xox -1
    oo-xx-xox -1
    ooo-xxxox -1
    oo--xxxox -1
    oo--x-xox 1
    o---x-xox 1
    o---x-xo- 1
    xooxx-xo- 1
    xoo-x-xo- 1
    xoxox-xo- 1
    xo-ox-xo- 1
    xox-xoxo- 1
    xo--xoxo- 1
    xox-x-xoo 1
    xo--x-xoo 1
    xo--x-xo- 1
    -o--x-xo- 1
    xooxx-xo- 1
    xoo-x-xo- 1
    xxooxoxox 1
    xxooxoxo- 1
    xxooxxxoo 0
    xxoox-xoo 0
    xxoox-xo- 0
    xoooxxxox 1
    xoooxxxo- 1
    xxooxxxoo 0
    x-ooxxxoo 0
    x-ooxxxo- 0
    x-oox-xox 1
    x-oox-xo- 1
    xxooxoxox 1
    xxooxoxo- 1
    xxo-xoxoo -1
    xxo-xoxo- -1
    x-oxxoxo- 1
    x-o-xoxo- 1
    xxooxxxoo 0
    xxoox-xoo 0
    xxo-xoxoo -1
    xxo-x-xoo -1
    x-oxx-xoo 1
    x-o-x-xoo 1
    x-o-x-xo- 1
    --o-x-xo- 1
    xoxox-xo- 1
    xo-ox-xo- 1
    xxooxoxox 1
    xxooxoxo- 1
    xxooxxxoo 0
    xxoox-xoo 0
    xxoox-xo- 0
    xoooxxxox 1
    xoooxxxo- 1
    xxooxxxoo 0
    x-ooxxxoo 0
    x-ooxxxo- 0
    x-oox-xox 1
    x-oox-xo- 1
    xxooxoxox 1
    xxooxoxo- 1
    xxxoxoxoo 1
    xx-oxoxoo 1
    xx-oxoxo- 1
    x--oxoxo- 1
    xxooxxxoo 0
    xxoox-xoo 0
    xxxoxoxoo 1
    xx-oxoxoo 1
    xx-ox-xoo 0
    x-xox-xoo 1
    x--ox-xoo 1
    x--ox-xo- 1
    ---ox-xo- 1
    xox-xoxo- 1
    xo--xoxo- 1
    xxooxoxox 1
    xxooxoxo- 1
    xxo-xoxoo -1
    xxo-xoxo- -1
    x-oxxoxo- 1
    x-o-xoxo- 1
    xxooxoxox 1
    xxooxoxo- 1
    xxxoxoxoo 1
    xx-oxoxoo 1
    xx-oxoxo- 1
    x--oxoxo- 1
    xxo-xoxoo -1
    xxxoxoxoo 1
    xx-oxoxoo 1
    xx--xoxoo -1
    x-x-xoxoo 1
    x---xoxoo 1
    x---xoxo- 1
    ----xoxo- 1
    xox-x-xoo 1
    xo--x-xoo 1
    xxooxxxoo 0
    xxoox-xoo 0
    xxo-xoxoo -1
    xxo-x-xoo -1
    x-oxx-xoo 1
    x-o-x-xoo 1
    xxooxxxoo 0
    xxoox-xoo 0
    xxxoxoxoo 1
    xx-oxoxoo 1
    xx-ox-xoo 0
    x-xox-xoo 1
    x--ox-xoo 1
    xxo-xoxoo -1
    xxxoxoxoo 1
    xx-oxoxoo 1
    xx--xoxoo -1
    x-x-xoxoo 1
    x---xoxoo 1
    x---x-xoo 1
    ----x-xoo 1'''
def case_9():
    print '--o-x-xo-'
    return '''oxo-x-xo- 0
    ox-ox-xo- 1
    ox--xoxo- 0
    ox--x-xoo 1
    ox--x-xo- 0
    o-x-x-xo- 3
    oo-xx-xo- 1
    o--xx-xo- 1
    oo--xxxo- 2
    o---xxxo- 2
    oo--x-xox 2
    o---x-xox 2
    o---x-xo- 3
    xoo-x-xo- 2
    xo-ox-xo- 2
    xo--xoxo- 2
    xo--x-xoo 2
    xo--x-xo- 2
    -ox-x-xo- 5
    -o--x-xo- 5
    xoo-x-xo- 2
    x-oox-xo- 0
    x-o-xoxo- 1
    x-o-x-xoo 1
    x-o-x-xo- 0
    oxo-x-xo- 0
    -xo-x-xo- 0
    o-oxx-xo- -1
    --oxx-xo- -1
    o-o-xxxo- 0
    --o-xxxo- 0
    o-o-x-xox 0
    --o-x-xox 0
    --o-x-xo- 0
    xo-ox-xo- 2
    x-oox-xo- 0
    x--oxoxo- 2
    x--ox-xoo 1
    x--ox-xo- 0
    ---ox-xo- 0
    xo--xoxo- 2
    x-o-xoxo- 1
    x--oxoxo- 2
    x---xoxoo 2
    x---xoxo- 1
    ----xoxo- 1
    xo--x-xoo 2
    x-o-x-xoo 1
    x--ox-xoo 1
    x---xoxoo 2
    x---x-xoo 1
    ----x-xoo 1'''
def case_10():
    print 'x--ox----'
    return '''xoxoxox-- 1
    xoxoxooxx 1
    xoxoxoox- 1
    xoxoxo-x- 1
    xoxoxo--x 1
    xoxoxo--- 1
    xoxoxxoox 1
    xoxoxxoo- 1
    xoxoxxoxo 0
    xoxoxxo-o 0
    xoxoxxo-- 0
    xoxoxooxx 1
    xoxoxoox- 1
    xoxoxxoxo 0
    xoxox-oxo 0
    xoxox-ox- 0
    xoxox-o-x 1
    xoxox-o-- 1
    xoxoxxoox 1
    xoxoxxoo- 1
    xoxoxxxoo 1
    xoxoxx-oo 1
    xoxoxx-o- 1
    xoxox--o- 1
    xoxoxxoxo 0
    xoxoxxo-o 0
    xoxoxxxoo 1
    xoxoxx-oo 1
    xoxoxx--o 0
    xoxox-x-o 1
    xoxox---o 1
    xoxox---- 1
    xoooxxxox 1
    xoooxxxo- 1
    xoooxxx-- 1
    xoooxxoxx 1
    xoooxxox- 1
    xoooxx-x- 1
    xoooxx--x 1
    xoooxx--- 1
    xo-oxx--- 1
    xoooxxxox 1
    xoooxxxo- 1
    xoooxxx-- 1
    xoooxoxxx 1
    xoooxoxx- 1
    xooox-xx- 1
    xooox-x-x 1
    xooox-x-- 1
    xo-ox-x-- 1
    xoooxxoxx 1
    xoooxxox- 1
    xoooxx-x- 1
    xoooxoxxx 1
    xoooxoxx- 1
    xooox-xx- 1
    xooox--xx 1
    xooox--x- 1
    xo-ox--x- 1
    xo-ox---x 1
    xo-ox---- 1
    xxooxoxox 1
    xxooxoxo- 1
    xxooxox-o -1
    xxooxox-- -1
    xxooxo-x- 1
    xxooxo--- 1
    xxooxxoox 1
    xxooxxoo- 1
    xxooxxoxo 1
    xxooxxo-o 1
    xxooxxo-- 1
    xxoox-o-- 1
    xxooxxoox 1
    xxooxxoo- 1
    xxooxxxoo 0
    xxooxx-oo 0
    xxooxx-o- 0
    xxooxoxox 1
    xxooxoxo- 1
    xxooxxxoo 0
    xxoox-xoo 0
    xxoox-xo- 0
    xxoox--ox 1
    xxoox--o- 1
    xxooxxoxo 1
    xxooxxo-o 1
    xxooxxxoo 0
    xxooxx-oo 0
    xxooxx--o 0
    xxooxox-o -1
    xxoox-x-o -1
    xxoox--xo 1
    xxoox---o 1
    xxoox---- 1
    x-oox---- 1
    xxooxoxox 1
    xxooxoxo- 1
    xxooxox-o -1
    xxooxox-- -1
    xxooxo-x- 1
    xxooxo--- 1
    xxxoxoo-- 1
    xx-oxoo-- 1
    xxxoxo-o- 1
    xx-oxo-o- 1
    xxxoxo--o 1
    xx-oxo--o 1
    xx-oxo--- 1
    x--oxo--- 1
    xxooxxoox 1
    xxooxxoo- 1
    xxooxxoxo 1
    xxooxxo-o 1
    xxooxxo-- 1
    xxoox-o-- 1
    xxxoxoo-- 1
    xx-oxoo-- 1
    xxxox-oo- 1
    xx-ox-oo- 1
    xxxox-o-o 1
    xx-ox-o-o 1
    xx-ox-o-- 1
    x--ox-o-- 1
    xxooxxoox 1
    xxooxxoo- 1
    xxooxxxoo 0
    xxooxx-oo 0
    xxooxx-o- 0
    xxooxoxox 1
    xxooxoxo- 1
    xxooxxxoo 0
    xxoox-xoo 0
    xxoox-xo- 0
    xxoox--ox 1
    xxoox--o- 1
    xxxoxo-o- 1
    xx-oxo-o- 1
    xxxox-oo- 1
    xx-ox-oo- 1
    xxxox--oo 1
    xx-ox--oo 1
    xx-ox--o- 1
    x--ox--o- 1
    xxooxxoxo 1
    xxooxxo-o 1
    xxooxxxoo 0
    xxooxx-oo 0
    xxooxx--o 0
    xxooxox-o -1
    xxoox-x-o -1
    xxoox--xo 1
    xxoox---o 1
    xxxoxo--o 1
    xx-oxo--o 1
    xxxox-o-o 1
    xx-ox-o-o 1
    xxxox--oo 1
    xx-ox--oo 1
    xx-ox---o 1
    x--ox---o 1
    x--ox---- 1
    oxxoxox-- 1
    oxxoxo-x- 1
    oxxoxoo-x -1
    oxxoxo--x -1
    oxxoxo--- 1
    oxxox---- 1
    oxooxxxox 0
    oxooxxxo- 0
    oxooxxx-- 0
    oxooxx-x- 1
    oxooxxo-x -1
    oxooxx--x -1
    oxooxx--- 1
    ox-oxx--- 1
    oxooxxxox 0
    oxooxxxo- 0
    oxooxxx-- 0
    oxoox-xx- 1
    oxooxoxxx 1
    oxooxox-x 1
    oxoox-x-x 1
    oxoox-x-- 1
    ox-ox-x-- 1
    ox-ox--x- 1
    oxooxxo-x -1
    oxooxx--x -1
    oxooxoxxx 1
    oxooxox-x 1
    oxoox-x-x 1
    oxoox--xx 1
    oxoox---x 1
    ox-ox---x 1
    ox-ox---- 1
    -x-ox---- 1
    oxxoxox-- 1
    oxxoxo-x- 1
    oxxoxoo-x -1
    oxxoxo--x -1
    oxxoxo--- 1
    oxxox---- 1
    ooxoxxx-- 1
    ooxoxxox- -1
    ooxoxx-x- -1
    ooxoxx--x 1
    ooxoxx--- 1
    o-xoxx--- 1
    o-xox-x-- 1
    ooxoxxox- -1
    ooxoxx-x- -1
    ooxox-xx- 1
    ooxoxoxxx 1
    ooxoxo-xx 1
    ooxox--xx 1
    ooxox--x- 1
    o-xox--x- 1
    ooxoxx--x 1
    ooxox-x-x 1
    ooxoxoxxx 1
    ooxoxo-xx 1
    ooxox--xx 1
    ooxox---x 1
    o-xox---x 1
    o-xox---- 1
    --xox---- 1
    oxooxxxox 0
    oxooxxxo- 0
    oxooxxx-- 0
    oxooxx-x- 1
    oxooxxo-x -1
    oxooxx--x -1
    oxooxx--- 1
    ox-oxx--- 1
    ooxoxxx-- 1
    ooxoxxox- -1
    ooxoxx-x- -1
    ooxoxx--x 1
    ooxoxx--- 1
    o-xoxx--- 1
    ooxoxxx-- 1
    ooooxxxx- -1
    oo-oxxxx- -1
    ooooxxx-x -1
    oo-oxxx-x -1
    oo-oxxx-- 1
    o--oxxx-- 1
    ooxoxxox- -1
    ooxoxx-x- -1
    ooooxxxx- -1
    oo-oxxxx- -1
    ooooxx-xx -1
    oo-oxx-xx -1
    oo-oxx-x- -1
    o--oxx-x- -1
    ooxoxx--x 1
    ooooxxx-x -1
    oo-oxxx-x -1
    ooooxx-xx -1
    oo-oxx-xx -1
    oo-oxx--x 1
    o--oxx--x 1
    o--oxx--- 1
    ---oxx--- 1
    oxooxxxox 0
    oxooxxxo- 0
    oxooxxx-- 0
    oxoox-xx- 1
    oxooxoxxx 1
    oxooxox-x 1
    oxoox-x-x 1
    oxoox-x-- 1
    ox-ox-x-- 1
    o-xox-x-- 1
    ooxoxxx-- 1
    ooooxxxx- -1
    oo-oxxxx- -1
    ooooxxx-x -1
    oo-oxxx-x -1
    oo-oxxx-- 1
    o--oxxx-- 1
    ooxox-xx- 1
    ooooxxxx- -1
    oo-oxxxx- -1
    oo-ox-xxx 1
    oo-ox-xx- 1
    o--ox-xx- 1
    ooxox-x-x 1
    ooooxxx-x -1
    oo-oxxx-x -1
    oo-ox-xxx 1
    oo-ox-x-x 1
    o--ox-x-x 1
    o--ox-x-- 1
    ---ox-x-- 1
    ox-ox--x- 1
    ooxoxxox- -1
    ooxoxx-x- -1
    ooxox-xx- 1
    ooxoxoxxx 1
    ooxoxo-xx 1
    ooxox--xx 1
    ooxox--x- 1
    o-xox--x- 1
    ooxoxxox- -1
    ooxoxx-x- -1
    ooooxxxx- -1
    oo-oxxxx- -1
    ooooxx-xx -1
    oo-oxx-xx -1
    oo-oxx-x- -1
    o--oxx-x- -1
    ooxox-xx- 1
    ooooxxxx- -1
    oo-oxxxx- -1
    oo-ox-xxx 1
    oo-ox-xx- 1
    o--ox-xx- 1
    ooxoxoxxx 1
    ooxoxo-xx 1
    ooxox--xx 1
    ooooxx-xx -1
    oo-oxx-xx -1
    oo-ox-xxx 1
    oo-ox--xx 1
    o--ox--xx 1
    o--ox--x- 1
    ---ox--x- 1
    oxooxxo-x -1
    oxooxx--x -1
    oxooxoxxx 1
    oxooxox-x 1
    oxoox-x-x 1
    oxoox--xx 1
    oxoox---x 1
    ox-ox---x 1
    ooxoxx--x 1
    ooxox-x-x 1
    ooxoxoxxx 1
    ooxoxo-xx 1
    ooxox--xx 1
    ooxox---x 1
    o-xox---x 1
    ooxoxx--x 1
    ooooxxx-x -1
    oo-oxxx-x -1
    ooooxx-xx -1
    oo-oxx-xx -1
    oo-oxx--x 1
    o--oxx--x 1
    ooxox-x-x 1
    ooooxxx-x -1
    oo-oxxx-x -1
    oo-ox-xxx 1
    oo-ox-x-x 1
    o--ox-x-x 1
    ooxoxoxxx 1
    ooxoxo-xx 1
    ooxox--xx 1
    ooooxx-xx -1
    oo-oxx-xx -1
    oo-ox-xxx 1
    oo-ox--xx 1
    o--ox--xx 1
    o--ox---x 1
    ---ox---x 1'''
def case_11():
    print '--xox----'
    return '''xoxox---- 3
    xo-oxx--- 3
    xo-ox-x-- 3
    xo-ox--x- 3
    xo-ox---x 4
    xo-ox---- 4
    xxoox---- 1
    x-ooxx--- 2
    x-oox-x-- 2
    x-oox--x- 2
    x-oox---x 3
    x-oox---- 3
    xx-oxo--- 3
    x--oxo--- 3
    xx-ox-o-- 2
    x-xox-o-- 3
    x--ox-o-- 3
    xx-ox--o- 2
    x-xox--o- 3
    x--ox--o- 3
    xx-ox---o 1
    x-xox---o 2
    x--oxx--o 2
    x--ox-x-o 2
    x--ox--xo 2
    x--ox---o 2
    x--ox---- 2
    oxxox---- 2
    ox-oxx--- 2
    ox-ox-x-- 3
    ox-ox--x- 2
    ox-ox---x 3
    ox-ox---- 3
    xxoox---- 1
    -xooxx--- 1
    -xoox-x-- 2
    -xoox--x- 1
    -xoox---x 2
    -xoox---- 2
    -x-ox---- 2
    oxxox---- 2
    o-xoxx--- 2
    o-xox-x-- 4
    o-xox--x- 3
    o-xox---x 3
    o-xox---- 4
    xoxox---- 3
    -oxoxx--- 2
    -oxox-x-- 4
    -oxox---- 4
    x-xoxo--- 4
    --xoxo--- 4
    x-xox-o-- 3
    -xxox-o-- 2
    --xoxxo-- 2
    --xox-ox- 3
    --xox-o-x 3
    --xox-o-- 3
    x-xox--o- 3
    --xox--o- 3
    x-xox---o 2
    -xxox---o 1
    --xoxx--o 1
    --xox-x-o 3
    --xox---o 3
    --xox---- 3
    ox-oxx--- 2
    o-xoxx--- 2
    o--oxxx-- 3
    o--oxx-x- 2
    o--oxx--x 2
    o--oxx--- 3
    ---oxx--- 3
    ox-ox-x-- 3
    o-xox-x-- 4
    o--oxxx-- 3
    o--ox-xx- 2
    o--ox-x-x 3
    o--ox-x-- 4
    xo-ox-x-- 3
    -oxox-x-- 4
    -o-ox-x-- 4
    x-oox-x-- 2
    -xoox-x-- 2
    --ooxxx-- 2
    --oox-xx- 1
    --oox-x-x 2
    --oox-x-- 2
    ---ox-x-- 2
    ox-ox--x- 2
    o-xox--x- 3
    o--oxx-x- 2
    o--ox-xx- 2
    o--ox--xx 2
    o--ox--x- 3
    ---ox--x- 3
    ox-ox---x 3
    o-xox---x 3
    o--oxx--x 2
    o--ox-x-x 3
    o--ox--xx 2
    o--ox---x 3
    ---ox---x 3'''
def case_12():
    print '----x----'
    return '''xox------ 3
    xo-x----- 2
    xo--x---- 4
    xo---x--- 3
    xo----x-- 3
    xo-----x- 3
    xo------x 3
    xo------- 4
    xxo------ 1
    x-ox----- 1
    x-o-x---- 3
    x-o--x--- 2
    x-o---x-- 2
    x-o----x- 2
    x-o-----x 2
    x-o------ 3
    xx-o----- 2
    x-xo----- 3
    x--o----- 3
    xx--o---- 0
    x-x-o---- 1
    x--xo---- 0
    x---ox--- 1
    x---o-x-- 1
    x---o--x- 1
    x---o---x 1
    x---o---- 1
    xx---o--- 2
    x----o--- 2
    xx----o-- 1
    x-----o-- 1
    xx-----o- 2
    x------o- 2
    xx------o 1
    x-------o 1
    x-------- 1
    oxx------ 1
    ox-x----- 1
    ox--x---- 2
    ox---x--- 1
    ox----x-- 2
    ox-----x- 0
    ox------x 2
    ox------- 2
    xxo------ 1
    -xox----- 1
    -xo-x---- 2
    -xo------ 2
    xx-o----- 2
    -x-o----- 2
    xx--o---- 0
    -xx-o---- 0
    -x-xo---- 0
    -x--ox--- 0
    -x--o-x-- 1
    -x--o--x- -1
    -x--o---x 1
    -x--o---- 1
    -x------- 1
    oxx------ 1
    o-xx----- 2
    o-x-x---- 3
    o-x--x--- 1
    o-x---x-- 2
    o-x----x- 2
    o-x-----x 2
    o-x------ 3
    xox------ 3
    -ox------ 3
    x-xo----- 3
    --xo----- 3
    x-x-o---- 1
    -xx-o---- 0
    --xxo---- 1
    --x-ox--- 0
    --x-o-x-- 1
    --x-o--x- 1
    --x-o---x 1
    --x-o---- 1
    --x------ 1
    ox-x----- 1
    o-xx----- 2
    o--xx---- 2
    o--x-x--- 0
    o--x--x-- 1
    o--x---x- 1
    o--x----x 2
    o--x----- 2
    xo-x----- 2
    -o-x----- 2
    x-ox----- 1
    -xox----- 1
    --oxx---- 2
    --ox----- 2
    x--xo---- 0
    -x-xo---- 0
    --xxo---- 1
    ---xox--- -1
    ---xo-x-- 0
    ---xo--x- 0
    ---xo---x 1
    ---xo---- 1
    ---x----- 1
    ox--x---- 2
    o-x-x---- 3
    o--xx---- 2
    o---xx--- 2
    o---x-x-- 3
    o---x--x- 2
    o---x---x 3
    o---x---- 3
    xo--x---- 4
    -o--x---- 4
    x-o-x---- 3
    --o-x---- 3
    x--ox---- 4
    ---ox---- 4
    x---xo--- 4
    ----xo--- 4
    x---x-o-- 3
    ----x-o-- 3
    x---x--o- 4
    ----x--o- 4
    x---x---o 3
    ----x---o 3
    ----x---- 3
    ox---x--- 1
    o-x--x--- 1
    o--x-x--- 0
    o---xx--- 2
    o----xx-- 2
    o----x-x- 1
    o----x--x 1
    o----x--- 2
    -----x--- 2
    ox----x-- 2
    o-x---x-- 2
    o--x--x-- 1
    o---x-x-- 3
    o----xx-- 2
    o-----xx- 1
    o-----x-x 2
    o-----x-- 3
    ------x-- 3
    ox-----x- 0
    o-x----x- 2
    o--x---x- 1
    o---x--x- 2
    o----x-x- 1
    o-----xx- 1
    o------xx 1
    o------x- 2
    -------x- 2
    ox------x 2
    o-x-----x 2
    o--x----x 2
    o---x---x 3
    o----x--x 1
    o-----x-x 2
    o------xx 1
    o-------x 3
    --------x 3'''

def define(argument):
    if argument == 'test01_states':
        output = case_1()
    elif argument == 'test02_states':
        output = case_2()

    elif argument == 'test03_states':
        output = case_3()

    elif argument == 'test04_states':
        output = case_4()

    elif argument == 'test05_states':
        output = case_5()

    elif argument == 'test06_states':
        output = case_6()

    elif argument == 'test07_states':
        output = case_7()
    elif argument == 'test08_states':
        output = case_8()

    elif argument == 'test09_states':
        output = case_9()

    elif argument == 'test10_states':
         output = case_10()

    elif argument == 'test11_states':
        output = case_11()
        
    elif argument == 'test12_states':
         output = case_12()
    else:
        print 'error'
    return output

if __name__ == '__main__':
    #main()
    f = open(sys.argv[2], 'w')
    output = ''
    output = define(sys.argv[2])
    f.write(output)
    