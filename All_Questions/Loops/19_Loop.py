"""  
Vowel or Consonant Checker

Write a Python program to check whether an alphabet is a vowel or consonant. 

Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.

"""

letter = input("Input a letter of the alphabet: ")

if letter == "a" or letter =="e" or letter == "i" or letter=="o" or letter == "u":
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")

"""
# Request input from the user to input a letter of the alphabet and assign it to the variable 'l'
l = input("Input a letter of the alphabet: ")

# Check if the input letter 'l' is present in the tuple containing vowels ('a', 'e', 'i', 'o', 'u')
if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)  # Display a message stating that the input letter is a vowel
# If the input letter is 'y', display a message stating that it sometimes represents a vowel and sometimes a consonant
elif l == 'y':
    print("Sometimes the letter y stands for a vowel, sometimes for a consonant.")
# If the input letter doesn't fall into any of the above conditions, it is considered a consonant; display a message stating so
else:
    print("%s is a consonant." % l) 
	
"""

"""
#Questions
Write a Python program to check if a given letter is a vowel or a consonant, using a set of vowels for comparison.
Write a Python program to accept a letter and determine its classification, ensuring input validation for alphabets only.
Write a Python program to implement a function that returns "vowel" or "consonant" for a single-character input.
Write a Python program to handle both uppercase and lowercase input and output the correct classification.

"""