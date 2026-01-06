"""
# 1_Question
# Write a function that returns the square of a number
"""


def square(number):
    print(number ** 2)

square(5)#25

"""
# 2_Question
# Create a function that takes two numbers as parameter and return their sum.
"""

def sum(num1,num2):
    print(num1+num2)

sum(2,5)

"""
# 3_Question
# Write a function multiply that multiplies two numbers,
but can also accept and multiply strings.
"""

def multiply(str1,str2):
    return str1 * int(str2)

print(multiply(5,5))
print(multiply("a",5))
print(multiply("a","5"))


"""
# 4_Question
# Create a function that return both the area and circumference of a circle given its radius.
"""
import math
def circle_stats(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return area,circumference

a,c=circle_stats(3)
print("Area:", round(a,2),"Circumference:", round(c,2))


"""
# 5_Question
# Write a function that greets a user. if no name is provided, it should greet with a default name.

"""

def greet(name="Patty"):
    return "Hello "  +  name  + "! "

print(greet("Patty"))
print(greet())

"""
# 6_Question
# Create a lambda function to compute the cube of a number.
"""

cube = lambda num: num ** 3
print(cube(3))

"""
# 7_Question
# Write a function that takes variable number of argument and return their sum.

"""

def sum(*args):
    return sum(args)

print(sum(1,2,3,4,5))