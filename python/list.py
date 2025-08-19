# list are mutable datatype (mutable means change)
# change data

sub=['eng','hindi','maths',13]
print(sub[2],sub[1] +" " + sub[0] ,sub[3])

# add
sub.append('science')
print(sub)

# insert
sub.insert(1,'history')
print(sub)

# delete
fruits=['apple','mango','orange']
print(fruits)
del fruits[2]
print(fruits)


# how to check length
num=[0,12,33,4]
print(num [-2])
length=len(num)
print(length)

# modify /updating
num[2]=29
print(num)

# how to concatenate two list in python

# 1. using extend method
sub_1=['eng','hindi','maths',]
num.append(sub_1)
print(num)

a=['a','b','c','d']
b=['e','f','g','h','i']
a.extend(b)
print(a)


# 2. using + operator
list_1=[1,2,3,4]
list_2=[5,6,7,8,]
result=list_1+list_2
print(result)

# iterating over lists

# using for loop
a=['apple','mango','banana','orange','grapes']
for i in a:
    print(i)



a=['red','green','yellow']
print(a)
print(a[1])