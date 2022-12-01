
'''Tic-Tac-Toe Game
Created by R. Griffin
Concept: 2 players use the 'X' and 'O' game pieces on a 3 x 3 game board. Winner is getting the game pieces 3 in a row'''

import random
import time
winner = None
gameRunning = True
currentPlayer = 'X'
comp = input("Is there more than one(1) player?(yes/no): ").lower()
# create the players, to use the AI use the random choice feature
game_piece = ["X", "O"]  # declare the game pieces to use

# have the program to randomly choose the game piece for the player.
p1 = random.choice(game_piece)
p2 = random.choice(game_piece)
while p2 == p1:  # if both of  the variables are the same value,  have it rechoose.
    p2 = random.choice(game_piece)


def Players(p1, p2):
    global currentPlayer
    print(f"player 1, you are \'{p1}\'.")
    print(f"player 2, you are \'{p2}\'.")
    if p1 == currentPlayer:
        print("Player 1 is going first")
    else:
        print("Player 2 is going first")
Players(p1, p2)


# create the board
board = [' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ']

def GameBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# player input for the game board.


def PlayerInput(board):
    global p1, p2, currentPlayer
    if p1 == currentPlayer:
        p1Choose = int(input("Player 1, choose a spot(1-9): "))
        if p1Choose >= 1 and p1Choose <= 9 and board[p1Choose-1] == ' ':
            board[p1Choose-1] = currentPlayer
        else:
            print("Sorry, Player 2 is already in that spot")
    else:
        p2Choose = int(input("Player 2, choose a spot(1-9): "))
        if p2Choose >= 1 and p2Choose <= 9 and board[p2Choose-1] == ' ':
            board[p2Choose-1] = currentPlayer
        else:
            print("Sorry, Player 1 is already in that spot")

def CompInput(board):
    global comp
    if comp == 'yes':
        pass
    else: 
        while currentPlayer == 'O':
            print("I will now choose my spot...")
            time.sleep(1)
            compchoice = random.randint(0,8)
            if board[compchoice] == ' ':
                board[compchoice] = 'O'
                SwitchPlayer()
            else:
                print("Looks like I picked the wrong spot, hold on..")
                continue 
                time.sleep(1)



# check the 3 in a row condition, and declare the winner.
def CheckHorz(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != ' ':
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != ' ':
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != ' ':
        winner = board[6]
        return True


def CheckRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != ' ':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        winner = board[2]
        return True


def CheckDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != ' ':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != ' ':
        winner = board[2]
        return True


def CheckTie(board):
    global gameRunning
    if ' ' not in board:
        GameBoard(board)
        print("There is a tie Game!")
        gameRunning = False


def SwitchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'


def CheckWin():
    global p1, p2, gameRunning
    
    if CheckHorz(board) or CheckRow(board) or CheckDiag(board):
        if p1 == winner:
            GameBoard(board)
            print(f"The Winner is Player 1({p1}).")
        else:
            GameBoard(board)
            print(f'The Winner is Player 2({p2}). ')
        gameRunning = False


while gameRunning:
    GameBoard(board)
    PlayerInput(board)
    CheckWin()
    CheckTie(board)
    SwitchPlayer()
    CompInput(board)
    CheckWin()
    CheckTie(board)
    
