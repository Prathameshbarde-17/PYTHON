
'''OOPS IN PYTHON'''

#Encapsulation

#Abstraction

#Inheritance

#Polymorphism

#Data Hiding

#Method Overloading

#Method Overriding

#Constructor

#Destructor

#Super

#Self

#Static

#Abstract

# What is OOP
            # Object oriented programming 
            # To map with real world scenarios we started using object in code.
            # This is a called OOP
            # In simple means object is a real word entity.

'''Class and Objects

class is a blueprint of object
object is a real world entity

syntax:
    class class_name:
        statements
    object_name = class_name()
     #Work
'''
#Examples


class student:
     name="Prathamesh Barde"
     
s1=student()
print(s1.name)

#__init__ Function
                 #Contructor
                 #It is used to initialize the object.
                 #It is automatically called when object is created.
                 #It is called when object is created.
                 
# All classes have function called__init_()


#Creating class
class Student:
     def __init__(self,fullname):
          self.name=fullname

#Creating a Object 
s1=Student("Prathamesh Barde")
print(s1.name)

#The self parameter is a reference to current instance of the class

#The __init__() function is called automatically every time the class is being used to create a new object

'''Constructor
   
   Types of constructor
   1> Default Constructor
   2> Parameterized Constructor
   3> Copy Constructor
   4> Private Constructor
   5> Protected Constructor
   6> Public Constructor
   
   1>Default contructor-->
                      Default contructor is a constructor that takes no arguments.
    
    syntax:
         
          class class_name:
               def __init__(self):
                    statements

    2>Parameterized constructor-->
                      Parameterized constructor is a constructor that takes arguments.
    
    syntax:
         
          class class_name:
               def __init__(self,argument1,argument2):
                    statements
 '''
# Examples             
'''
class Student:
     def __init__(self,fullname):
          self.name=fullname
s1=Student("Prathamesh Barde")
print(s1.name)

class Student:
     def __init__(self,fullname,age):
          self.name=fullname
          self.age=age
s1=Student("Prathamesh Barde",22)
print(s1.name)
print(s1.age)

class Student:
     def __init__(self,fullname,age):
          self.name=fullname
          self.age=age
     def display(self):
          print("Name:",self.name)
          print("Age:",self.age)
s1=Student("Prathamesh Barde",22)
s1.display()

class Student:
     def __init__(self,fullname,age):
          self.name=fullname
          self.age=age
     def display(self):
          print("Name:",self.name)
          print("Age:",self.age)
     def update(self):
          self.age=24
s1=Student("Prathamesh Barde",22)
s1.display()
s1.update()
s1.display()

# Class and Instance Attributes

# Class Attributes
# Instance Attributes
# Examples

class Student:
     name="Collage"
     def __init__(self,fullname,age):
          self.name=fullname
          self.age=age
     def display(self):
          print("Name:",self.name)
          print("Age:",self.age)
     def update(self):
          self.age=25
s1=Student("Prathamesh Barde",22)
s1.display()
s1.update()
s1.display()

#Examples

#Create student class that takes names& marks of 3 subject as argument in contructor 
#Then create a method to print the average.

class student:
     def __init__(self,name,marks):
          self.name=name
          self.marks=marks
      
     def average(self):
          return sum(self.marks)/len(self.marks)
     
s1=student("XYZ",[90,80,70])
print(s1.name)
print(s1.marks)
print("Average Marks:", s1.average())
'''
#static method --->
               # Method that don't use self parameter.(Work at class level)
               # @staticmethod

# syntax:
#                  class class_name:
#                     @staticmethod
#                         def function_name():
#                             statements

class student:
     @staticmethod  #decorator 
     def hello():
          print("Hello I am Static method")

s1= student.hello()


# class method
# Method that use self parameter.(Work at object level)
# @classmethod

# syntax:
#                  class class_name:
#                     @classmethod
#                         def function_name(cls):
#                             statements

class student:
     @classmethod
     def hello(cls):
          print("Hello I am Class method")

s1= student.hello()

#Examples
#Create Account class with 2 attributes balance and account no 
#Create method for debit,credit & printing balance.

class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} debited successfully.")
        else:
            print("Insufficient balance!")

    def credit(self, amount):
        self.balance += amount
        print(f"₹{amount} credited successfully.")

    def print_balance(self):
        print(f"Account No: {self.account_no}")
        print(f"Current Balance: ₹{self.balance}")


# --- Example usage ---
a1 = Account(123456, 10000)
a1.print_balance()

a1.debit(4000)
a1.print_balance()

a1.credit(5111)
a1.print_balance()


#11111

 


 

