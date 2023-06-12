import random

number = random.randint(1,100)

easy = 10

hard = 5

print('''Number Guesser Game!!
I am guessing the number between 1 to 100.''')

difficulity = input("What mode do you wanna play in 'easy' or 'hard': ")

def guesser():
    lives = 0
    if difficulity == 'easy':
        lives = easy
    elif difficulity == 'hard':
        lives = hard
    elif difficulity != 'easy' or 'hard':
        print("Wrong Input.")
        exit()
    guessed = False
    def check():
        if guess > number:
            print('Too High')
        elif guess < number:
            print('Too Low')
    while lives != 0 and guessed == False:
        guess = int(input('Guess a Number: '))
        if guess == number:
            print("You guessed the number!")
            guessed = True
        elif guess != number:
            check()
            print("Guess again.")
            lives -= 1
            print(f"Attempts left {lives}")
            if lives == 0:
                print("0 Attempts left.")
            else:
                pass
        else:
            pass

guesser()