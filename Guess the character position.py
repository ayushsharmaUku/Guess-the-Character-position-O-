mylist = [0,1,2]
from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input('Please choose a position from 0,1 or 2 to find the hidden "O": ')

    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct guess')

    else:
        print('Wrong guess unfortunately!!')
        print(myist)


mylist = ['','O','']

mixed_list = shuffle_list(mylist)

guess = player_guess()

check_guess(mylist,guess)
