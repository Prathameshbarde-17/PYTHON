"""
#List
#A built in data type that stores set of values.
#List is mutable (can be changed)

marks=[10,80,60,50,90,100]
print(marks)
#Accesing element of list
print(marks[3])

#changging value of list
marks[2]=20
print(marks)

#List slicing
print(marks[1:4])

#List Function
Languages=["Python","Java","C","C++", "JavaScript"]
#1. append()--> add element at the end of list 
Languages.append("ReactJs")
print(Languages)
#2. insert()--> add element at specific index
Languages.insert(2,"HTML")
print (Languages)

#3 remove()--> remove element from list
Languages.remove("HTML")
print(Languages)

#4. sort()--> sort the list in asending order
Languages.sort()#ascending order
print(Languages)

#5.reverse()--> reverse the list
#6. pop()--> remove last element of list 
#7.count()--> count the number of occurence of element in list
#8. extend()--> add elements of one list to another list
#9. index()--> return the index of element 
#10. clear()--> remove all elements from list

#Examples
#Write a program to ask user enter names of their 3 favrourite movies and store them in a list

movie1=input("Enter first movie name: " )
movie2=input("Enter second movie name: " )
movie3=input("Enter third movie name: " )

movie=[movie1,movie2,movie3]
print("Favourite movies are:", movie)

#Write a program to check if a list contain a palindrone of element(Hint: use copy() method )

list1=[10,20,10]

copt_list=list1.copy()
copt_list.reverse()

if(copt_list==list1):
    print("Palindrone")
else:
    print("NOT palindrone")

"""


#tuples
#A built in data type that create immutable sequence of values.
#Tuple is mmuatable (cannot be changed value.)

fruits=("Apple", "banana","Mango","Orange")
print(fruits)
#Accesing element of tuple
print(fruits[2])
#fruits[1]="Santra" #error because tuple is immutable

#Slicing
print(fruits[1:3])

#Tuple Function
#1. count()--> count the number of occurence of element in tupple
print (fruits.count("Mango"))

#2. index()--> return the index of element
print(fruits.index("Orange"))


#Examples
#Write a program to count the number of student with the "A"Grade in the following tuple
#("C","D","A","A","B","B","A")

grades=("C","D","A","A","B","B","A")
print("Number of student with the A Grade is:", grades.count("A"))

#Store the above value in a list and sort them from "A" to "D".

grades_list=list(grades)
grades_list.sort()
print("Sorted from grade A to D: ", grades_list)
