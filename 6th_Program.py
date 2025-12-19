'''Sets in Python'''

#Sets
'''Set is collection of the unordered items.
Sets are unchangeable, unindexed and do not allow duplicate values.
Sets are defined by curly braces {}.'''

#Creating a set
fruits={"Apple", "Banana", "Mango", "Orange"}
print(fruits)

#Accessing items from set
for fruit in fruits:
    print(fruit)

#Adding items to set
fruits.add("Graphes")
print(fruits)

#Removing items from set
#1
fruits.remove("Banana")
print(fruits)
#2
fruits.discard("Mango")
print(fruits)

#3
fruits.pop()
print(fruits)

#4
fruits.clear()
print(fruits)

#Set Methods

#1. union()
# Combines two sets and returns a new set

set1={1,2,3}
set2={4,3,2}
print(set1.union(set2))

#2. intersection()
# Returns a set that contains the common elements between two sets
print(set1.intersection(set2))

#3. difference()
# Returns a set that contains the elements present in the first set but not in the second set     
print(set1.difference(set2))

#4. issubset()    //Bolean value
# retuns a set that contains all elements of the set
set3={1,2}
print(set3.issubset(set1))

#Exapmles

#Write a program to input 5 numbers from user and store them in a set.

num_set=set()
for i in range(5):
    num_set.add(int(input("Enter number: ")))
    print("Numbers in set:", num_set)

#Write a program to find the common elements between two sets entered by user.

setA =set(input("Enter element of first space set seperated by space: ").split())
setB =set(input("Enter element of second space set seperated by space: ").split())
#common= setA.intersection(setB)
common = setA & setB
print("Common elements between two sets:", common)



#Write a program to find the unique elements from two sets entered by user.

setx= set(input("Enter element of first : ").split())
sety= set(input("Enter element of second : ").split())
#unique= setx.symmetric_difference(sety)
unique= setx ^ sety
print("Unique elements from two sets:", unique)


#Write a program to find the elements present in first set but not in second set.

set1A= set(input("Enter element of first : ").split())
set2B= set(input("Enter element of second : ").split())
difference= set1A.difference(set2B)
print("Elements present in first set but not in second set:", difference)


#Advanced level examples
#write a program to find the largest and smallest element in a set.

num_set={34, 12, 5, 67, 23, 89}
print("Largest value:", max(num_set) )
print("Smallest value:", min(num_set) )

#Write a program to remove duplicates from a list using sets.   Set--> set madhe duplicate value nasate


# set madhe convert karun duplicates remove karayche 
num_list=[1,2,3,4,2,3,5,1,6,4]
num_set=set(num_list)
print("List after removing duplicates:", num_set)


#Write a program to count the number of unique words in a sentence using sets.
sentence= input("Enter a sentence: ")
words= sentence.split()
unique_words= set(words)
print("Number of unique words in the sentence:", len(unique_words))

#Write a program to check if two sets are disjoint or not.
setA= {1,2,3}
setB= {4,5,6}
print(setA.isdisjoint(setB))    
