class bike:
     name=""
    #  constructor function
     def __init__(self,name=""):
         self.name=name

     def display(self):
          print("Name of the bike is:",self.name)
bike1=bike("mountain bike")
bike1.display()
print("-----------")

# Multiple Inheritance

class mammal:
     def mammal_info(self):
          print("Mammals have hair and feed their young ones with milk")

class wingedanimal:
     def wingedanimal_info(self):
          print("Winged animals can fly")

class bat(mammal,wingedanimal) :
     pass

b1=bat()                   
b1.mammal_info()
print("-----------")
b1.wingedanimal_info()
print("-----------")

# Multilevel Inheritance

class superclass:
     def super_method(self):
          print("This is a method of superclass")

class derivedclass1(superclass):
     def derived1_method(self):
          print("This is a method of derived class 1")
          
class derivedclass2(derivedclass1):
     def derived2_method(self):
          print("This is a method of derived class 2")
     
d2=derivedclass2()
d2.super_method()    
print("-----------")
d2.derived1_method()
print("-----------")
d2.derived2_method()

# encapsulation

# public member
class public:
     def __init__(self):
          self.name="john"
          self.age=25

     def display_name(self):
          print(self.name)
          print(self.age)

print("-----------")
object=public()
object.display_name()

# protected member

class protected:
     def __init__(self):
          self._age=20
          self._name="jake"


class subclass(protected):
     def display_age(self):
          print(self._age)

     def display_name(self):
               print(self._name)
       
print("-------------")
obj=subclass() 
obj.display_name()
obj.display_age()

# private method

class private:
     def __init__(self):
          self.__salary=50000

     def salary(self):
          return self.__salary
     
print("-----------")
obj=private()     
print(obj.salary())





