#Definition of functions
def displayboard(board):
    print (f'{board[6]:^7}|{board[7]:^7}|{board[8]:^7}')
    print ('-----------------------')
    print (f'{board[3]:^7}|{board[4]:^7}|{board[5]:^7}')
    print ('-----------------------')
    print (f'{board[0]:^7}|{board[1]:^7}|{board[2]:^7}')
def playermarker():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = (input("Choose X or O: ")).upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
def placemaker (board,marker,position):
    board[position-1] = marker
def wincheck(board,mark):
    return board[0]==board[1]==board[2]==mark or board[3]==board[4]==board[5]==mark or board[6]==board[7]==board[8]==mark or board[0]==board[3]==board[6]==mark or board[4]==board[1]==board[7]==mark or board[5]==board[8]==board[2]==mark or board[0]==board[4]==board[8]==mark or board[6]==board[4]==board[2]==mark
def checkfirst():
    from random import randint
    flip = randint(1,2)
    if flip == 1:
        return 'player 1'
    else:
        return 'player 2'
def spacecheck(board,position):
    return board[position] == ' '
def fullboardcheck(board):
    return board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '
def fullboardcheck1(board):
    for i in range(1,10):
        if spacecheck(board,i):
            return False
    return True
def playerchoice(board):
    position = 0 
    while position not in range (1,10) or not spacecheck(board,position):
        position = int(input('Choose a number from 1-9: (1-9)'))
    return position
def replay():
    choice = ''
    while choice.capitalize() != 'Yes' and choice.capitalize() != 'No':
        choice = (input('Play again? Yes or No: '))
    return choice.capitalize() == 'Yes' 
print ('Welcome to X and O')
#Play the game
while replay():
    ## Set everythin up (board, choose markers and who is first)
    gameboard = [' ']*9
    player1_marker, player2_marker = playermarker()
    turn = checkfirst()
    print (turn + ' is the first player')
    ready = int(input('Ready to play? To answer yes enter 1 to answer no enter 2: '))
    if ready == 1:
        gameon = True
    else:
        gameon = False
    ## Game play
    while gameon:
        ### Player one turn
        if turn == 'player 1':
            #### Show the Board
            print ('\n'*100)
            displayboard(gameboard)
            ##### Choose position
            position = playerchoice(gameboard)
            ##### Place the marker in the position
            placemaker(gameboard,player1_marker,position)
            #####Check if they won
            if wincheck(gameboard,player1_marker):
                print ('\n'*100)
                displayboard(gameboard)
                print ('CONGRATULATIONS, PLAYER ONE YOU HAVE WON THE GAME.')
                gameon = False 
            #####Or if there is a tie
            else:
                if fullboardcheck(gameboard):
                    print ('\n'*100)
                    displayboard(gameboard)
                    print('TIE GAME.')
                    gameon = False
            #####No win, no tie next players turn
                else:
                    print ('\n'*100)
                    turn = 'player 2'
        ### Player two turn
        else:
            #### Show the Board
            displayboard(gameboard)
            ##### Choose position
            position = playerchoice(gameboard)
            ##### Place the marker in the position
            placemaker(gameboard,player2_marker,position)
            #####Check if they won
            if wincheck(gameboard,player2_marker):
                print ('\n'*100)
                displayboard(gameboard)
                print ('CONGRATULATIONS, PLAYER TWO YOU HAVE WON THE GAME.')
                gameon = False 
            #####Or if there is a tie
            else:
                if fullboardcheck(gameboard):
                    print ('\n'*100)
                    displayboard(gameboard)
                    print('TIE GAME.')
                    gameon = False
            #####No win, no tie next players turn
                else:
                    print ('\n'*100)
                    turn = 'player 1'
    if not replay():
       break