"""

13. Filter 4-Digit Binary Numbers Divisible by 5

Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input.
The program will print the numbers that are divisible by 5 in a comma separated sequence.

Sample Data : 0100,0011,1010,1001,1100,1001

Expected Output : 1010
"""

binary_numbers= input("Enter a sequence of comma separated 4 digit binary numbers: ") .split(",")

divisible_by_5 = []

for num in binary_numbers:
    num = num.strip()   # remove extra spaces or text

    # validate 4-digit binary
    if len(num) == 4 and all(bit in "01" for bit in num):
        if int(num, 2) % 5 == 0:
            divisible_by_5.append(num)


print(",".join(divisible_by_5))


"""
#Questions
Write a Python program to accept a sequence of comma-separated 4-digit binary numbers and print those that are divisible by 5.
Write a Python program to convert 4-digit binary strings to integers and filter out those divisible by 5.
Write a Python program to use list comprehension to parse binary numbers and return a comma-separated string of those divisible by 5.
Write a Python program to validate each 4-digit binary number and print only those whose decimal conversion is a multiple of 5.

"""

