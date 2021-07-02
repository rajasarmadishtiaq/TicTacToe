import sys
import math
import time
import random

num = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

symbols = ['', '']

print("Welcome To TicTacToe","\nYou will be playing against The Computer.")
print()
user_name = str(input("Please enter your name: "))

user_turn = False
comp_turn = False
user_move = 0


def print_board():
    for row in range(0, 3):
        print("-----------------")
        for column in range(0, 3):
            print("",num[row][column], end = "  | ")
        print()
    print("-----------------")
        
    print(" ")

def toss():
    global symbols
    global user_turn
    global comp_turn
    global first_turn
    
    user_symbol = ""
    computer_symbol = ""
    toss_value = random.randint(1, 2)
    user_toss_value = eval(input(user_name + " enter 1 for heads and 2 for tails: "))
    if user_toss_value < 1 or user_toss_value > 2:
        valid = False
        while not valid:
            user_toss_value = eval(input(user_name + " invalid entry. Enter 1 for heads and 2 for tails: "))
            if user_toss_value == 1 or user_toss_value == 2:
                valid = True
    if user_toss_value == toss_value:
        print("You have won the toss!")
        user_turn = True
        user_symbol = str(input("Enter X to choose X or O to choose O: "))
        user_symbol = user_symbol.upper()
        if user_symbol == "X":
            computer_symbol = "O"
        else:
            computer_symbol = "X"
    else:
        print("You have lost the toss.")
        comp_turn = True
        computer_symbol = random.choice(("X", "O"))
        if computer_symbol == "X":
            user_symbol = "O"
        else:
            user_symbol = "X"
    print("")
    print(user_name + "\'s symbol:",user_symbol,"\nComputer's symbol:",computer_symbol)
    
    symbols = [user_symbol, computer_symbol]

def player_move():
    global user_move
    global user_turn
    global comp_turn
    
    while user_turn == True:
        user_move = eval(input("Please enter the box position (1-9): "))
        if user_move < 1 or user_move > 9:
            turn_valid = False
            while not turn_valid:
                user_move = eval(input("Invalid entry. Please enter the box position (1-9): "))
                if user_move >=1 and user_move <= 9:
                    break
        break
    
    user_turn = False   
    comp_turn = True

def moves_left(board):
    for row in range(3):
        for column in range(3) :
            if (board[row][column] == " "):
                return True
    return False

def winning_condition(board) :
    if board[0][0] == symbols[0] and board[0][1] == symbols[0] and board[0][2] == symbols[0] or board[1][0] == symbols[0] and board[1][1] == symbols[0] and board[1][2] == symbols[0] or board[2][0] == symbols[0] and board[2][1] == symbols[0] and board[2][2] == symbols[0] or board[0][0] == symbols[0] and board[1][0] == symbols[0] and board[2][0] == symbols[0] or board[0][1] == symbols[0] and board[1][1] == symbols[0] and board[2][1] == symbols[0] or board[0][2] == symbols[0] and board[1][2] == symbols[0] and board[2][2] == symbols[0] or board[0][0] == symbols[0] and board[1][1] == symbols[0] and board[2][2] == symbols[0] or board[0][2] == symbols[0] and board[1][1] == symbols[0] and board[2][0] == symbols[0]:
        return -1

    elif board[0][0] == symbols[1] and board[0][1] == symbols[1] and board[0][2] == symbols[1] or board[1][0] == symbols[1] and board[1][1] == symbols[1] and board[1][2] == symbols[1] or board[2][0] == symbols[1] and board[2][1] == symbols[1] and board[2][2] == symbols[1] or board[0][0] == symbols[1] and board[1][0] == symbols[1] and board[2][0] == symbols[1] or board[0][1] == symbols[1] and board[1][1] == symbols[1] and board[2][1] == symbols[1] or board[0][2] == symbols[1] and board[1][2] == symbols[1] and board[2][2] == symbols[1] or board[0][0] == symbols[1] and board[1][1] == symbols[1] and board[2][2] == symbols[1] or board[0][2] == symbols[1] and board[1][1] == symbols[1] and board[2][0] == symbols[1]:
        return 1

    else:
        return 0

def best_move(board):
    global user_turn
    global comp_turn
    
    bestScore = -math.inf
    
    print("\nComputer is making its turn...")

    start_time = time.time()

    for row in range(3):    
        for column in range(3):
         
            if (board[row][column] == " "):
             
                board[row][column] = symbols[1]
 
                moveScore = minimax(board, False, -math.inf, math.inf)
 
                board[row][column] = " "

                if (moveScore > bestScore):               
                    bestMove = (row, column)
                    bestScore = moveScore

    end_time = time.time()
    
    board[bestMove[0]][bestMove[1]] = symbols[1]
    num[bestMove[0]][bestMove[1]] = symbols[1]

    print("\nTime taken for Computer to make move:",round(end_time - start_time, 2),"seconds.")
    print()


    user_turn = True
    comp_turn = False

def minimax(board, isMaximizing, alpha, beta):
    
    score = winning_condition(board)
 
    if (score == 1):
        return score
 
    if (score == -1):
        return score
 
    if (moves_left(board) == False):
        return 0
    
    if (isMaximizing):    
        best = -math.inf
 
        for row in range(3):
            
            for column in range(3):
              
                if (board[row][column]== " "):
                 
                    board[row][column] = symbols[1]
 
                    best = max(best, minimax(board, False, alpha, beta))

                    alpha = max(alpha, best)

                    board[row][column] = " "
                    
                    if beta <= alpha:
                        break
                    
        return best
 
    else:
        best = math.inf
 
        for row in range(3):
            
            for column in range(3):
              
                if (board[row][column] == " "):
                 
                    board[row][column] = symbols[0]
 
                    best = min(best, minimax(board, True, alpha, beta))

                    beta = min(beta, best)
 
                    board[row][column] = " "

                    if beta <= alpha:
                        break
                    
        return best

def play_again():
    global board
    global user_turn
    global comp_turn
    global num
    global symbols
    global user_name
    
    if winning_condition(board) == -1:
        print(symbols[0],"WINS!")
    elif winning_condition(board) == 1:
        print(symbols[1],"WINS!")
    elif winning_condition(board) == 0:
        print("DRAW!")
    print("Game over")
                    
    user = str(input("Press P to play again Q to quit: "))
    user = user.upper()
    if user != "P" and user!= "Q":
        valid = False
        while not valid:
            user = str(input("Invalid input. Press P to play again Q to quit: "))
            user = user.upper()
            if user == "P" or user == "Q":
                break
            
    if user == "P":
        num = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

        board = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

        symbols = ['', '']
        user_name = str(input("Please enter your name: "))
        user_turn = False
        comp_turn = False
        toss()
        print_board()
        game_loop()
    elif user == "Q":
        sys.exit()

def game_loop():
    global board
    global num
    global user_move
    global user_turn
    global comp_turn
    
    while moves_left(board):

        if moves_left(board) == False:
            break
        
        if winning_condition(board) != 0:
            break
            
        if user_turn == True:            
            player_move()
            
            flag = False
            
            for row in range(0, 3):
                for column in range(0, 3):
                    if num[row][column] == user_move:
                        flag = True
                        board[row][column] = symbols[0]
                        num[row][column] = symbols[0]
                            
            if flag == False:
                while not flag:
                    user_move = eval(input("Area already occupied. Please enter another box position (1-9): "))
                    for row in range(0, 3):
                        for column in range(0, 3):
                            if num[row][column] == user_move:
                                flag = True
                                board[row][column] = symbols[0]
                                num[row][column] = symbols[0]
        
        elif comp_turn == True:
            best_move(board)

        print_board()

    play_again()


print_board()
toss()
game_loop()
