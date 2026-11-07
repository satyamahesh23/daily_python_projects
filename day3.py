#checking password like 12 characters Aa*1
# list1=["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%*&"]   
# pass1=""    
# password=input("enter the password: ")
# if pass1=="":
#    A= list1.append(pass1)
# print("successfully created and strong password",A)
# import random
# char =["!@#$%^&*abcdefghijklmnopqrstuvwxyz12345678910"]
# A=input("enter the password : ")
# password=""
# if A<=12:
#         print("incorrect password atleast 12 characters are required")
# else:
#         password+=random.choice(char)
#         print("strong password created",password)


password=input("enter the password :")
if len(password)!=12:
        print("error altest 12 character must be ")
elif len(password)==12:

        print("successfully password is created")
else:
        print("valid password")
    
         