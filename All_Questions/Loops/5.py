


"""

5. Reverse a Word

Write a Python program that accepts a word from the user and reverses it.

"""
"""
# Solution 1
word = input("Enter a word: ")

reversed_word = word[ ::-1 ]

print("Reversed word:", reversed_word)

"""

#Solution 2

word = input("Enter a word: ")

reverse_Word=" "

for i in range(len(word)-1,-1,-1):
    reverse_Word += word[i]

print("Reversed word:", reverse_Word)


"""
#Questions
Write a Python program to reverse a word entered by the user using slicing.
Write a Python program to reverse each word in a sentence while maintaining the word order.
Write a Python program to recursively reverse a given string without using slicing.
Write a Python program to reverse a word using a stack data structure to simulate character popping.
