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
    print (f" You now only have {remaining_lives}")
remaining_lives = mathGame()
amount(remaining_lives)

print ("Congrats! You passed the first level. Now, can you do me a favor...")
loses = int(input("Choose a number between 1-10"))
print (f"Okay, you now have {remaining_lives-loses} lives left! I told you this would frustrate you!")

print ("I have a question for you again... No tricks this time!")
option = input ("Do you want to regain some of your lives back? Your either in or your out. We can do a game of higher or lower?: ")
option = option.lower() 
if option == "Yes" or option == "Y":
    print ("Yes!")
    def higherlower():
        print ("It's simple. I'll give you a number. You have to guess whether the next number will be higher or lower. You guess correctly, you gain a life back. Incorrectly and yah...")
        while True:
            randomnumber = random.randint(1,10000)
            randomnumber1 = random.randint(1,10000)
            print (randomnumber)
            userguess = input("Will the next number be higher or lower.")
            userguess =userguess.lower()
            if  randomnumber <= randomnumber1: 

elif option != "Yes" or option != "Y":
    print ("Interesting...")
    time.sleep (1)
    print ("To bad... we're still playing!")
    def higherlower():
        
