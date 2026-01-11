"""
 Dog Age in Dog Years

Write a Python program to calculate a dog's age in dog years.

Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73

"""

dog_age= int(input("Enter a Dog age in human years: "))

if dog_age <= 2:
    dog_age = dog_age * 10.5
else:
    dog_age = (2* 10.5) + ( dog_age - 2) * 4

print(f"The dog's age in dog's years is {dog_age}")


"""
#Questions
Write a Python program to convert a dog's age in human years to dog years using different multipliers for the first two years and subsequent years.
Write a Python program to prompt the user for a dog's age and output the equivalent dog years with conditional calculations.
Write a Python program to implement the dog age conversion using a function that handles fractional human ages.
Write a Python program to calculate dog years by reading input and applying a formula that distinguishes between early and later years.
"""