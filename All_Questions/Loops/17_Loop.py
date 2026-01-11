"""  
17. Alphabet Pattern 'A'

Write a Python program to print the alphabet pattern 'A'.

Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *

"""

num = ""

for row in range(0,7):
    for column in range(0,7):


        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            num = num + "*"
        else:
            num=num + " "
    num=num + "\n"

print(num)


"""
# Method 2
num = 5
for i in range(num):
    if i ==0 or i ==num-1:
        print(" * "*num)
    else:
        print(" * " + " " * (num-2)+" * ")
"""    

"""
#Questions
Write a Python program to print the letter 'A' using nested loops with a fixed pattern of spaces and asterisks.
Write a Python program to generate the pattern for 'A' where the crossbar is centered horizontally.
Write a Python program to use string multiplication and formatting to display the letter 'A' as a pattern.
Write a Python program to construct the pattern of 'A' by dynamically calculating the spacing for each row.
"""