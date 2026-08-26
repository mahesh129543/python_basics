# num=int(input("enter the nm:"))
# cnt=0
# for i in range(1,num+1):
#     if num%i==0:
#         cnt=cnt+1
# if cnt==2:
#     print("prime")
# else:
#     print("not prime")

    

# num=int(input("enter the nm:"))
# cnt=0
# for i in range(2,num//2):
#     if num%i==0:
#         cnt=cnt+1
# if cnt>0:
#     print(" not prime")
# else:
#     print("prime")



num1=int(input("enter thenum:"))
num2=int(input("enter the num2:"))

if(num1==0):
    print("invalid")


if num1<0:
    sign=-1
elif num2<0:
    sign=-1
else:
    sign=1

a=abs(num1)
b=abs(num2)

cnt=0

while a>=b:
    a=a-b
    cnt=cnt+1

print(sign*cnt)

    

