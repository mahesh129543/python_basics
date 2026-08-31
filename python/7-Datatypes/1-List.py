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