import numpy as np

board_input = str(input(""))
#to vanish the spaces between each line


#def Convert(string): 
   # li = list(string.split(" ")) 
    #return li 

#print(Convert(b)) 

def vanish_space(string):
    a = ''
    for line in board_input:
        a += line.strip()
        c = a.split()
        b = ''.join(c)
    return b

def horizon_win(string):
    for char in string:
        if string[0]==string[1]==string[2]:
            win = True;
        elif string[3]==string[4]==string[5]:
            win = True;
        elif string[6]==string[7]==string[8]:
            win = True;
        else:
            win = False;
    return win


def vertical_win(string):
    for char in string:
        if string[0]==string[3]==string[6]:
            win = True;
        elif string[1]==string[4]==string[7]:
            win = True;
        elif string[2]==string[5]==string[8]:
            win = True;
        else:
            win = False;
    return win

def diagnoal_win(string):
    for char in string:
        if string[0]==string[4]==string[8]:
            win = True;
        elif string[2]==string[4]==string[6]:
            win = True;
        else:
            win = False;
    return win

def valid_move():
    
def judge():
    vanish_space(board_input)
    if (horizon_win(board_input) or vertical_win(board_input) or diagnoal_win(board_input)):
       return 1
    else:
        return -1
        
print(judge())
#def create_game(board_input):
   #board = 
   
    
    
