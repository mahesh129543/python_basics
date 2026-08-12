# # Q11) Print the greatest of 3 nos given by user.


# a = int(input("Enter  number1: "))
# b = int(input("Enter number2: "))
# c = int(input("Enter number3: "))

# if a >= b and a >= c:
#     print("Greatest =", a)
# elif b >= a and b >= c:
#     print("Greatest =", b)
# else:
#     print("Greatest =", c)




# # Q12) Print the smallest of 3 nos given by user.(using nest conditionals(nested if-else))
# a = int(input("Enter  number1: "))
# b = int(input("Enter number2: "))
# c = int(input("Enter number3: "))

# if a < b:
#     if a < c:
#         print("Smallest =", a)
#     else:
#         print("Smallest =", c)
# else:
#     if b < c:
#         print("Smallest =", b)
#     else:
#         print("Smallest =", c)

# # Q13) Check the temprature given by user is for which season
# #      (spring(15-30 °C), summer(30+ °C), autumn(0-10 °C), and winter( 10–15 °C))

# temp = float(input("Enter temperature in  C: "))

# if temp > 30:
#     print("Summer")
# elif temp >= 15 and temp <= 30:
#     print("Spring")
# elif temp > 10 and temp < 15:
#     print("Winter")
# elif temp >= 0 and temp <= 10:
#     print("Autumn")
# else:
#     print("Temperature is outside the given range")

# # Q14) Wap to Take values of length and breadth of a rectangle from user and check if it is square or not.
# length = float(input("Enter length: "))
# breadth = float(input("Enter breadth: "))

# if length == breadth:
#     print("It is a Square")
# else:
#     print("It is not a Square")

# # Q15) Alice is trying to find a no which is non negative and even and divisible by 3 given by Alice .

# num = int(input("Enter a number: "))

# if (num >= 0 and num % 2 == 0 and num % 3 == 0):
#     print("Number satisfies all conditions")
# else:
#     print("Number does not satisfy all conditions")




# Q16) Write a program to print Yes if no which is odd and between 10 to 15 and divisible by 4 given by user





# num = int(input("Enter a number: "))

# if num % 2 != 0 and num >= 10 and num <= 15 and num % 4 == 0:
#     print("Yes")
# else:
#     print("No")

# # Q17) Write a program to check the input nos. given by Jeff and Bob are same or not for same "Won" else "Lost"


# jeff = int(input("Enter Jeff's number: "))
# bob = int(input("Enter Bob's number: "))

# if jeff == bob:
#     print("Won")
# else:
#     print("Lost")


# # Q18) Create a program using nested if-else where the player chooses between "tea" or "coffee," 
# #      and then chooses "hot" or "cold" to get a final drink suggestion.
# drink = input("Choose tea or coffee: ")
# temperature = input("Choose hot or cold: ")

# if drink == "tea":
#     if temperature == "hot":
#         print("Hot Tea")
#     else:
#         print("Cold Tea")
# else:
#     if temperature == "hot":
#         print("Hot Coffee")
#     else:
#         print("Cold Coffee")
# # Q19)A student needs to know if they passed their exam. Write a program that checks their score and prints "Pass" if it is 40 or more, otherwise "Fail."
# score = int(input("Enter your score: "))

# if score >= 40:
#     print("Pass")
# else:
#     print("Fail")
# # Q20) Write a Python program that takes the user's age and income as input and determines if they 
# #      qualify for a loan based on these rules:

# #    If the age is less than 18, print "Not eligible for a loan."
# #    If the age is between 18 and 60:
# #    If the income is less than 20,000, print "Eligible for a basic loan."
# #    If the income is between 20,000 and 50,000, print "Eligible for a standard loan."
# #    If the income is above 50,000, print "Eligible for a premium loan."
# #    If the age is above 60:
# #    If the income is less than 30,000, print "Eligible for a senior citizen basic loan."
# #    If the income is 30,000 or more, print "Eligible for a senior citizen premium loan."


# age = int(input("Enter your age: "))
# income = int(input("Enter your income: "))

# if age < 18:
#     print("Not eligible for a loan.")

# elif age <= 60:
#     if income < 20000:
#         print("Eligible for a basic loan.")
#     elif income <= 50000:
#         print("Eligible for a standard loan.")
#     else:
#         print("Eligible for a premium loan.")

# else:
#     if income < 30000:
#         print("Eligible for a senior citizen basic loan.")
#     else:
#         print("Eligible for a senior citizen premium loan.")





# a=int (input("enter num:"))

# if a>100 and a<200:
#     total=a-((a*10)/100)
#     print(total)

# elif a>=200:
#     total=a-((a*20)/100)
#     print(total)

# else:
#     print("no discount",a)



# age=int(input("enter age:"))

# if(age<=12):
#     print("price is 10")

# elif(age>12 and age<40):
#     print("price is 15")

# else:
#     print("price is 12")


# temp=int(input("temperature:"))
# hum=int(input("enter humidity:"))

# if(temp>30 and hum<40):
#     print("water need")
# else:
#     print("not need")



# amount=int(input("enter the amount:"))
# y=int(input("enter the year:"))
# if(y<=5):
#     total=amount+(amount*5)/100
#     print(total)

# elif(y>5 and y<=10):
#     total=amount+(amount*10)/100
#     print(total)
# else:
#     total=amount+(amount*20)/100
#     print(total)

# 7. A travel agency offers discounts on train tickets: 5% for students, 10% for senior citizens, and no discount otherwise. Write a program to calculate the final ticket price.  


age=int(input("enter the age:"))
price=250
if(age<=18):
    total=price-(price*5)/100
    print(total)
elif(age>40 and age<=80):
    total=price-(price*10)/100
    print(total)
else:
    total=price
    print(total)


    # 8. A food delivery app charges $5 for delivery. If the order amount is above $50, delivery is free. Write a program to calculate the total cost.  


amount=int(input("enter the amount:"))
if(amount>50):
    total=amount
    print(total)
else:
    total=amount+5
    print(total)


    # 9. Write a program to check if a year is a leap year. A year is a leap year if it is divisible by 4 but not divisible by 100, except if it is divisible by 400.  

year=int(input("enter the year:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("leap year")
else:
    print("not leap year")


# 10. A car rental service charges $20 per day. If the customer rents for more than 7 days, they get a $50 discount. Write a program to calculate the total rental cost.  


days=int(input("enter the days:"))
if(days>7):
    total=(days*20)-50
    print(total)
else:
    total=days*20
    print(total)


# 11. A gym offers membership discounts: 10% for students, 15% for teachers, and no discount otherwise. Write a program to calculate the membership fee.

age=int(input("enter the age:"))
occu=input("enter the name:")
price=500
if(age<=18 and occu=="student"):
    total=price-(price*10)/100
    print(total)
elif(age>18 and occu=="teacher"):
    total=price-(price*15)/100
    print(total)
else:
    total=price
    print(total)


#trianle check

a=int(input("enter the l1:"))
b=int(input("enter the l2:"))
c=int(input("enter the l3:"))
if(a==b and b==c):
    print("equilateral triangle")
elif(a==b or b==c or a==c):
    print("isosceles triale")
else:
    print("scalene triangle")