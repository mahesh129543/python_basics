num=153
temp=num

sum=0
while num>0:
    rem=num%10
    sum=sum+rem*rem*rem
    num =num//10
if temp==sum:
    print("153 is amstromng num")

else:
    print("not amstrong")
