"""
14. Count Digits and Letters in a String

Write a Python program that accepts a string and calculates the number of digits and letters.

Sample Data : Python 3.2

Expected Output :

Letters 6
Digits 2

"""

string = input("Enter a string : ")

digits = 0
letters = 0

for char in string:
    if char.isdigit():
        digits+=1
    elif char.isalpha():
        letters+=1

print("Letters", letters)
print("Digits", digits)


"""
#Questions
Write a Python program to accept a string and calculate separately the number of alphabetic characters and numeric digits.
Write a Python program to iterate over a string and use isalpha() and isdigit() to count letters and digits.
Write a Python program to use a dictionary to store counts of letters and digits from an input string.
Write a Python program to output the counts of digits and letters in a string after filtering out whitespace and punctuation
"""