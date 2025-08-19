# assignment 1
class Student():
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade


    def display_info( self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Grade:",self.grade)

student1=Student("Jake",17,"12th")
student2=Student("Anny",18,"12th")

student1.display_info()
print("--------")
student2.display_info()
print("--------")

# assignment 2

class Animal():
    def make_sound(self):
        print("Some sound")

class Dog():
    def make_sound(self ):
        print("Bark")

animal=Animal()
animal.make_sound()
print("--------")
dog=Dog()
dog.make_sound()








       


