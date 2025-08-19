# tuple are immutable datatypes
# change memory location

sub=('eng','hindi','maths','gk')
sub=('pol sci','his' , 'geo',15,True,3.45)
print(sub)
# print(sub[1])

# checking data types
print(type(sub[-1]))
print(type(sub[-2]))
print(type(sub[-3]))
print(type(sub[-4]))


# tuple method

# count method

numbers = (1,2,4,5,6,1,1,4,3,6)
count_2=numbers.count(2)
print(count_2)

# count_1=numbers.count(6)
# print(count_1)

print(numbers.count(6))


# index method
 
fruits=('mango','apple','banana','cherry','orange','mango')
index_banana = fruits.index("banana")
print(index_banana)

index_mango = fruits.index("mango",)
print(index_mango)

index_mango = fruits.index("mango",1)
print(index_mango)




