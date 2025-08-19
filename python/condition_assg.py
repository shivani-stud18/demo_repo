# 1st assignment
output=''
score=int(input("type ur score here!"))
print(score)

output='high!' if score>=85 else 'low!' 
print(output)

if score>=90:
    output="Excellent!"
elif score>=70:
    output="Good!"
else:
    output="Needs Improvement!"   

# 2nd assignment

status  = "false"
flag="1" if status=="true" else "0"
print(flag)

# 3rd assignment
marks=int(input("type your marks here!")) 
 
if marks>=90:
    print("You got Grade A")
elif marks>=80:
    print("You got Grade B")    
elif marks>=70:
    print("You got Grade C")
elif marks>=60:
    print("You got Grade D")
else:
    print("You are Fail")            
   
# 4th assignment

age=int(input("How old are you?"))
print(age)

if age<13:
    print("You are a kid")
elif age>=13 and age<20:
    print("You are a teenager")
elif age>=20 and age<=60:
    print("You are an adult")
elif age>=60 and age<=100:
    print("You are a senior")
else:
    print("Invalid!")    

# 5th assignment
number =int(input("type any odd or even number here!"))
if number%2==0:
    print("You typed an even number")
else:
    print("You typed an odd number")

# 6th assignment
logged_in=input("Enter True or False")
if logged_in=="true":
    print("Welcome Back!")
else:
    print("Please login first")