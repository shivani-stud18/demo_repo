# open file

# f = open('demotext.txt')
# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# use of for loop

# with open("demofile.txt") as f:
#   for x in f:
#     print(x)


# through with statement

# with open("demotext.txt") as f:
#     print(f.read())

# close statement

# f = open("demotext.txt")
# print(f.read())
# f.close() 


# append method 
# with open("demotext.txt", "a") as f:
#   f.write("Now the file has more content!")

# with open("demotext.txt") as f:
#   print(f.read())
 

# write method 

# with open("demotext.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# with open("demotext.txt") as f:
#   print(f.read())

# create file method

# f = open("myfile.txt", "x")
# f=open("myfile.txt")
# print(f.read())

# create folder method
# import os
# os.mkdir("myfolder")  

# delete file method
# import os
# os.remove("myfile.txt")

# Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


# delete folder method
# import os
# os.rmdir("myfolder")


