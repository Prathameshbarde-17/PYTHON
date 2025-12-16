"""
#Type of conversion 

num1="30"
num1=int(num1)
num2=20.30
sum = num1 +num2
print("Sum: ",sum)


#Type of casting

num1="30"
num2=20.30
sum = float (num1) + num2
print("Sum:",sum)


#Practice Problem
#Write a problem to input 2 numbers & print their sum

num1= int(input("Enter first number:"))
num2 = int(input("enter second number:"))

sum =num1 + num2
print ("Sum :",sum)

#Write a prongram to input 2 int number a and b
#Print True if a is greater than or equal to b
# if not print false.

a= int (input("Enter a number: "))
b= int (input("Enter b number: "))

if(a>=b):
    print("True")
else:
    print("False")
 """ 

# String
# String is data type that store sequence of characters.

str1="This is a string.\nThis line printed in next line."
str2='This ia single quote string.'
str3='''This is mutli line string.'''

print(str1)
#Concatenation of String
result= str2+str3
print(result)

#Lenth of String
#syntax--> len()
print(len(str1))

#Indexing
str4="Prathamesh"
print(str4[6])

#Slicing 
#syntax--> string_name[start_index:end_index]
str_name= "Hwllo, Iam Python Language."
print(str_name[5:11])


#String Function
#1 endswith("")
str="i am study python now."
print(str.endswith("now."))

#2. capitalize()---->only first letter uppercase
print(str.capitalize())

#3. replace() 
print(str.replace("now","today"))

#4  find()
print(str.find("python"))

#5 count()
print(str.count("o"))

#Exapmles 
#Write a program to input a user first name and print its length.

first_name=input("Enter first name: ")
print("Lenth of first name is:",len(first_name))

#Write a program to find the occurence of $ in a sting 
string_name= "Hi $ this symbol is a dollor $. "
print(string_name.count("$"))