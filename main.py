import os
import random
import sys
import json



def get_teams_json():
    with open('name_list.json') as f:
        return json.load(f)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(wrong_guess, right_guess, random_team):
    clear()

    print('Strikes: {}/7'.format(len(wrong_guess)))
    print('')

    for letter in wrong_guess:
        print(letter, end=' ')
    print('/n/n')

    for letter in random_team:
        if letter in right_guess:
            print(letter, end='')
        else:
            print('_', end='')

    print('')


def get_guess(wrong_guess, right_guess):
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in wrong_guess or guess in right_guess:
            print("You've already guessed that letter!")
        else:
            return guess


def play(done):
    clear()
    teams = get_teams_json()
    random_team = random.choice(teams['teams'])
    wrong_guess = []
    right_guess = []

    while True:
        draw(wrong_guess, right_guess, random_team)
        guess = get_guess(wrong_guess, right_guess)

        if guess in random_team:
            right_guess.append(guess)
            found = True
            for letter in random_team:
                if letter not in right_guess:
                    found = False
            if found:
                print("You win!")
                print("The secret word was {}".format(random_team))
                done = True
        else:
            wrong_guess.append(guess)
            if len(wrong_guess) == 7:
                draw(wrong_guess, right_guess, random_team)
                print("You lost!")
                print("The secret word was {}".format(random_team))
                done = True

        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()

def welcome():
    start = input("Press enter to start or 'Q' to quit").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True


print('Welcome to Hangman! You are attempting to guess and NFL team name')

done = False

while True:
    clear()
    welcome()
    play(done)
