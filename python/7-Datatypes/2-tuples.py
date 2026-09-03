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