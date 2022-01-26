#!/usr/bin/env python3

""" conditionals and while loop"""

round = 0       #integer initiated at 0
while True:     # loop condition
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The life of ______"')
    answer = input("Your guess--> ")
    if answer == 'Brian':
        print('Correct')
        break
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")

