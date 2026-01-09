



"""
6. Count Even and Odd Numbers

# Write a Python program to count the number of even and odd numbers in a series of numbers

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :

Number of even numbers : 5
Number of odd numbers : 4


"""

numbers =(1,2,3,4,5,6,7,8,9)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 ==0:
        even_count +=1
    else:
        odd_count +=1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)


"""
# Questions
Write a Python program to count the even and odd numbers in a tuple of integers using a loop.
Write a Python program to use list comprehension to separate even and odd numbers from a list and then report their counts.
Write a Python program to implement a function that returns a dictionary with keys 'even' and 'odd' and their respective counts.
Write a Python program to compute the ratio of even to odd numbers in a list and print a formatted summary.
"""
