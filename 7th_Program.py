'''Loops in Python'''

#Loops
'''Loops are used to execute a block of code repeatedly intructions until a certain condition is met.  
   Python mainly has two types of loops.
   1. for loop
   2. while loop
   
   # 1. for loop --->
                 used to iterate over a sequence like list, tuple, string etc.
   # 2. while loop-->
                 used to execute a block of code as long as the condition is true.'''
   
 
   # while loop
   #creating while loop

count=1
while count<=5:
    print("Count is:", count)
    count=count+1

#Example
# Write a program to print first n natural numbers using while loop.
# Input: 5
# Output: 1 2 3 4 5

n= int(input ("Enter a number: "))
i=1
while i<=n:
    print(i, end=" ")
    i=i+1 


#Print 100 to 1 in while
num=100
while num>=1:
    print(num)
    num-=1





'''For Loop'''

#creating for loop

fruits =["apple", "banana", "cheerry"]

for fruit in fruits:
    print(fruit)

#Example

#Write a program to print all even number from 1 to n using for loop.
#input: 10
#Output : 2 4 6 8 10

n= int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)


#Print 100 to 1 in while
num=100
while num>=1:
    print(num)
    num-=1


'''Break and Continue statements'''
#Break Statement
'''The braek statement is used to terminate the loop prematurely  when a certain condition is met.'''

for i in range(1,11):
    if i==6:
        break  #break---> stop iteration when i is 6
    print(i)

#continue statement 
'''The continue statement is used to skip the current iteration of the loop and move to the next iteration when a certain condition is met. '''

for i in range(1,11):
    if i==6:
        continue   #continue ---> skip iteration when i is 6
    print(i)



'''Range()'''

'''Range function is used to generate a sequence of numbers. 
   It can take one, two , or three argument.
   1. range (stop) : generate numbers from 0 to stop-1
   2. range (start, stop) : generate numbers from start to stop-1
   3. range (start, stop, step): generate numbers from start to stop-1 with a step value of step.'''

#Examples
#Generate numbers from 0 to 4
for i in range(5):
    print(i)
#Print numbers from 1 to 100
for i in range(1,101):
    print(i)
#Print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)
#Print the multiplication table of a number
num= int(input("Enter a number: "))
for i in range(1,11):
    print(num*i)


'''Pass Statement'''
'''Pass is a null statement in python used as a placeholder for future code'''
 
for i in range (1,11):
    pass   # pass statement used here as a placeholder
    print(i)

#Function with pass statement
def my_function():
    pass  # pass statement used here as a placeholder
my_function()


#End of the code
