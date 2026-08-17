#Amstrong num

# defination: a number that is the sum of its own digits each raised to the power of the number of digits
# example: 153=1*1*1+5*5*5+3*3*3

num=int(input("enter the num:"))

sum=0
while num>0:
    rem=num%10
    amg=rem*rem*rem
    sum=sum+amg
    num=num//10

print(sum)

if sum==num:
    print("amstrong")
else:
    print("not amstrong")


# finding the num nt he number

num=int(input("enter the num:"))

even=0
odd=0

while num>0:
    rem=num%10

    if rem%2==0:
        even=even+1
    else:
        odd=odd+1

    num=num//10

print(f"even count is {even} and odd count is {odd}")
