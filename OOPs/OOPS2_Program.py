'''Inheritance in Python'''
              
'''when a one class is derived from another class it is called inheritance.

Syntax:    
class derivedClassName(baseClassName):
    <statement-1>
    .
    .
    <statement-N>
    
Example:

class Parent:
    def func1(self):
        print("This function is in parent class.")
        
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
        
obj = Child()
obj.func1()
obj.func2()

Output:
This function is in parent class.
This function is in child class.
'''
#Examples 
 
class Car:
    @staticmethod
    def start():
     print("car started..")
    @staticmethod
    def stop():
      print("car stopped..")
 
class ToyotaCar(Car):
     def __init__(self,name):
       self.name=name
       
car1=ToyotaCar("Fortuner")
car2=ToyotaCar("Camry")

print(car1.start())
print(car1.name)
print(car1.stop())





'''
Types of inheritance:
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

'''

# 1> Single Inheritance
                       # Single Inheritance is a type of inheritance in which one class inherits properties from a single parent class.
#base class
#child class

#Syntax:

class Parent:
    def func1(self):
        print("This function is in parent class.")
class child(Parent):
    def func2(self):
       print("This function is in child class.")

obj=child()
obj.func1()
obj.func2()

# 2> Multiple Inheritance 
                         
# Multiple Inheritance is a type of inheritance in which a class inherits properties from more than one parent class.

#base class1
#base class2
#child class

#Syntax:

class Parent1:
    def func1(self):
       print("This function is a first parent class")

class Parent2:
    def func2(self):
       print("This function is a second parent class.")

class child(Parent1,Parent2):
    def func3(self):
       print("This function is a child class.")

obj=child()
obj.func1()
obj.func2()
obj.func3()

# 3> Multilevel Inheritance

# Multilevel Inheritance is a type of inheritance in which a class inherits properties from a parent class and that parent class inherits properties from another parent class.

#base class
#child class1
#child class2

#Syntax:

class Parent:
    def func1(self):
        print("This function is in parent class.")

class child(Parent):
    def func2(self):
        print("This function is in child class.")

class grandchild(child):
   def func3(self):
       print("This function is in grandchild class.")

obj=grandchild()
obj.func1()
obj.func2()
obj.func3()


# 4> Hierarchical Inheritance

# Hierarchical Inheritance is a type of inheritance in which more than one child class inherits properties from a single parent class.

#base class
#child class1
#child class2

#Syntax:

class Parent:
    def func1(self):
        print("This function is in parent class.")

class child1(Parent):
    def func2(self):
        print("This function is in child1 class.")

class child2(Parent):
    def func3(self):
        print("This function is in child2 class.")

obj1=child1()
obj2=child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()

#5> Hybrid Inheritance

# Hybrid Inheritance is a type of inheritance in which a class inherits properties from more than one parent class.

#base class1
#base class2
#child class

#SUPER( )Method
# super() method is used to access method of parent class.

#Example

class Parent:
    def func1(self):
        print("This function is in parent class.")

class child(Parent):
    def func2(self):
        super().func1()
        print("This function is in child class.")

obj=child()
obj.func2()

#Class Method

# A class method is bound to class and receive class as implicit first argument.

#Example

class Car:
    @classmethod
    def start(cls):
        print("Car started..")

    @classmethod
    def stop(cls):
        print("Car stopped..")

Car.start()
Car.stop()

#Property 

# We use @property decorator on any method in class to use method as property.

#Example

class Car:
    @property
    def start(self):
        print("Car started..")

    @property
    def stop(self):
        print("Car stopped..")

car=Car()
car.start

#setter and getter

# We use @property decorator on any method in class to use method as property.

#Example    
#SETTER-->
        # SETTER is used to change the value of property

class Car:
    @property
    def start(self):
        print("Car started..")

    @start.setter
    def start(self):
        print("Car stopped..")

car=Car()
car.start

#GETTER-->
        # GETTER is used to get the value of property

class Car:
    @property
    def start(self):
        print("Car started..")

    @start.getter
    def start(self):
        print("Car stopped..")

car=Car()
car.start
