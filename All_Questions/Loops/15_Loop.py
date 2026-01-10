"""
15. Password Validity Checker

Write a Python program to check the validity of passwords input by users.

Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

"""
import re
password = input("Input your password : ")
x=True
while x:
   if len(password)<6 or len(password)>16:
    break
   elif not re.search("[a-z]",password):
    break
   elif not re.search("[A-Z]",password):
    break
   elif not re.search("[0-9]",password):
    break
   elif not re.search("[$#@]",password):
    break
   else:
    print("Valid Password!")
    x = False
    break

if x:
    print("Not a Valid Password")


"""
#Questions
Write a Python program to validate a password ensuring it has at least one lowercase, one uppercase, one digit, and one special character, with length constraints.
Write a Python program to prompt the user for a password and check it against a set of complexity rules, outputting validation errors.
Write a Python program to use regular expressions to verify that an input string meets password criteria including mixed cases and digits.
Write a Python program to implement a password checker that returns True only if the password satisfies all given rules, otherwise False.
"""

