"""
12. Sequence of Lines to Lowercase

# Write a Python program that accepts a sequence of lines (blank line to terminate)
  as input and prints the lines as output (all characters in lower case).

"""

lines = []

# Continue to prompt the user for input indefinitely until a blank line is entered
while True:
    # Prompt the user to input a line of text
    l = input()
    
    # Check if the entered line is not empty (non-empty string)
    if l:
        # Convert the entered line to uppercase and append it to the 'lines' list
        lines.append(l.upper())
    else:
        # If the entered line is empty, break out of the loop
        break;

# Iterate through each line in the 'lines' list
for l in lines:
    # Print each line (converted to uppercase) from the 'lines' list
    print(l) 

"""
lines = []

while True:
    line = input("Enter a line: ")

    if line :
       lines.append(line.lower())
    else:
       break

for line in lines:
    print(line)

"""

"""
#Questions
Write a Python program to continuously accept user input lines until a blank line is encountered, then output all lines in lower case.
Write a Python program to read multiple lines from standard input and convert each line to lower case before printing.
Write a Python program to build a list of input lines, convert them to lower case, and print the list.
Write a Python program to implement a loop that terminates on an empty line and prints all captured lines in lower case.

"""
