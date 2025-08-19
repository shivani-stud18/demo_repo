stud_name=input('type your name ')
print(stud_name)   

# try:
#     num=int(input('type any number '))
#     print(num*3)
# except : 
#     print('invalid input')    

try:
    num=int(input('type any number '))
    print(num*3)
except Exception as a: 
    # print(a)  
    print(f'hey you got this error {a}')      