


a=int (input("enter num:"))

if a>100 and a<200:
    total=a-((a*10)/100)
    print(total)

elif a>=200:
    total=a-((a*20)/100)
    print(total)

else:
    print("no discount",a)



age=int(input("enter age:"))

if(age<=12):
    print("price is 10")

elif(age>12 and age<40):
    print("price is 15")

else:
    print("price is 12")


temp=int(input("temperature:"))
hum=int(input("enter humidity:"))

if(temp>30 and hum<40):
    print("water need")
else:
    print("not need")
