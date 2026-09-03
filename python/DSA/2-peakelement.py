nums = [1,2,1,3,5,6,4]

i=1
while i<len(nums)-1:
    if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
        print(i)
    i=i+1


n =[2,7,11,15]
t = 9


i=0
j=len(n)-1

while i<j:
    sum=n[i]+n[j]
    if sum==t:
        print(i,j)
        break
    elif sum<t:
        i=i+1
    else:
        j=j-1


