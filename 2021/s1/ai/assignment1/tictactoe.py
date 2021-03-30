#import numpy as np
#from math import inf as infinity
from random import choice
import sys
import random
from collections import Counter

text_file = open("visted.txt", "w")
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

def legal_move_left(board):
    """ 判断棋盘上是否还有空位 """
    for slot in SLOTS:
        if board[slot] == Open_token:
            return True
    return False


def winner(board):
    """ 判断局面的胜者,返回值-1表示X获胜,1表示O获胜,0表示平局或者未结束"""
    for triad in WINNING_TRIADS:
        triad_sum = board[triad[0]] + board[triad[1]] + board[triad[2]]
        if triad_sum == 3 or triad_sum == -3:
            return board[triad[0]]  # 表示棋子的数值恰好也是-1:X,1:O
    return 0

HUMAN = 1
COMPUTER = 0

def determine_move(board):
    """决定电脑(玩家O)的下一步棋,若估值相同则随机选取步数"""
    best_val = -2  # 本程序估值结果只在[-1,0,1]中
    my_moves = []
    for move in SLOTS:
        if board[move] == Open_token:
            board[move] = O_token
            
            val = alpha_beta_valuation(board, X_token, O_token, -2, 2)
            board[move] = Open_token
            #print("Computer ", move, ",leads to ", END_PHRASE[val])
            #print str(print_board((board)) + ' ' + END_PHRASE[val])
            if val > best_val:
                best_val = val
                my_moves = [move]
            if val == best_val:
                my_moves.append(move)
                
    return random.choice(my_moves)
    


def alpha_beta_valuation(board, player, next_player, alpha, beta):
    wnnr = winner(board)
    if wnnr != Open_token:
        # 有玩家获胜
        return wnnr
    elif not legal_move_left(board):
        # 没有空位,平局
        return 0
    # 检查当前玩家"player"的所有可落子点
    for move in SLOTS:
        if board[move] == Open_token:
            
            board[move] = player
            # 落子之后交换玩家，继续检验
            #print_board(board_list)
            #print print_board(board) + ' ' + str(winner(board)+1)
            val = alpha_beta_valuation(board, next_player, player, alpha, beta)
            #print str(print_board((board)) + ' ' + END_PHRASE[val])
            board[move] = Open_token
            if player == O_token:  # 当前玩家是O,是Max玩家(记号是1)
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta  # 直接返回当前的最大可能取值beta, 进行剪枝
            else:  # 当前玩家是X,是Min玩家(记号是-1)
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha  # 直接返回当前的最小可能取值alpha, 进行剪枝
    if player == O_token:
        retval = alpha
    else:
        retval = beta
    return retval



    
def main():
        board = board_list
        while legal_move_left(board) and winner(board) == Open_token:
            next_move = COMPUTER
            if next_move == COMPUTER and legal_move_left(board):
                mymv = determine_move(board)
                #print print_board(board)
                #print("Computero ", mymv)
                board[mymv] = O_token
                print print_board(board)
                break
            
            
            text_file.close()   
                
        

if __name__ == '__main__':
    main()

   
    
