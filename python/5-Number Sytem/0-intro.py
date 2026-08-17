#Number system

#we all fetch the digit in the numbe
 
num=123

while num>0:
    print(num%10)

    num=num//10

# print the all digit sum in number
print("sum")
num=2354
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10

print(sum)

# Reverse the given num

n=int(input("enter the number:"))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
