# house rob problem

def rob(nums):
    total=0
    n=len(nums)
    if n==1:
        return nums[0]
    k=0
    j=len(nums)-1
    while k<=j:
        i=k
        sum=0
        while i<=j:
            sum=sum+nums[i]
            i=i+2

        if sum>total:
            total=sum
        k=k+1
    return total

print(rob([2,7,9,3,1]))


for i in range(3):
    print(i)
else:
    print("end")

for i in range(3,0,-1):
    print(i,end=" ")

for i in 'abc':
    print(i)

   

  