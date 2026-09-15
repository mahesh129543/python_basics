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


l=[1,2,3,4,5,6,7]
l1=[]

for i in l:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt=cnt+1


    if cnt==2:
        l1.append(i)
print(l1)

l=["coddnera","jay","kiran","at"]
max=0
for i in range(len(l)):

    if (len(l[i]))>max:
        max=len(l[i])
        print(max)
for i in range(len(l)):
    if len(l[i])==max:
        print(l[i])



l=[1,"2#",3,"4#"]
l1=[]

for i in range(len(l)):
    if type(l[i])==str:
        l1.append(int(l[i][0])*2)
    else:
        l1.append(l[i])
print(l1)



    
       
    
