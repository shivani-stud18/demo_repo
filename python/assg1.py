# 1 assignment
class animal():
    def speak(self):
        print("Animal speak")

class dog(animal):
    def speak(self):
        super().speak()
        print("Dog barks!")

pet=dog()   
pet.speak() 

# 2 assignment
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

class student(person):
    def __init__(self,name,age,student_id):
        self.student_id=student_id
        super().__init__(name,age)

Stu=student("My name is Anny"," My age is 20","My  id is 1234.")

print(Stu.name)
print(Stu.age)
print(Stu.student_id)


# 3 assignment
class account():
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
        
    def display (self):
            print(f"account holder: {self.account_holder}")
            print(f"balance: {self.balance}")

class SavingsAccount(account):
    def __init__(self,account_holder,balance,interest_rate):
        super().__init__(account_holder,balance)
        self.interest_rate=interest_rate
        
    def display(self):
        super().display()
        print(f"interest rate: {self.interest_rate}%")

balance = SavingsAccount("John", 2345, 2.6)
balance.display()











     
        





