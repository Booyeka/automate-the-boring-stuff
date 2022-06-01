
import random
import time
#make a tic tac toe game

# model physcial board
def print_board(board):
    print()
    print(f"{board['top_L']} | {board['top_M']} | {board['top_R']}".center(20))
    print('--+---+--'.center(20))
    print(f"{board['mid_L']} | {board['mid_M']} | {board['mid_R']}".center(20))
    print('--+---+--'.center(20))
    print(f"{board['low_L']} | {board['low_M']} | {board['low_R']}".center(20))
    print()

# test if winning board is present
def is_winning(board):

    # conditions to win - player O - rows
    if   Board['top_L'] == 'O' and Board['top_M'] == 'O' and Board['top_R'] == 'O':
        print('Player "O" Won!')
        return True
    elif Board['mid_L'] == 'O' and Board['mid_M'] == 'O' and Board['mid_R'] == 'O':
        print('Player "O" Won!')
        return True
    elif Board['low_L'] == 'O' and Board['low_M'] == 'O' and Board['low_R'] == 'O':
        print('Player "O" Won!')
        return True

    # columns - Player O
    elif Board['top_L'] == 'O' and Board['mid_L'] == 'O' and Board['low_L'] == 'O':
        print('Player "O" Won!')
        return True
    elif Board['top_M'] == 'O' and Board['mid_M'] == 'O' and Board['low_M'] == 'O':
        print('Player "O" Won!')
        return True
    elif Board['top_R'] == 'O' and Board['mid_R'] == 'O' and Board['low_R'] == 'O':
        print('Player "O" Won!')
        return True

    #diagonals - Player O
    elif Board['top_L'] == 'O' and Board['mid_M'] == 'O' and Board['low_R'] == 'O':
        print('Player "O" Won!')
        return True
    elif Board['top_R'] == 'O' and Board['mid_M'] == 'O' and Board['low_L'] == 'O':
        print('Player "O" Won!')
        return True

    # conditionals for player X - Rows
    elif   Board['top_L'] == 'X' and Board['top_M'] == 'X' and Board['top_R'] == 'X':
        print('Player "X" Won!')
        return True
    elif Board['mid_L'] == 'X' and Board['mid_M'] == 'X' and Board['mid_R'] == 'X':
        print('Player "X" Won!')
        return True
    elif Board['low_L'] == 'X' and Board['low_M'] == 'X' and Board['low_R'] == 'X':
        print('Player "X" Won!')
        return True

    # columns - player X
    elif Board['top_L'] == 'X' and Board['mid_L'] == 'X' and Board['low_L'] == 'X':
        print('Player "X" Won!')
        return True
    elif Board['top_M'] == 'X' and Board['mid_M'] == 'X' and Board['low_M'] == 'X':
        print('Player "X" Won!')
        return True
    elif Board['top_R'] == 'X' and Board['mid_R'] == 'X' and Board['low_R'] == 'X':
        print('Player "X" Won!')
        return True

    #diagonals - Player X
    elif Board['top_L'] == 'X' and Board['mid_M'] == 'X' and Board['low_R'] == 'X':
        print('Player "X" Won!')
        return True
    elif Board['top_R'] == 'X' and Board['mid_M'] == 'X' and Board['low_L'] == 'X':
        print('Player "X" Won!')
        return True

    else:
        return False

#determine if Draw
def is_draw(board):
    if ' ' not in board.values():
        return True
    else:
        return False
  

#function to test if position is already taken
def is_taken(position):
    if Board[position] != ' ':
        return True
    else:
        return False

def play_game(Board):
    print_board(Board)
    print('1 or 2 players?'.center(20))
    players = input()

    if players == '2':
        turn = 'X'
        while not is_winning(Board):
            if is_draw(Board):
                print("It's a draw!! No one won!")
                break
            if turn == 'X':
                position = input('Player X\'s turn:')
            else:
                position = input('Player O\'s turn:')
                
            try:
                if is_taken(position):
                    print("That position is taken, please try again".center(20))
                    continue
            except KeyError:
                print('unrecognizable input, please try again'.center(20))
                continue

            Board[position] = turn
            print_board(Board)
            if turn == 'X':
                turn = "O"
            else:
                turn = 'X'
    
    else:
        print('heads or tails?')
        if input() == 'heads' or 'tails':
            num = random.randint(1,10)
            if num > 5:
                print('you go first!'.center(20))
                turn = 'X'
            else:
                print('The computer will go first!'.center(20))
                turn = 'O'
            
        while not is_winning(Board):
            if is_draw(Board):
                print("It's a draw!! No one won!".center(20))
                break
            if turn == 'X':
                print('Your turn:'.center(20), end='\n')
                position = input(''.rjust(10))
            else:
                print('Computer\'s turn:'.center(20))
                time.sleep(2)
                while True:
                    pos_list = [
                        0,1,2,
                        3,4,5,
                        6,7,8]
                    num = random.randint(0,len(pos_list)-1)
                    if num == 0:
                        position = 'top_L'
                    elif num == 1:
                        position = 'top_M'
                    elif num == 2:
                        position = 'top_R'
                    elif num == 3:
                        position = 'mid_L'
                    elif num == 4:
                        position = 'mid_M'
                    elif num == 5:
                        position = 'mid_R'
                    elif num == 6:
                        position = 'low_L'
                    elif num == 7:
                        position = 'low_M'
                    elif num == 8:
                        position = 'low_R'

                    if not is_taken(position):
                        break

                
            try:
                if is_taken(position):
                    print("That position is taken, please try again".center(20))
                    continue
            except KeyError:
                print('unrecognizable input, please try again'.center(20))
                continue

            Board[position] = turn
            print_board(Board)
            if turn == 'X':
                turn = "O"
            else:
                turn = 'X'






Board = {
    'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
    'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
    'low_L': ' ', 'low_M': ' ', 'low_R': ' ',
}


play_game(Board)



# future features --- play against computer











    

