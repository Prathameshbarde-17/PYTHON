'''Dictionary and Set'''

# Dictionary in python -->
'''Dictionaries are used to store data values in key:value pairs.
They are unordered, changeable and dont allow duplicates keys.'''
 
#Creating a dictionary
student_info={
    "name" : "Patty",
    "cgpa" : 10,
    "isGraduated": True,
    "subjects": ["Python","Java","C++"]
}

print(student_info)

#Accesing values from dictionary

print(student_info["name"])
print(student_info.get("cgpa"))

#Adding new key:value pair to dictionary

student_info["age"]=22
print(student_info)

#Changing value of existing key

student_info["cgpa"]=9.5
print(student_info)

#Removing key:value pair from dictionary

student_info.pop("isGraduated")
print(student_info)

#Dictionary Methods

#1. keys()--> returns all keys of dictionary
print(student_info.keys())

#2. values()--> returns all values of dictionary
print(student_info.values())

#3. items()--> returns all key:values pairs of dictionary
print(student_info.items())

#4. clear()--> removes all items from dictionary
#student_info.clear()
#print(student_info)

#5. copy()--> returns a copy of dictionary
copy_dict= student_info.copy()
print(copy_dict)

#6.update()--> Updates the dictionary with specified key:value pairs
student_info.update({"semester":4})
print(student_info)

#7.fromkeys()
#8.get ()
#9.popitem()
#10.setdefault()
#11.pop()
'''
#Eamples
#Write a program to create a dictionary to store names and marks of 3 students and print the dictionary.
student_info1={
     "name": input("Enter name of first student: "),
     "marks": int(input("Enter marks of first student: "))
}
student_info2={
     "name": input("Enter name of second student: "),
     "marks": int(input("Enter marks of second student: "))
}
student_info3={
     "name": input("Enter name of third student: "),
     "marks": int(input("Enter marks of third student: "))
}
 
print("Student Data :",student_info1,student_info2,student_info3)
#print("Student 2:",student_info2)
#print("Student 3:",student_info3)
'''
#Example
#Write a program to merge two dictionaries.
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
dict1.update(dict2)
print("Merged two dictionary :",dict1)


#Write a program to count the number of occurence of each character in a string
#using dictionary.

string = input("Enter a string: ")
char_count = {}

for ch in string:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("Character count:", char_count)




#Write a Program to find the highest and lowest marks from a dictionary of student marks.

marks_dict={
    "Alice":89,
    "peter":90,
    "John":99,
    "Marry":66,
    "David":55
}

highest_marks=max(marks_dict.values())
lowest_marks=min(marks_dict.values())

print("Highest Marks:",highest_marks)
print("Lowest Marks:",lowest_marks)


#Write a program to sort a dictionary by keys and values.

unsorted_dict={
    "b":3,
    "a":2,
    "d":6,
    "c":7
}
#Sorting 
sorted_by_keys=dict(sorted(unsorted_dict.items()))
#sorted_by_values=dict(sorted(unsorted_dict.items()))
print("Sorted by keys&value",sorted_by_keys)
#print("Sorted by values:",sorted_by_values)

#WAP to merge two dictionaries and sum the values of common keys.

dictA={"a":1,"b":2}
dictB={"c":3,"d":4}
merge_dict=dictA.copy()
for key,value in dictB.items():
    if key in merge_dict:
        merge_dict[key]+=value
    else:
        merge_dict[key]=value

print("Merged dictionary with sum of common keys:",merge_dict)


'''
dictA={"a":1,"b":2}
dictB={"c":3,"d":4}
dictA.update(dictB)
print("Merged dictionary:",dictA)
'''



#Write a program to create a dictionary with keys as numbers from 1 to 5 and values as their squares.
#First Logic
sqaure={
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
print("Dictionary of squares:", sqaure)

#Second Logic

squares_dict={num:num**2 for num in range(1,11)}
print("Dictionary of squares:",squares_dict)

