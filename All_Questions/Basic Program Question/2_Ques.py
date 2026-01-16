"""
 2_Ques: Find Maximum of two numbers in Python
 Finding the maximum of two numbers in Python helps determine the larger of the two values. 
 For example, given two numbers a = 7 and b = 3, 
 you may want to extract the larger number, which in this case is 7.
 Let's explore different ways to do this efficiently.
"""

# Using max()function

num1 = 10
num2 = 25

maximum = max(num1, num2)
print("The maximum of", num1, "and", num2, "is:", maximum)

# Using if-else statement

a = 45
b = 50
if a > b:
    print("The maximum of",a ,"and",b,"is:",a)
else:
    print("The maximum of",a ,"and",b,"is:",b)

# Using Ternary Operator
x = 15
y = 20
maximum = x if x>y else y
print("The maximum of", x, "and", y, "is:", maximum)

# Using Sort()
numbers =[40,50,8,0,90,]
numbers.sort()
print("The maximum number is:", numbers[-1])

