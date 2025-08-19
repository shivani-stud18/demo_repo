# "class" is a blueprint for creating objects. It defines the properties and methods of an object. 
# "object" is a copy of the class . It has its own set of attributes and methods . 
# "class" is a template for creating objects. It defines the structure and behavior of an object.

# creating a class
class woman:
    name= ""     # class variable 
    age = 0      # class variable 

# creating an object
obj1 =woman()
obj1.name="Anny"
obj1.age=25

# creating another object
obj2 = woman()
obj2.name="Lily"
obj2.age=24

print (f" My name is {obj1.name} and I am {obj1.age} years old")  # accessing class variable using object
print (f" My name is {obj2.name} and I am {obj2.age} years old")  # accessing class variable using object


# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit the properties and behavior of another class. In Python, inheritance is implemented using the 'class' keyword and the '(ParentClass)' syntax.

# base class
class animal():
    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep!")

# derived class 
class dog(animal):
    def bark(self):
        print("I can bark! woof woof!!")

dog1=dog() # create object of the dog class 
    
dog1.eat()  # call the eat method of the animal class
dog1.sleep()  # call the sleep method of the animal class
dog1.bark();  # call the bark method of the dog class