import random


def is_win(player, opponent):
    # rock(r) > scissors(s), scissors(s) > paper(p), paper(p) > scissors(s)
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "tie"

    while user != computer:
        if is_win(user, computer):
            return 'You won'
    else:
        return 'You Lost!'


print(play())
