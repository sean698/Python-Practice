from random import randint
from os import system
from logo import logo

EASY_LEVEL_LIFE = 10
HARD_LEVEL_LIFE = 5

print(logo)

def setDifficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while True:
        if level == 'easy':
            return EASY_LEVEL_LIFE
        elif level == 'hard':
            return HARD_LEVEL_LIFE
        else:
            level = input("You typed a wrong word, please type again: ")
  

def checkAnswer(guess, realNum, life):
    if guess == realNum:
        print("You win, congratulations!")
        return -1
    elif guess > realNum:
        print("Too high.")
        return life - 1
    else:
        print("Too low.")
        return life - 1

def checkIfGameOver(life):
    if life == 0:
        print("You have run out of attempts, you lost.")
        return True
    elif life == -1:
        return True
    return False

def game():
    realNum = randint(1, 100)
    isGameOver = False
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    life = setDifficulty() 
    while not isGameOver:
        print(f"You have {life} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        life = checkAnswer(guess, realNum, life)
        isGameOver = checkIfGameOver(life)

while(input("Do you want to play a game? Press 'y' to play, press 'n' to end: ") == 'y'):
    system('cls')
    game()        
        