

"""
# Write a Python program to guess a number between 1 and 9.

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

"""
num = int(input("Enter a number between 1 and 9: "))

while num < 1 or num > 9:
    num = int(input("Enter a number between 1 to 9:"))

print("Well guessed!")


"""
# Write a Python program that randomly selects a number between 1 and 9 and repeatedly prompts the user until the correct guess is made.
"""

import random

num = random.randint(1, 9)

while True:
    guess = int(input("Enter a number between 1 and 9: "))

    if guess ==num:
        print("Well guessed!")
        break
    else:
        print("Try again!")



"""
# Write a Python program to implement a number guessing game with a maximum number of attempts and hints for higher or lower.

"""

import random

num = random.randint(1, 11)

for i in range(5):
    guess = int(input("Enter a number between 1 and 10:"))

    if guess == num :
        print("Well guessed!")
        break
    elif guess > num:
        print("Too high!")
    else:
        print("Too low!")





"""
# Write a Python program to create a guessing game where the program gives feedback on how close the guess is to the target.
"""

import random
target = random.randint(1, 100)

print("Guess the number 1 to 100:")

while True:
    guess = int(input("Enter your guess:"))
   
    difference= abs(target-guess)    

    if difference == 0:
        print("🎉 Correct! You guessed the exact number.")
        break
    elif difference <= 5:
        print("🔥 Very hot! You are extremely close.")
    elif difference <= 10:
        print("♨️ Hot! You are close.")
    elif difference <= 20:
        print("🌡️ Warm. Getting closer.")
    else:
        print("❄️ Cold. You are far away.")


"""                                                                                                                                                                 
# Write a Python program that logs the number of guesses made and congratulates the user once the correct number is guessed.
"""

import random

number = random.randint(1, 10)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses += 1

    if guess == number:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break
