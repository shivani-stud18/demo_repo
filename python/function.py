#function with default value
# def cal_per():
#     marks=100
#     per=marks/200*100
#     print(per)
# cal_per()    

# function with parameters
# def cal_per(marks,total):
#     marks=100
#     per=marks/total*100
#     print(per)
# cal_per(100,200)   

# function default para
# def cal_per(marks,total=500):
#     marks=100
#     per=marks/total*100
#     print(per)
# cal_per(100)    

# function keyword para
# def cal_per(stud_name, sur_name="rana", mid_name=""):
#        full=stud_name + " " +mid_name + " " + sur_name
#        print(full)
# cal_per("Suresh", mid_name="kumar")  

# function (return)
def cal_per(stud_name,sur_name):
       full=stud_name +" " + sur_name
       return full

full=cal_per("suresh" , "kumar")
print(full)

def cal(x,y):
       z=x+y
       return z   
z= cal(20,30)
print(z)      