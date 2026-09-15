#tupple:
# definations:
# A tuple is an immutable sequence of Python objects. Tuples are sequences, just like lists. 
# The difference between the two is that tuples cannot be changed once created.
# tuples are written as comma-separated values between parentheses.
# syntax: tup=(value1,value2,value3)

#what type of data tuple contain:heterogeneous data
#and homogeneous data and ordered

tup=(12,23,34,45,56)
print(tup)
print(type(tup))
print(len(tup))

tup1=("mahesh",22,"pune")
print(tup1)

tup2=("mahesh",22,"pune",12,23,34,45,56)
print(tup2)


# Indexing and slicing:

t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# output:(30, 40, 50, 60)

print(t[2:6])


# output:(10, 20, 30, 40)

print(t[:4])

# output:(60, 70, 80, 90, 100)

print(t[5:])

# output:(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print(t[:])

# output:(10,30,50,70,90)

print(t[::2])

# output:(100, 90, 80, 70, 60, 50, 40, 30, 20, 10)

print(t[::-1])

# output:(100, 80, 60, 40, 20)

print(t[9:1:-2])

# output:(90,100) By negative slicing

print(t[-2:])

t1=(1,2,3,4,5,6,7,8,9,10)
# all odd
print(t1[::2])

# all even
print(t1[1::2])


# nested sclicing 

l1=[[1,2,3],[4,5,6]]
print(l1[1][1])
print(l1[0][0])


l1=[1,2,3,7,[4,5,6,"jay"]]
print(l1[4])
print(l1[4][1])
print(l1[4][3])

l1=l1=[1,2,3,7,[4,5,6,"jay"],[1,2,3,"jiya"]]
print(l1[5][3])

l1=[[10,20,30],[40,50,60],[70,80,90]]
print(l1[0][0])
print(l1[1][1])
print(l1[2][1])

print(l1[1])
print(l1[2]) 

l=[1,2,3,[6,"bill",6,7],5,[1,2,"gate"],"jet"]

print(l[3][1],l[5][2])

x=[1,2,[11,("steve",33)],[["woz"],"jeff"]]

print(x[2][1][0],x[3][0][0],x[3][1] )


#tuple packing and unpacking

#packing all assinging multiple value in the single variable in single steps
# unpacking is  the extracting the value from the tuple

tup=(10,20,30,40,50)
print(tup)

a,b,c,d,e=tup
print(a)
print(b)
print(c)
print(d)
print(e)

#packing 
t=12,23,2,34,5
print(t)
print(type(t))

#unpacking
t=(12,23,2,34,5)
a,b,c,d,e=t
print(a)
print(b)
print(c)
print(d)
print(e)


#immutable:
'''we can not assign the  value to the tuple'''

# t=(10,20,30,40,50)
# t[0]=100
# print(t)

# methods in the tuple only two which is 

#1.index()
t=(10,20,30,40,50)
print(t.index(30))

#2.count

t=(10,20,30,40,50,10,10,10)
print(t.count(10))

# can we store the list inside the tupe
# yes we can store the list inside the tuple

t=(10,20,30,40,50,[1,2,3,4])
print(t)
print(type(t))

# can you able to the change in the tuples list
# yes we can able to the change in the tuples list
t=(10,20,30,40,50,[1,2,3,4])
t[5][0]=100
print(t)

# how to iterate the tuple

t=(10,20,30,40,50,[1,2,3,4])
for i in t:
    if type(i)==list:
        for j in i:
            print(j)
    else:        
        print(i)

# 1. Python program to find tuples which have all elements divisible by K from a list of tuples

# Input : test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)], K = 6 

# Output : [(6, 24, 12), (60, 12, 6)] 

t = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
K = 6 
print(len(t))
r=[]

for i in t:
    cnt=0
    
    for j in i:
        
        if j%6==0:
            cnt=cnt+1
    if cnt==len(i):
        print(i)
        r.append(i)
print(r)


# Explaination : Both tuples have all elements multiple of 6.
  

# 2. Python program to find Tuples with positive elements in List of tuples

# Input : test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 

# Output : [(4, 5, 9)] 
t = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]

r=[]

for i in t:
    cnt=0
    
    for j in i:
        
        if j>0:
            cnt=cnt+1
    if cnt==len(i):
        print(i)
        r.append(i)
print(r)    





# Explaination : Extracted tuples with all positive elements.

#  3. Python | Removing duplicates from tuple

# The original tuple is : (1, 3, 5, 2, 3, 5, 1, 1, 3)
t=(1, 3, 5, 2, 3, 5, 1, 1, 3)
r=[]

for i in t:
    if i not in r:
        r.append(i)
    
print(tuple(r))


''' remember the converting the tuple using the tuple the tuple()
        inside the tuple we can store the list
         syntax: tuple(list) => type casting '''


# The tuple after removing duplicates : (1, 3, 5, 2)

# 4. Python | Remove duplicate lists in tuples (Preserving Order)

 

# The original tuple is : ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
t=([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
r=[]

for i in t:
    if i not in r:
        r.append(i)
    
print(r)
# The unique lists tuple is : [[4, 7, 8], [1, 2, 3], [9, 10, 11]]


# 5. Python – Sum of tuple elements

# The original tuple is : (7, 8, 9, 1, 10, 7)
t=(7, 8, 9, 1, 10, 7)
sum=0
for i in t:
    sum=sum+i
print(sum)

# The summation of tuple elements are: 42

# Write a  Python program to remove an empty tuple(s) from a list of tuples.

# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
t=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(len(t[0]),len(t[3]))
r=[]
for i in t:
    if len(i)>0:
        r.append(i)
        
    
print(r)
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

# prime number in the tuple

t=(1,2,3,4,5,6,7,8,9,10)
r=[]
sum=0

for i in t:
    cnt=0
    for j in range(2,i//2):
        if i%j==0:
            cnt=cnt+1
    if cnt==0:
        r.append(i) 
        sum=sum+i
        

print("prime number:",r)
print("sum of the prime number:",sum)
print("count of the prime number:",len(r))
