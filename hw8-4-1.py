# Author: Nolan (AMDG) 1/9/2021

import random

number = random.randint(0, 50)

while True:
    user_number = input("Guess a number from 0-50. ")
    if user_number == "stop":
        print("The random number was " + str(number))
        break
    if int(user_number) > number:
        print("Guess lower")
        continue
    elif int(user_number) < number:
        print("Guess higher")
        continue
    elif int(user_number) == number:
        print("You guessed the correct number!")
        break