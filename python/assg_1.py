# name=input('type ur name here')
# age=input('type ur age here')
# print(f'my name is {name} I am {age} years old' )



name_1=input('type ur name')
age_1=input('type ur age')
print("my name is " + name_1 + " I am "+ age_1 + " years old")

name_2=input('type ur name')
age_2=input('type ur age')

print("my name is " + name_2  + " and I am " + age_2 + " years old")


if(age_1<age_2):   
    print(f" {name_1} is younger than {name_2}")  
elif age_1==age_2:
    print (f" {name_1} and {name_2} are same age")  
else:
    print(f" {name_1} is older than {name_2}")
