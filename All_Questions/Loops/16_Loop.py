"""
16. Numbers with All Even Digits

# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. 
 The numbers obtained should be printed in a comma-separated sequence.
"""

for num in range(100,400):
    if all(int(digit) %2 == 0 for digit in str(num)):
        print(num)

"""
#Questions
Write a Python program to list all numbers between 100 and 400 whose every digit is even.
Write a Python program to filter numbers in a range by converting them to strings and checking if each digit is even.
Write a Python program to use list comprehension to output a comma-separated string of numbers with only even digits.
Write a Python program to implement a function that tests whether all digits in a number are even and apply it to a specified range.
"""