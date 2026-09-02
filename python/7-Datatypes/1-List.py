# list data type
# list is the sequence data type
#defination: a list is a collection of items in a particular order.
#list is mutable.   
#features:
#1. ordered
#2. duplicate
#3. mutable
# useing the squre brackets
# both type of the data homogeneous and also the heterogeneous

# syntax: list1=[value1,value2,value3]
# one important that do not use the list name is list it is a reserved word

list1=[12,23,34,45,56] # homogeneous data
print(list1)

l1=["mahesh",22,"pune"]#heterogeneous data
print(l1)

l1=["mahesh",22,"pune",12,23,34,45,56]
print(l1)

# list with duplicate value it print the all data a its index
l1=["mahesh",22,"pune",12,23,34,45,34,12]
print(l1)

# list constructor using two parenthesis 
l1=list((12,23,34,45,56))
print(l1)
# both are same

# empty list 
l1=[]
print(l1)


# indexing of the list
# positive indexing  always star from zero 
l1=[11,22,33,44,55,66]
'''
index element
0   11
1   22
2   33
3   44
4   55
5   66

using the index we can fetch the any element in the list also we can do more operation 
beacause the list is the mutable data type and sequence data type
'''
#data_type_name[index]

print(l1[2])
print(l1[3])

# slicing of the list
'''
start:end:step

slicing means the fetching the perticular range data with steps and without steps also



'''
print(l1[0:5:2])
print(l1[0:5])
print(l1[:5])
print(l1[2:])
print(l1[:])

# neagtive indexing 
#it will start with the -1
l1=[11,22,33,44,55,66]
'''
index element
-1     66
-2     55
-3     44
-4     33
-5     22
-6     11

'''
print(l1[-1])
print(l1[-1: -7:-1])

print(l1[::-1])
print(l1[-1: :-1])


print(" more examples:")

list1=[12,23,34,45,56,"mahesh","narke",12.45,True]
print(list1[::-1])
print(list1[1])
print(list1[-2])
print(list1[0:4])
print(list1[:4])
print(list1[2:])
print(list1[:])
print(list1[6])
print(list1[::2])
'''
[True, 12.45, 'narke', 'mahesh', 56, 45, 34, 23, 12]
23
12.45
[12, 23, 34, 45]
[12, 23, 34, 45]
[34, 45, 56, 'mahesh', 'narke', 12.45, True]
[12, 23, 34, 45, 56, 'mahesh', 'narke', 12.45, True]
narke
'''


# l=[7,6,4,5,3,2,1]

l=[7,6,4,5,3,2,1]

# # o/p : 5 using positive indexing
print(l[3])

# # o/p : 5 using negative indexing
print(l[-4])

# # o/p : [4,5,3] using positive slicing
print(l[2:5])

# # o/p : [4,5,3] using negative slicing
print(l[-3:-6:-1])

# # o/p : [1,2,3,5,4,6,7]
print(l[::-1])

# # o/p: [7,4,3,1]
print(l[::2])

# # o/p: [1,3,4,7]
print(l[::-2])

l2=[2,3,4,5,6,7,8]
print(l2[-3:])

# # List Slicing: Given the list numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 
l3=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # write a Python program to extract the middle 4 elements using slicing.
print(l3[3:7])
# # fruits = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"], 
fruits = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
# # write a program to extract every alternate element from the list.
print(fruits[::2])


#mutable data type
#modification in the list

print("mutable list or list modification example")

list1=[12,23,34,45,56,"mahesh","narke",12.45,True]
print(list1)
list1[0]=100
print(list1)
list1[1:4]=["jay","rohit","virat"]
print(list1)
list1.append("dhoni")
print(list1)

lt=[1,2,3,4,5,6]
lt[1]=["mahi","rai"]
print(lt)


# inbuid method in the list
#1. append()

list1=[12,23,34,45,56,"mahesh","narke",12.45,True]
list1.append("dhoni")
print(list1)
'''
we can not add more element at one time
but we can add more list at one time
'''
list1.append([1,2,3,4])
print(list1)

#2. extend()
'''
we can add more element at one time
'''

list1=[11,22,33,44,55]
list1.extend([1,2,3,4])
print(list1)

#3. insert()
'''
it is use to add the element to the exact position and all eleent is shifted
next to the element
sytax: list.insert(index,value)
it have to parameter the use of the index and value
'''
list1=[11,22,33,44,55]
list1.insert(2,"jay")
print(list1)

# Deletion methods
# 1. remove()
'''
it is use to remove the element from the list but
the first occurance of the element is removed

sytax: list.remove(value)
use: to remove the element from the list
'''
list1=[11,22,33,44,55]
list1.remove(22)
print(list1)


# 2. pop()
'''
pop() is use to delete the element on the list
using the index we need to give the perticular index to the 
parameter
it working on the specific index wise

list1.pop()=> it will remove or delete the last element 

sytax: list.pop(index)

'''
list1=[11,22,33,44,55]
list1.pop(2)
list1.pop()
print(list1)

# remove 3 in the list

l1=[1,1,3,4,5,6,7,3,3,5]
l2=[]

for i in l1:
    if i!=3:
        l2.append(i)
    
    
print(l1)
print(l2)



# 3. clear()
'''
it is use to clear the list it will remove all the element from the list

syntax: list.clear()
it will give the empty list => []
'''
list1=[11,22,33,44,55]
list1.clear()
print(list1)



#del 
'''
it is use to delete the list it will give the error
it will delete permenantly the list
'''
list6=[11,22,33,44,55]
del list6[2]
print(list6)

# use also indexing and slicing
list6=[11,22,33,44,55]
del list6[2: ]
print(list6)

list6=[11,22,33,44,55,66,77,88]
del list6[: :2 ]
print(list6)


# Write a program to count the elements in a list.

l1=[1,2,3,4,5,6,7,8,9]
cnt=0
for i in l1:
    cnt=cnt+1
print(cnt)

# Write a program to sum of elements in a list.

l1=[1,2,3,4,5,6,7,8,9]
sum=0
for i in l1:
    sum=sum+i
print(sum)

# WAP to remove all the negative elements from lits.

l1=[-1,2,-3,4,-5,6,-7,8]
l2=[]
for i in l1:
    if i>0:
        l2.append(i)
print(l2)

# WAP to remove the duplicates element from the list
l1=[2,3,4,3,4,5,3,2]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

#  list1=[2,3,3,4,6]

#  output: [2,3,4,6]

# we need remove all the 7 from list:[1,2,3,4,5,7]
l1=[1,2,4,6,7,5,7,7]

l2=[]
for i in l1:
    if i!=7:
        l2.append(i)
print(l2)




# write a program to print the square of all list items:[1,2,3,4]
l1=[1,2,3,4]
l2=[]
for i in l1:
    l2.append(i*i)
print(l2)

# Add single element at the end of the list.
l1=[12,3,4,5,6]
l1.append(7)
print(l1)

# Add multiple elements at the end of the list.

l1=[12,3,4,5,6]
l1.extend([7,8,9])
print(l1)



# count() method
'''

it is use to count the element in the list

sytax: list.count(value)

value is the element which we need to count it is mendetory
other wise it will give the error
if in list there is the multiple same values that time we need
to count tht time we use the count method it give exact count of the element


'''

l1=[12,3,4,5,6]
print(l1.count(3))

l2=[12,3,4,5,3,4,3,4,5,6]
print(l2.count(3))

#index() method
'''

it is use to find the index of the element in the list

sytax: list.index(value)

value is the element which we need to find the index it is mendetory
other wise it will give the error

also it give the first occurance index of the element
'''

l1=[12,3,4,5,6]
print(l1.index(3))

l2=[12,3,4,5,3,4,3,4,5,6]
print(l2.index(3))



# reverse() method
'''

it is use to reverse the list

sytax: list.reverse()

'''

l1=[12,3,4,5,6]
l1.reverse()
print(l1)

# reverse the list without using  the reverse method

l1=[12,3,4,5,6]
l2=l1[::-1]
print(l2)

l1=[1,2,3,4,4,5,6,7]
l2=[]
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
print(l2)

l1=[1,2,3,4,5]

print(len(l1))

i=0 
j=len(l1)-1
while i<j:
    temp=l1[i]
    l1[i]=l1[j]
    l1[j]=temp
    i=i+1
    j=j-1
print(l1)


# sort() method

'''

it is use to sort the list

sytax: list.sort()

'''

l1=[12,3,4,5,6]
l1.sort()
print(l1)# it will give the acsending order

l1=[12,3,4,5,6]
l1.sort()
l1.reverse()
print(l1)# it will give the decending order

# sort list without using the inbuid method

l1=[4,5,3,2,7,8,9]

for i in range(len(l1)-1):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
print(l1)

# you have to print the palindrome element from the list
l1=[121,456,131,678,454,234]
res=[]
for i in l1:
    temp=i
    rev=0
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if rev==i:
        res.append(i)
print(res)


# concat of teh multiple lists:
'''
using the plus operator we will be performing the concatination of 
the lists
'''

l1=[1,2,3,4]
l2=[5,6,7,8]
l3=l1+l2
print(l3)

# product of the list
'''one list print that time of the multiply'''
l1=[1,2,3,4]

l3=l1*2
print(l3)


l1=[23,4,5,34,5,6,23]
print(min(l1))

l1=[23,4,5,34,5,6,23]
print(max(l1))




# max without using the inbuid method

l1=[23,4,5,34,5,6,23]
max=l1[0]
for i in l1:
    if i>max:
        max=i
print(max)

#min

l1=[23,4,5,34,5,6,23]
min=l1[0]
for i in l1:
    if i<min:
        min=i
print(min)

#second max
l1=[12,34,23,45,62,21]

max=l1[0]
for i in l1:
    if i>max:
        max=i
print(max)

secmax=l1[0]
for i in l1:
    if i>secmax and i<max:
        secmax=i
print(secmax)


l1=[12,32,434,54,65,76,54,34]

maxele=0
secmax=0

for i in l1:
    if i>maxele:
        secmax=maxele
        maxele=i
    elif i>secmax and i!=maxele:
        secmax=i

print(secmax)


l1=[12,32,434,54,65,76,54,34]

minele=l1[0]
secmin=float('inf')

for i in l1:
    if i<minele:
        secmin=minele
        minele=i
    elif i<secmin and i!=minele:
        secmin=i

print(secmin)



#deep copy and the shallow copy



l1=[1,2,3,4,5]#deep copy it bellong to same same memory location

l2=l1
print(l2)
l2.append(6)
print(l2)
print(l1)
print(id(l1))
print(id(l2))


l1=[1,2,3,4,5]#shallow copy it create the new memory address list
l2=l1.copy()
print(l2)
l2.append(6)
print(l2)
print(id(l1))
print(id(l2))



# WAP to find the avg of all the items from the list

l1=[2,4,6,8,7,9,5]

sum=0
for i in l1:
    sum+=i
avg=sum/len(l1)
print(avg)

# WAP to print the sum of all the even items in a list.
l1=[2,4,6,8,7,9,5]

sum=0
for i in l1:
    if i%2==0:
        sum+=i
print(sum)

# WAP to print the sum of all the odd items in a list.

l1=[2,4,6,8,7,9,5]

sum=0
for i in l1:
    if i%2!=0:
        sum+=i
print(sum)

# wap 2nd max element in a list.
l1=[2,4,6,8,7,9,5]

maxele=0
secmax=0

for i in l1:
    if i>maxele:
        secmax=maxele
        maxele=i
    elif i>secmax and i!=maxele:
        secmax=i

print("second max",secmax)

# wap 3rd min element in a list.
l1 = [2, 4, 6, 8, 7, 9, 5]

minele = l1[0]
secmin = float('inf')
thirdmin = float('inf')

for i in l1:

    if i < minele:
        thirdmin = secmin
        secmin = minele
        minele = i

    elif i < secmin and i != minele:
        thirdmin = secmin
        secmin = i

    elif i < thirdmin and i != secmin and i != minele:
        thirdmin = i

print("third min", thirdmin)

# 21. seprate the even and odd items from the list in different list 

list1=[10,10,20,30,5,3,9] 

even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

# 22. all the even itmes shoud be in left side and odd items should be in right side. 

list2=[1,2,3,4,5,6,7]

even=[]
odd=[]

for i in list2:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even+odd)

# 23. all the zeros (0) should be in left side of the list and 1 should be in roght side. 

list2=[1,0,1,0,0,1,1]

zero=[]
one=[]

for i in list2:
    if i==0:
        zero.append(i)
    else:
        one.append(i)

print(zero+one)





l1=[2,4,7,86,4,5,56,78,3]
l2=[]

for i in l1:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        l2.append(i)
print(l2)




