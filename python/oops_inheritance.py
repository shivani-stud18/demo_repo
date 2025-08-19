class animal:
    name=""
    age=0
    
    def eat(self):    #eat is a super class
      print('I can eat') 

class dog(animal):
    def display(self):     #display is a sub class 
        print("My name is ",self.name ,'\n' "I am ",self.age," years old") 

labrador=dog()          # creating an object of the class dog
labrador.name='Rex'
labrador.age=5
labrador.eat()           # eat() is a method of animal class 
labrador.display()       # display () is a method of dog class and it is called using object of dog class 



# overriding method     
# In Python, overriding refers to the process of redefining a method or attribute in a subclass that is already defined in its superclass. This allows the subclass to provide a specific implementation for a method or attribute that is different from the one provided by the superclass.



def eat():
    print("I can eat") 

class dog(animal):
    def eat(self):
        print("I like to eat bones!")

labrador = dog() 
labrador.eat()        



# super() function in python
# The super() function is used to give access to methods and properties of a parent or sibling class, which is used in inheritance. It is used to invoke methods of a superclass from a subclass. 

 
class pet():
    name=""

    def eat(self):
        print("I can eat")

class dog(pet):

    def eat(self):
        super().eat()
        print("I like too eat bones!")

jake=dog()
jake.eat()

