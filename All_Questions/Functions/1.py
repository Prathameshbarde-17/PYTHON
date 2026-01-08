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
def sum(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)
print(sum(1,2,3,4,5))

"""

"""
# 8_Question
# Create a function that accept any number of keyword argument and prints them in the format.
# Key: value
"""

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

print_kwargs(name="Patty",age=20)
print_kwargs(name="Patty",age=20,city="Pune")

"""
# 9_Question
# Write a generator function  that yield even numbers up to specified limit

"""

def even_Generator(limit):
    for i in range(2,limit,2):
        yield i

for i in even_Generator(10):
    print("Even Numbers:",i)

"""
# 10_Question
# create a recursive function to calculate the factorial of a number.
"""

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial : ",factorial(5))
