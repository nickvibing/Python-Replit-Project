import time
import os
import random


print ("Hello, We're going to be playing a game.")
time.sleep (1)
user_name = input ("What's your name?: ")
time.sleep (1)
print (f"Hey {user_name}. Here Are The Rules\n")
print ("1. You only have 100 lives. Each time there's an error, you lose a life\n2. Don't Get Mad")
time.sleep (1)
os.system ("cls")
def mathGame():
    lives = 100
    print ("Here's the first game")
    time.sleep (1)
    random_guess = random.randint(1,10000)
    while True:
        try: 
            number_guess = int(input("A good old math game.\n Guess The Number out of 10,000!: "))
        except ValueError:
            print("That's not a valid number. Try again.")
            continue
        if number_guess == random_guess:
            print (f"{number_guess} is correct!")
            break
        elif number_guess >= random_guess:
            lives -= 1
            print (f"{number_guess} is way to high. Only {lives} left... ")
        elif number_guess <= random_guess:
            lives -= 1
            print (f"{number_guess} is way to low. Only {lives} left... ")
    return lives
            
def amount(lives):
    print (f"Wow, that only took {100 - lives} lives")
remaining_lives = mathGame()
amount(remaining_lives)

loses = int(input("""Congrats! You passed the first level. Can you do me a favor.
               Choose a number between 1-10"""))
print (f"Okay, you now have {remaining_lives-loses} lives left! I told you this would frustrate you!")

