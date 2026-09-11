# Set :
# set is a collection of unique items

# defination : a set is a collection of unique items
# set is mutable
# features:
# 1. unordered
# 2. unindexed
# 3. unchangeable
# 4. mutable    
# set are created usigg the curly brackets {}
# syntax : set1={value1,value2,value3}
# one important that do not use the set name is set it is a reserved word
# set element is hashable which is fixed
set1={12,34,56,78,90}
print(set1)

set2={"mahesh",22,"pune"}
print(set2)

set3={"mahesh",22,22,22,22,44,44,44,44,"pune",12,23,34,45,56}
print(set3)

#list1=[1,2,3,4,1,2,3,4,5,6,7,8]
#remove all the duplicates without using loop:

list1=[1,2,3,4,1,2,3,4,5,6,7,8]
s=set(list1)
print(list(s))

# inbuilt mehtod in set
#1.add():
''' add() is use to add the element 
in the set only one elment can be added at a time
at any position'''

set1={12,34,56,78,90}
set1.add(100)
print(set1)

s={1,2,3,4,5,6,7,8}
s.add(100)
s.add(200)
print(s)


# deletion methods
#1. remove()
'''
remove() is use to remove the element from the set
'''

set1={12,34,56,78,90}
set1.remove(90)
print(set1)

set1={12,34,56,78,90}
set1.remove(90)
print(set1)


# 2. discard()
'''
discard() is use to remove the element from the set
which is different to the remove
which like using remove method it will give the error at the time
of the element is not in the set and
discard method will not give the error if the element is not present
'''
set1={12,34,56,78,90}
set1.discard(90)
print(set1)

set1={12,34,56,78,90}
set1.discard(90)
print(set1)

#pop()
'''
pop() is use to remove the element from the set
pop is rmove random element in the set not need to 
give the specific index
it will remove the  1st element in unordered collection
'''
set1={1,2,3,4,5,6,7,8}
set1.pop()
print(set1)

set1={12,34,56,78,90}
set1.pop()
print(set1)

# clear()
'''
clear() is use to remove all the element from the set
the structure will be empty and there
'''
set1={12,34,56,78,90}
set1.clear()
print(set1)

#del
'''
del is use to delete the set
'''
set1={12,34,56,78,90}
del set1
# print(set1)


# difference()
'''
difference() is use to find the difference between two sets
it will give different element as caompare to set 1 only
it will return uncommon and unique element from set 1
'''
set1={1,2,3,4,5,6,7,8}
set2={3,4,5,6,7,8,9,10}
print(set1.difference(set2))

set1={1,2,3,4,5,6,7,8}
set2={3,4,5,6,7,8,9,10}
print(set1.difference(set2))

#difference_update
'''

'''
set1={1,2,3,4,5,6,7,8}
set2={3,4,5,6,7,8,9,10}
set1.difference_update(set2)
print(set1)

set1={1,2,3,4,5,6,7,8}
set2={3,4,5,6,7,8,9,10}
set1.difference_update(set2)
print(set1)

#symetric_difference()
'''
it is giving the different element of both that
is avoiding the all common element and give the all element
in both set
'''
set1={1,2,3,4,5,6,7,8}
set2={3,4,5,6,7,8,9,10}
print(set1.symmetric_difference(set2))


#intersection()
'''
it is use to find the common element in both set
'''
set1={1,2,3,4,5,6,7,8}
set2={3,4,5,6,7,8,9,10}
print(set1.intersection(set2))


#intersection_update()
'''
it is use to find the common element in both set
'''
set1={1,2,3,4,5,6,7,8}
set2={3,4,5,6,7,8,9,10}
set1.intersection_update(set2)
print(set1)

#union()
'''
it is use to find the all element in both set
'''
set1={1,2,3,4,5,6,7,8}
set2={3,4,5,6,7,8,9,10}
print(set1.union(set2))


#isdisjoint()
'''
it is use to find the common element in both set
it gives boolen 
if both sethave unique then it will give the true
'''
set1={1,2,3,4,5,6,7,8}
set2={3,4,5,6,7,8,9,10}
print(set1.isdisjoint(set2))

s={1,2}
s1={5,6,7,}
print(s.isdisjoint(s1))

#issubset()
'''
it is use to find the common element in both set
it gives boolen
'''
set1={1,2,3,4,5,6,7,8}
set2={3,4,5}
print(set2.issubset(set1))

#issuperset()
'''
if the all element of set2 is present in
set1 then it will give the true other wise false
it gives boolen
'''
set1={1,2,3,4,5,6,7,8}
set2={3,4,5}
print(set1.issuperset(set2))


#update()
'''
it is use to update the set
'''
set1={1,2,3,4,5,6,7,8}
set2={45}
set1.update(set2)
print(set1)

# 1.Create a set with the elements (2, 4, 6, 8, 10) and add the number 12 to it.

# 2. Remove the number 4 from a set (1, 2, 3, 4, 5} using an appropriate method.
#3. Remove the number 5 from a set{1,2,3} using remove method, observe output.

#How is it different from discard()?
# 4.Check whether the number 7 is present in the set (3, 5, 7, 9).
#5. Find the union of two sets: 1, 3, 5} and {2, 4, 6).
#6.Find the intersection of (1, 2, 3, 4) and (3, 4, 5, 6).

