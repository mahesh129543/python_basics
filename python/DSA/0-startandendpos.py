


#using log(n) time complexity 
def search(arr,target):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1
arr1=[2,4,5,8,9]
target=8

print(search(arr1,target))