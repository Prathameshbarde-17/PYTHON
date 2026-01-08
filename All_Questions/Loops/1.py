
"""
#1. Divisible by 7 and Multiples of 5

# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

"""
n1=[]
for num in range(1500, 2701):
    if num % 7 ==0 and num % 5 == 0:
     n1.append(num)

print(n1)  
#print(",".join(n1))

"""
# Write a Python program to list numbers between 1000 and 3000 that are divisible by 7 but not by 5.

"""
n2=[]
for num in range(1000,3000):
   if num % 7 ==0 and num % 5 != 0:
      n2.append(num)

print(n2)


"""
# Write a Python program to count how many numbers between 1500 and 2700 are divisible by 7 and also multiples of 5.

"""

n=[]
for num in range(1500,2701):
   if num % 7 ==0 and num % 5 ==0:
      n.append(num)

print(len(n))


"""
# Write a Python program to compute the sum of numbers between 1500 and 2700 that are divisible by 7 and multiples of 5.

"""

n4=[]

for num in range(1500,2700):
   if num % 7 ==0 and num%5==0:
      n4.append(num)

print(sum(n4))




"""
Write a Python program to generate a comma-separated string of numbers between 1500 and 2700 that satisfy being divisible by 7 and multiples of 5.

"""

n5=[]

for num in range(1500,2700):
   if num % 7 ==0 and num%5==0:
      n5.append(str(num))

print(",".join(n5))
