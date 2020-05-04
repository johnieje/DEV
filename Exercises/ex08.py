"""
Rock Paper Scissors game Script
"""
import sys

print('Welcome to the Rock Paper Scissors Game')

while True:
    user1 = input('Enter Play 1: ')
    user2 = input('Enter Play 2: ')

    if user1 == 'rock' and user2 == 'scissors':
        print('Rock beats Scissors')

    elif user1 == 'rock' and user2 == 'paper':
        print('Paper beats rock')

    elif user1 == 'scissors' and user2 == 'paper':
        print('Scissors beat Paper')

    elif user1 == 'paper' and user2 == 'rock':
        print('paper beats rock')

    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()
