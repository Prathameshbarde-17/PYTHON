'''Functions in Python
   A Function is a block of statement that perform a specific task. 
   A function is executed when it is called.
   
   syntax:
    def function_name(parameters):  #function defination
          statements
          return value
    function_name(arguments)      #function call'''

# Examples 1:
#Sum 
def sum (a,b):
    s=a+b
    return s
print("Sum is: ",sum(5,10))

#Examples 
#Write a function to find the maximum of three numbers.

def max(a,b,c):
    if (a>=b) and (a>=c):
        return a
    elif (b>=a) and (b>=c):
        return b
    else:
        return c
high_num= max(10,20,70)
print("Maximum number is:", high_num)


#Examples
# Write a function to print the length of a list (list is a parameter)  
my_list=[10,20,30,40,50,60,70,80,90,100]

def length(list):
    print(len(list))

length(my_list)

#Examples
# Write a function to print the element of a list in a single line.(list is the parameter)

my_list1=[10,20,30,40,50,60,70,80,90,100]

def print_list(list):
    for items in list:
        print(items, end = "")
    print_list(my_list1)
#print()

#Write a Function factorial of n.

def print_fact(n):
 fact=1
 for i in range(1,n+1):
    fact=fact*i
    print(fact)
print_fact(5)

#Write a function to convert USD to INR

def converter(usd_val):
   inr_val=usd_val*83
   print(usd_val, "$ =", inr_val, "INR")
converter(3)
converter(2)
converter(1)




"""
Recursion in Python

Recursion is a programming concept where a function calls itself as a subroutine. 
In Python, a recursive function can be defined by using the def keyword.

In simply understand about recursion is a function calling itself agaun and again.


syntax:
     
      def function_name(parameters):
          statements
          function_name(arguments)

          function_name(arguments)

          function_name(arguments)

          return
    
          function_name(parameters)

          return



"""
#Example of Recursion
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
