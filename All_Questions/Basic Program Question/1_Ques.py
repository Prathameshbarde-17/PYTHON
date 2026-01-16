# How to Add Two Numbers in Python

"""
The task of adding two numbers in Python involves taking two input values and computing their sum using various techniques . 
For example, if a = 5 and b = 7 then after addition, the result will be 12.

Using the "+" Operator
+ operator is the simplest and most direct way to add two numbers . It performs standard arithmetic addition between two values and 
returns the result.
"""

a1 = 20
b1 = 50

# Using Input 
result =a1+b1
print("The sum of", a1, "and", b1, "is:", result)


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

sum = a+b
print("The sum of", a, "and", b, "is:", sum)


# Using Function

def add_numbers(x,y):
    return x+y

num1=50
num2=50

result1 = add_numbers(num1,num2)
print("The sum of", num1, "and", num2, "is:", result1)


#Using Lambda Function

add = lambda x, y: x+y

num1 = 15
num2 = 25

result = add(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)

#USing Add operator
import operator
print(operator.add(20,50))

