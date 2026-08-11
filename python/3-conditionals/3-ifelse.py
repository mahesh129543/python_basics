#if else statement 

'''
syntax: 

if condition:
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
else:
    print("b is greater than a")


num=int(input("enter the number:"))

if(num%2==0):
    print("the number is even")
else:
    print("the number is not even")

num1=int(input("enter the number:"))
if(num1%2!=0):
    print("the number is odd")
else:
    print("the number is not odd")


num3=int(input("enter the number:"))
if(num3%5==0):
    print("the number is divisible by 5")
else:
    print("the number is not divisible by 5")


#voting problem

age=int(input("enter your age:"))
if(age>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")


