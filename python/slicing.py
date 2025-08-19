#list slicing syntax
# list_name[start : end : step]
# list_name[start:end]
# list_name[start:]
# list_name[:end]
# list_name[:]
# list_name[start::step]
# list_name[::step]


#example

a=[1,2,3,4,5,6,7,9]
# print(a[1:4])       #1 is starting point and 4 is ending
# print(a[1::5])      #1 is starting point and 5 is step size 
# print(a[:3])        #3 is ending point
# print(a[3:])         #3 is starting point
print(a[1:9:2])        #1 is starting, 9 is ending and 2 is step size
print(a[::2])          #2 is step size


s=[2,3,5,7,9,4,5,6,8,3] 
print(a[-2:])        #2 is ending point from last 
print(a[:-2])        #2 is starting point from last
print(a[::-1])       #1 is step size from last

