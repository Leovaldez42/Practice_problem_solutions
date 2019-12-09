""" Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
    print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock """


import random

stop = False

while not stop:
    x = input("Enter r for rock, s for scissor and p for paper to play: ")
    y = random.choice(['r', 'w', 'p'])
    print(x)
    print(y)

    if x.lower() == y:
        print("it is a tie")
    elif x.lower() == 'r' and y == 'p':
        print("you lose")
    elif x.lower() == 'p' and y == 's':
        print("you lose")
    elif x.lower() == 's' and y == 'r':
        print("you lose")
    elif x.lower() == 'r' and y == 's':
        print("you win")
    elif x.lower() == 'p' and y == 'r':
        print("you win")
    elif x.lower() == 's' and y == 'p':
        print("you win")
    answer = input('Do you want to start a new game? (Yes or No)')

    if answer == 'Yes':
        print('New game will start')
    elif answer == 'No':
        stop = True
        print('GAME OVER')