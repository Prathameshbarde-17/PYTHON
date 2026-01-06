'''Polymorphism in Python

Polymorphism means "many forms" — 
the same function or operator can behave differently depending on the object it is used with.

Polymorphism is one of the core concepts in object-oriented programming.

Operator Overloading
Operator overloading is a feature of object-oriented programming languages that allows operators to have different meanings depending on the type of operands they are applied to.

#Example
'''
class complex:
    def __init__(self,real,imag):
     self.real=real
     self.imag=imag

    def showNum(self):
        print(self.real,"i +",self.imag,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return complex(newReal,newImag)

    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return complex(newReal,newImag)


num1 =complex(1,3)
num1.showNum()
num2 = complex(2,4)
num2.showNum()
num3 = num1 + num2
num3.showNum()
num4 = num1 - num2
num4.showNum()

#Examples
#Define a Circle clas to create a circle with radius r using the contructor.
#Define an area() method of the class to calculate the area of the circle.   
#Define a perimeter() method of the class to calculate the perimeter of the circle.

class Circle:
   def __init__(self,r):
      self.r=r

   def area(self):
      return 3.14*self.r*self.r
   
   def perimeter(self):
      return 2*3.14*self.r
   
c1=Circle(21)
print("radius of circle :",c1.r)
print("Area of circle :",c1.area())
print("Perimeter of circle:",c1.perimeter())


#Examples
#Define a Employee class with attributes role, department and salary.
#This class also showDetails() method.
#Create Engineer class that inherit properties from Employee & has additional 
# attributes : name and  age.


class Employee:
   def __init__(self, role,department, salary):
      self.role=role
      self.department=department
      self.salary=salary

   def showDetails(self):
      print("Role:",self.role)
      print("Department:",self.department)
      print("Salary:",self.salary)

class Engineer(Employee):
   def __init__(self, name,age):
      self.name=name
      self.age=age
      super().__init__("Engineer","IT",50000)

e1=Engineer("Rahul",21)
e1.showDetails()
print("Name:",e1.name)
print("Age:",e1.age)

#Examples
# create a class called Order which stores items & its price.
# Use Dunder function __gt__() to convey that:
# order1>order2 if price of order1> price of order2

class Order:
   def __init__ (self,items,price):
      self.items=items
      self.price=price

   def __gt__ (self,ord2):
      return self.price > ord2.price

ord1=Order("Laptop",50000)
ord2=Order("Mobile",10000)
print(ord1>ord2)