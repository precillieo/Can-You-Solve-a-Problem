# Rock, Paper, Scissors Game

import random
def computer_choice():
    game_choices = ('rock' , 'paper' , 'scissors')
    return game_choices[random.randint(0,2)]

def playon(a):
    if a.lower() == 'yes':
        return True
    else:
        return False

play = True

while play == True:
    print('Choose rock, paper, scissors?')
    choice = str(input())
    computer = computer_choice()
    if choice == computer:
        print('There is a tie!')
        print('\n')
        print('Do you still want to play?')
        stay = str(input())
        play = playon(stay)
    elif choice.lower() == 'rock' and computer.lower() == 'paper':
        print('I won, you suck!')
        print('\n')
        print('Do you still want to play?')
        stay = str(input())
        play = playon(stay)
    elif choice.lower() == 'paper' and computer.lower() == 'scissors':
        print('I won, you suck!')
        print('\n')
        print('Do you still want to play?')
        stay = str(input())
        play = playon(stay)
    elif choice.lower() == 'scissors' and computer.lower() == 'rock':
        print('I won, you suck!')
        print('\n')
        print('Do you still want to play?')
        stay = str(input())
        play = playon(stay)
    elif choice.lower() == 'paper' and computer.lower() == 'rock':
        print('You won, I suck!')
        print('\n')
        print('Do you still want to play?')
        stay = str(input())
        play = playon(stay)
    elif choice.lower() == 'scissors' and computer.lower() == 'paper':
        print('You won, I suck!')
        print('\n')
        print('Do you still want to play?')
        stay = str(input())
        play = playon(stay)
    elif choice.lower() == 'rock' and computer.lower() == 'scissors':
        print('You won, I suck!')
        print('\n')
        print('Do you still want to play?')
        stay = str(input())
        play = playon(stay)
    else:
        print('You gave an invalid option.')
        play = False