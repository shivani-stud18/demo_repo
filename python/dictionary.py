
abc={"name":"John",
     "class":"12th",
     "age":"25"
     }
for i in abc:
    print(abc[i])
    print(i)
# print(abc["age"])
# print(abc["class"])
# print(abc["name"])


# methods in dict


# item method
dict= {"first":"james",
   "second":"jake",
   "third":"jay"
   }

for i,v in dict.items():  
    print(i)    



# key method
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}

keys=car.keys()
print(keys)

keys_list =list(car.keys())
print(keys_list)

for i in car.keys():
    print(i)


# value method
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


values=person.values()
print(values)

values_list =list(person.values())
print(values_list)

for v in person.values():
    print(v)


# pop method 

student = {
    "name": "Alice",
    "age": 22,
    "course": "Math"
}

d = student.pop("name")
print(d)          
print(student)




