# if elif else statement

'''
syntax: 

if condition:
    statement1
    statement2
    statement3
    statement4
elif condition:
    statement1
    statement2
    statement3
    statement4
else:
    statement1
    statement2
    statement3
    statement4

'''

#example

a=12
b=23    

if b>a:
    print("a is greater than b")
elif b==a:
    print("a is equal to b")
else:
    print("b is greater than a")

#example2

age=12

if age<18:
    print("young person")
elif age>=18 and age<35:
    print("adult")
else:
    print("old person")



mark=int(input("enter the mark:"))

if mark>=80:
    print("first class")
elif mark>=60 and mark<80:
    print("second class")
elif mark>=40 and mark<60:
    print("third class")
else:
    print("fail")


num1=int(input("enter the number:"))
num2=int(input("enter the number:"))

if(a>b):
    print("a is greater than b")
elif(a==b):
    print("a is equal to b")
else:
    print("b is greater than a")


numm1=int(input("enter the number:"))
numm2=int(input("enter the number:"))
numm3=int(input("enter the number:"))

if(numm1>numm2 and numm1>numm3):
    print("numm1 is greater")
elif(numm2>numm1 and numm2>numm3):
    print("numm2 is greater")
else:
    print("numm3 is greater")



if (numm1<numm2 and numm1<numm3):
    print("numm1 is smaller")
elif(numm2<numm1 and numm2<numm3):
    print("numm2 is smaller")
else:
    print("numm3 is smaller")

