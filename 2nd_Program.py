# Comment in Python

# This symbol used for single comment.
"""This is used for multi line comment"""

#Input in Python
"""Input statement is used to accept value using keyword
fromm user"""

#String Input
name= input("First Name: ")
name2=input ("Last Name: ")
print("Full Name is:", name , name2)

#Integer Input
age =int (input("Enter your age: "))
print("Age: ", age)

#Float Input
cgpa = float(input ("Enter yout CGPA: "))
print("CGPA is: ",cgpa)

#Boolean Input
isGraduated = bool(input("Are you graduated: "))
print ("Graduated:",isGraduated)

#Conditional statement 
"""Conditional statement is used to execute a block of code """
#Example 

light =input("light color: ")

if(light == "red"):
    print("Stop")
elif(light =="yellow"):
    print("Go on")
elif(light =="green"):
    print("Move fast")
else:
    print("No signal")
    