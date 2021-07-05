import sys
import math
import pygame

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

count = 1

pygame.init()

width = 595

go_first = True

screen = pygame.display.set_mode((width, width))

pygame.display.set_caption("TicTacToe by Sarmad")

x_image = pygame.transform.scale(pygame.image.load("images\X.png"), (195, 195))
o_image = pygame.transform.scale(pygame.image.load("images\O.png"), (195, 195))


font = pygame.font.SysFont("Candara", 30)

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
red = (128, 0, 32)
blue = (0, 0, 255)
lilac = (200,162,200)
purple = (153,102,204)
seagreen = (32,178,255)
georgiapeach = (249,114,114)
teal = (0,128,128)


symbols = ["X", "O"]

pygame.display.update()

def message(msg, color, position):
    text = font.render(msg, True, color)
    screen.blit(text, (position))
    pygame.display.update()

def moves_left():
    for row in range(3):
        for column in range(3):
            if board[row][column] == " ":
                return True       
    return False

def winning_condition():
    
    if board[0][0] == symbols[0] and board[0][1] == symbols[0] and board[0][2] == symbols[0] or board[1][0] == symbols[0] and board[1][1] == symbols[0] and board[1][2] == symbols[0] or board[2][0] == symbols[0] and board[2][1] == symbols[0] and board[2][2] == symbols[0] or board[0][0] == symbols[0] and board[1][0] == symbols[0] and board[2][0] == symbols[0] or board[0][1] == symbols[0] and board[1][1] == symbols[0] and board[2][1] == symbols[0] or board[0][2] == symbols[0] and board[1][2] == symbols[0] and board[2][2] == symbols[0] or board[0][0] == symbols[0] and board[1][1] == symbols[0] and board[2][2] == symbols[0] or board[0][2] == symbols[0] and board[1][1] == symbols[0] and board[2][0] == symbols[0]:
        return 1

    elif board[0][0] == symbols[1] and board[0][1] == symbols[1] and board[0][2] == symbols[1] or board[1][0] == symbols[1] and board[1][1] == symbols[1] and board[1][2] == symbols[1] or board[2][0] == symbols[1] and board[2][1] == symbols[1] and board[2][2] == symbols[1] or board[0][0] == symbols[1] and board[1][0] == symbols[1] and board[2][0] == symbols[1] or board[0][1] == symbols[1] and board[1][1] == symbols[1] and board[2][1] == symbols[1] or board[0][2] == symbols[1] and board[1][2] == symbols[1] and board[2][2] == symbols[1] or board[0][0] == symbols[1] and board[1][1] == symbols[1] and board[2][2] == symbols[1] or board[0][2] == symbols[1] and board[1][1] == symbols[1] and board[2][0] == symbols[1]:
        return -1

def minimax(isMaximizing, alpha, beta):    
    score = winning_condition()
 
    if (score == 1):
        return score
 
    if (score == -1):
        return score
 
    if (moves_left() == False):
        return 0
 
    if (isMaximizing) :    
        best = -math.inf
 
        for row in range(3) :        
            for column in range(3) :
              
                if (board[row][column]== " "):
                 
                    board[row][column] = symbols[0]
 
                    best = max(best, minimax(False, alpha, beta))
 
                    board[row][column] = " "

                    alpha = max(best, alpha)

                    if beta <= alpha:
                        break
                    
        return best
 
    else :
        best = math.inf
 
        for row in range(3) :        
            for column in range(3) :
              
                if (board[row][column] == " "):
                 
                    board[row][column] = symbols[1]
 
                    best = min(best, minimax(True, alpha, beta))
 
                    board[row][column] = " "

                    beta = min(best, beta)

                    if beta <= alpha:
                        break
                    
        return best
    

def best_move():
    bestScore = -math.inf
    
    for row in range(3):    
        for column in range(3):
         
            if (board[row][column] == " "):
             
                board[row][column] = symbols[0]
 
                moveScore = minimax(False, -math.inf, math.inf)
 
                board[row][column] = " "

                if (moveScore > bestScore):               
                    bestMove = (row, column)
                    bestScore = moveScore

    board[bestMove[0]][bestMove[1]] = symbols[0]
    insert_best_move(bestMove)

def insert_best_move(bestMove):
    if bestMove == (0, 0):
        screen.blit(x_image,(0, 0))

    elif bestMove == (0, 1):
        screen.blit(x_image,(200, 0))
        
    elif bestMove == (0, 2):
        screen.blit(x_image,(400, 0))
        
    elif bestMove == (1, 0):
        screen.blit(x_image,(0, 200))
                                
    elif bestMove == (1, 1):
        screen.blit(x_image,(200, 200))
        
    elif bestMove == (1, 2):
        screen.blit(x_image,(400, 200))
                        
    elif bestMove == (2, 0):
        screen.blit(x_image,(0, 400))
                        
    elif bestMove == (2, 1):
        screen.blit(x_image,(200, 400))
                        
    elif bestMove == (2, 2):
        screen.blit(x_image,(400, 400))

def insert(position, x_turn, o_turn):

    global count
     
    #for 1
    
    if position[0] > 0 and position[0] < 200 and position[1] > 0 and position[1] < 200 and board[0][0] == " ":
        if x_turn == True:
            screen.blit(x_image,(0, 0))
            board[0][0] = "X"
                        
        elif o_turn == True:
            screen.blit(o_image,(0, 0))
            board[0][0] = "O"

    elif position[0] > 0 and position[0] < 200 and position[1] > 0 and position[1] < 200 and board[0][0] != " ":
        count -= 1

    #for 2

    elif position[0] > 200 and position[0] < 400 and position[1] < 200 and board[0][1] == " ":
        if x_turn == True:
            screen.blit(x_image,(200, 0))
            board[0][1] = "X"
                        
        elif o_turn == True:
            screen.blit(o_image,(200, 0))
            board[0][1] = "O"

    elif position[0] > 200 and position[0] < 400 and position[1] < 200 and board[0][1] != " ":
        count -= 1


    #for 3

    elif position[0] > 400 and position[0] < 600 and position[1] < 200 and board[0][2] == " ":
        if x_turn == True:
            screen.blit(x_image,(400, 0))
            board[0][2] = "X"
                        
        elif o_turn == True:
            screen.blit(o_image,(400, 0))
            board[0][2] = "O"

    elif position[0] > 400 and position[0] < 600 and position[1] < 200 and board[0][2] != " ":
        count -= 1


    #for 4

    elif position[0] > 0 and position[0] < 200 and position[1] < 400 and board[1][0] == " ":
        if x_turn == True:
            screen.blit(x_image,(0, 200))
            board[1][0] = "X"
                        
        elif o_turn == True:
            screen.blit(o_image,(0, 200))
            board[1][0] = "O"

    elif position[0] > 0 and position[0] < 200  and position[1] < 400 and board[1][0] != " ":
        count -= 1


    #for 5

    elif position[0] > 200 and position[0] < 400 and position[1] < 400 and board[1][1] == " ":
        if x_turn == True:
            screen.blit(x_image,(200, 200))
            board[1][1] = "X"
                        
        elif o_turn == True:
            screen.blit(o_image,(200, 200))
            board[1][1] = "O"

    elif position[0] > 200 and position[0] < 400  and position[1] < 400 and board[1][1] != " ":
        count -= 1


    #for 6

    elif position[0] > 400 and position[0] < 600 and position[1] < 400 and board[1][2] == " ":
        if x_turn == True:
            screen.blit(x_image,(400, 200))
            board[1][2] = "X"
                        
        elif o_turn == True:
            screen.blit(o_image,(400, 200))
            board[1][2] = "O"

    elif position[0] > 400 and position[0] < 600 and position[1] < 400 and board[1][2] != " ":
        count -= 1


    #for 7

    elif position[0] > 0 and position[0] < 200 and position[1] < 600 and board[2][0] == " ":
        if x_turn == True:
            screen.blit(x_image,(0, 400))
            board[2][0] = "X"
                        
        elif o_turn == True:
            screen.blit(o_image,(0, 400))
            board[2][0] = "O"

    elif position[0] > 0 and position[0] < 200 and position[1] < 600 and board[2][0] != " ":
        count -= 1
    
    
    #for 8

    elif position[0] > 200 and position[0] < 400 and position[1] < 600 and board[2][1] == " ":
        if x_turn == True:
            screen.blit(x_image,(200, 400))
            board[2][1] = "X"
                        
        elif o_turn == True:
            screen.blit(o_image,(200, 400))
            board[2][1] = "O"

    elif position[0] > 200 and position[0] < 400 and position[1] < 600 and board[2][1] != " ":
        count -= 1


    #for 9

    elif position[0] > 400 and position[0] < 600 and position[1] < 600 and board[2][2] == " ":
        if x_turn == True:
            screen.blit(x_image,(400, 400))
            board[2][2] = "X"
                        
        elif o_turn == True:
            screen.blit(o_image,(400, 400))
            board[2][2] = "O"

    elif position[0] > 400 and position[0] < 600 and position[1] < 600 and board[2][2] != " ":
        count -= 1

    
def play_again():
    
    global board
    global count
    
    play_game = pygame.draw.rect(screen, teal,(200, 260, 190, 35))
    quit_game = pygame.draw.rect(screen, red,(235, 320, 120, 35))
    message("Play Again", black, (225, 265))
    message("Quit", black, (265, 325))
    valid = False
    while not valid:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()

                if play_game.collidepoint(position):
                    valid = True
                    board = [[" ", " ", " "],
                             [" ", " ", " "],
                             [" ", " ", " "]]
                    count = 1
                    game_start()
                    play_again()

                elif quit_game.collidepoint(position):
                    valid = True
                    pygame.quit()
                    sys.exit()
                    
def print_board():
    line = 0
    for i in range(1, 3):
        line = i * (width // 3)
        pygame.draw.line(screen, seagreen, (line, 0), (line, width), 10)
        pygame.draw.line(screen, seagreen, (0, line), (width, line), 10)
        pygame.display.update()
    


def game_start():
    screen.fill(gray)
    message("Welcome to TicTacToe!", black, (150, 200))
    message("You vs", black, (250, 260))

    with_human = pygame.draw.rect(screen, lilac,(120, 315, 120, 50))
    with_ai = pygame.draw.rect(screen, red,(345, 315, 120, 50))

    message("Human", black, (133, 327))
    message("AI", black, (390, 327))
    pygame.display.update()

    valid = False
    while not valid:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()

                if with_human.collidepoint(position):
                    valid = True
                    human()
                                        
                elif with_ai.collidepoint(position):
                    valid = True
                    ai()
                    

def human():

    global count

    screen.fill(lilac)
    print_board()
    game_end = False

    while not game_end:
        
        if count % 2 == 0:
            x_turn = False
            o_turn = True
            
        elif count % 2 != 0:
            x_turn = True
            o_turn = False

        if winning_condition() == 1:
            game_end = True
            screen.fill(georgiapeach)
            message("X WINS", black, (245, 200))

        elif winning_condition() == -1:
            game_end = True
            screen.fill(seagreen)
            message("O WINS", black, (245, 200))

        elif moves_left() == False:
            game_end = True
            screen.fill(gray)
            message("DRAW", black, (250, 200))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                insert(position, x_turn, o_turn)
                count += 1
                pygame.display.update()

        pygame.display.update()
        
def ai():

    global count
    
    screen.fill(red)

    message("Do you want to go first? (Y/N): ", black, (100, 270))

    valid = False

    while not valid:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    o_turn = True               #O is human player
                    x_turn = False
                elif event.key == pygame.K_n:
                    x_turn = True               #X is computer
                    o_turn = False
                valid = True
                    
    screen.fill(red)
    print_board()
    
    game_end = False

    while not game_end:

            
        if o_turn == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    count = 1
                    insert(position, x_turn, o_turn)
                    count += 1
                    if count == 2:
                        o_turn = False
                        x_turn = True

        if winning_condition() == 1:
            screen.fill(georgiapeach)
            message("X WINS", black, (245, 200))
            break

        elif winning_condition() == -1:
            screen.fill(seagreen)
            message("O WINS", black, (245, 200))
            break
            

        elif moves_left() == False:
            screen.fill(gray)
            message("DRAW", black, (250, 200))
            break
                                               
        if x_turn == True:
            best_move()
            o_turn = True
            x_turn = False
        
        pygame.display.update()
            
                
game_start()
play_again()
