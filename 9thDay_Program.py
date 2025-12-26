 
''' File I/O in python'''
  
''' File is a collection of data stored in a computer memory.
    It can be created and deleted.
    It can be read and written.
    It can be opened and closed.                
    
    File I/O is used to read and write data in files.
    It is used to store and retrieve data from a file. 
    
Types of all files

1> Text files --->extension: .txt , .docx , .pdf ,.doc ,.csv, .xlsx etc
2> Binary files---> extension: .jpg ,.png, .jpeg, .gif etc


Open , read and close files
                    ---->  we have to open file before reading and writing 
Syntax

      f = open("file_name","mode")
      f.read()
      f.close()




Modes:

1> "r"---> read mode(default)
2> "w"---> write mode
3> "a"---> append mode
4> "x"---> create mode
5> "b"---> binary mode
6> "t"---> text mode(default)
7> "+"---> read and write mode

combined modes: 1> r+ , 2> w+ , 3> a+

'''
'''
#Examples

#Default mode
f= open("File_INPUT.txt","r")
data= f.read()
print(data)
f.close()

#Write mode
f= open("File_INPUT.txt","w")
f.write("Now Firstly remove data from file and write a new data in file .")
#print(f.read())
f.close()

#Append Mode

f= open("File_INPUT.txt", "a")
f.write("\nNow this is append mode that mean we can add new data in file.")
f.close()

#Create Mode
#f= open("new_File_INPUT.txt","x")
#f.write("Create a new file and write data in it.")

#f.close()


#R+
f= open ("File_INPUT.txt", "r+")
data= f.read()
print(data)
f.write("\n Now this ia read and write mode.")
f.close()

#W+
f= open ("new_File_INPUT.txt", "w+")
f.write ("Create a new file and write a data in it.")
f.close

#A+
f= open("new_File_INPUT.txt","a+")
f.write ("\nNow this is append mode that next line will add new data in the file..")
f.close

'''

# Examples most Important 

#Create a new file "practice.txt" using python. Add the following data in it.
"""Hi eveyone
   We are leaning file I/O in python
   using a java.
   I like programmming in java."""

file = open("practice.txt","w")
file.write("Hi eveyone\n")
file.write("We are learning file I/O in PYTHON.\n")
file.write("using a JAVA.\n")
file.write("I like programmming in JAVA.")
file.close()


#WAF that replace all occurance of "Java" with "Python" in a above file.

file = open("practice.txt","r")
data = file.read()
new_data = data.replace("JAVA","PYTHON")
print(new_data) 
file.close()
file=open ("practice.txt","w")
file.write(new_data)
file.close()

# search if the word "learning" exist in the file or not.

file =open("practice.txt","r")
data=file.read()
print("Learning word exist in file or not:", "learning" in data)
file.close()

#WAF to find in which line the word "learning" exist in the file.Print -1 if word not exist.
# This first way
file=open("practice.txt","r")
data=file.read()

if "learning" in data:
    print("line number:",data.find("learning"))
else:
    print("-1")

    file.close()

# This second way [Function ]
def check_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as file:
        while data:
            data = file.readline()
            if word in data:
                print("Line Number:",line_no)
                return
            line_no=line_no+1
        
        return-1 
        print(check_line())

#From a file containing numbers seperated by commas, print count of even numbers
count = 0

# Open the file in read mode
with open("numbers.txt", "r") as f:
    data = f.read()

# Split the numbers by comma
values = data.split(",")

# Loop through each value
for val in values:
    val = val.strip()  # remove spaces or newlines
    if val == "":      # skip empty values
        continue
    if int(val) % 2 == 0:
        count += 1

print("Count of even numbers:", count)

