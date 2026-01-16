"""  
Factorial of a Number 

Given an integer n, the task is to compute its factorial, i.e., the product of all positive integers from 1 to n.
Factorial is represented as n! and is commonly used in mathematics, permutations and combinatorics. 
For Example:

Input: n = 6
Output: 720
Explanation: 6! = 6 × 5 × 4 × 3 × 2 × 1 = 720
"""

# Using math.factorial() function
import math
num = int(input("Enter a number to find factorial: "))
factorial =math.factorial(num)
print("Factorial Number : ",factorial)


#Using NumPy np.prod() function

import numpy as np
num = int(input("Enter a number to find factorial: "))
facto=np.prod(np.arange(1,num+1))
print("Factorial Number : ",facto)

# Using Iterative for loop Approach

num = int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(1,num+1):
    factorial =factorial*i
print("Factorial Number : ",factorial)

 # Using Recursive Function

def factorial(n):

    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter a number to find factorial: "))
result =factorial(num)
print("Factorial Number : ",result) 