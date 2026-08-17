# iterative for loop
# defination: a loop that executes a block of code a certain number of times.
# we use the iterative for loop at the time of fetchig the individual data from the list'

# syntax:

'''
for variable in sequence:
    statement1
    statement2
    statement3
    statement4

'''
#there are 4-5 imp point in for loop
#1. initialization
#2. condition  
# print/block of code 
#3. increment
#4. decrement


# list1=[12,23,34,45,56]
# for i in list1:
#     print(i)    

# # sum of  all the elements in the list

# list1=[12,23,34,45,56]
# sum=0
# for i in list1:
#     sum=sum+i
# print(sum)  

# # len fuction

# list1=[12,23,34,45,56]
# for i in range(len(list1)):
#     print(f"index is {i} and value is {list1[i]}")   
#  #print(i,list1[i])


# l1=[12,23,34,45,56]
# for i in l1:
#     print(l1.index(i),i)
#     print()

# #


# print the no not divisible by 5 from list l=[1,2,3,5,15,10,4]

l=[1,2,3,5,15,10,4]
for i in l:
    if i%5!=0:
        print(i)


# print the no divisible by 3 from list l=[1,2,3,5,6,10,9]

l=[1,2,3,5,6,10,9]
for i in l:
    if i%3==0:
        print(i)


# print the even indexed elements of list l=[16,15,11,13,1,10]

l=[16,15,11,13,1,10]
for i in range(len(l)):
    if i%2==0:
        print(l[i])


# Count how many times 's' occurs in l = ['s','a','s','x','s']

l=['s','a','s','x','s']
cnt=0
for i in l:
    if i=='s':
        cnt=cnt+1
print(cnt)
# Print numbers greater than 10 from l = [5, 12, 3, 20, 8]


l=[5, 12, 3, 20, 8]
for i in l:
    if i>10:
        print(i)