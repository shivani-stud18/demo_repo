# polymorphism means "many forms".It refers to the ability of an entity (like a function or object) to perform different actions based on the context.
# In Python, we can achieve polymorphism using functions, classes, and objects. Here are some examples: 

# Polymorphism in Built-in Functions
     
# Polymorphic len() function
print(len("Programiz"))
print("-------------")
print(len([1, 2, 3, 4]))
print("-------------")
print(len(["Python", "Java", "C"]))
print("-------------")
print(len({"Name": "John", "Address": "Nepal"}))
print("-------------")
print(max(1,2,4,6,9,8))
print("-------------")
print(max("a","z","b","y"))


# Polymorphism in Functions

class pen:
    def use (self):
        return "Writing"

class eraser:
    def use(self):
        return "Erasing"
    
def perform_tool(tool):
    print(tool.use())

perform_tool(pen())    
perform_tool(eraser())

# Polymorphism in addition Operators
num1=2
num2=3
print(num1+num2)
print("----------")
print(5+10)
print("----------")
print("Hello" + " World ")
print("----------")
print([1,2] + [3,4])

# Polymorphism in Class Methods
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def sound(self):
        print("Meow")


class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def sound(self):
        print("Bark")

cat1=cat("kitty",3)
dog1=dog("Fluffy",2.5)    

for animal in (cat1,dog1):
    animal.sound()
    animal.info()
    animal.sound()
