

"""
4. Construct Pattern (Diamond Pattern)

# Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""

n = 5

for i in range(n):
    for j in range(i):
        print("*", end=" ")

    print(' ')

for i in range( n, 0 ,-1):
    for j in range(i):
        print("*", end=" ")

    print(' ')


"""
Write a Python program to print a pyramid pattern of stars that first increases then decreases using nested loops.
Write a Python program to construct a diamond shape pattern with asterisks, where the widest row is the middle row.
Write a Python program to generate a symmetric star pattern that has an even number of rows and mirror-image halves.
Write a Python program to create an hourglass pattern using a nested for loop, with stars decreasing then increasing in count.
"""
