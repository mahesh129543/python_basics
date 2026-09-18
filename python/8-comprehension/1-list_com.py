# list comprehension

#list comprehension is consies way to create the list on performing
# the operation on the existing list
'''sorther and clean code and also the fast execution

synax: l2=[( expression ) for item in list (if any conditins)]
expression is the operation which we want to perform

it will give the list
if any specific condition the apply the operation

'''


l1=[1,2,3,4,5,6]
l2=[i**2 for i in l1 if i%2==0]
print(l2)


l=[1,2,3,4,5,6,7,8,9]
l3=[i for i in l if i%2==0]
print(l3)

l=[1,2,3,4,5,6,7,8,9]
l3=[i for i in l if i%2!=0]
print(l3)

#
s=["apple", "banana", "kiwi"]
s1=[i[0] for i in s]
print(s1)


s=["alice", "kiwi", "kiya", "illina"]
s1=[ i for i in s if i[0] in 'aeiouAEIOU']
print(s1)

# 1. From a list of words, get the length of each word.l=["hello","hii","welcome","thankyou"]
l=["hello","hii","welcome","thankyou"]
l1=[len(i) for i in l]
print(l1)

# 2. Create a list of numbersmthat are divisible by both 3 and 5.[11,23,15,30,67,45]
l=[11,23,15,30,67,45]
l1=[i for i in l if i%3==0 and i%5==0]
print(l1)
# 3. Get the first letter of each word in a list if the word has more than 3 letters. w=["jay","kiya","jefff","lilyy"]
w=["jay","kiya","jefff","lilyy"]
w1=[i[0] for i in w if len(i)>3]
print(w1)

# 4. Print the table of 8.
l=[i*8 for i in range(1,11)]
print(l)

# 5. Write a Python program that takes a list of integers and returns the sum of the squares of the even numbers using list comprehension.

#    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l=[i**2 for i in n if i%2==0]
print(sum(l))

#    Output: 220

# 6. sentence = "list comprehension is cool" From sentence extract only vowel.
sentence = "list comprehension is cool"
s1=[i for i in sentence if i in 'aeiouAEIOU']
print(s1)
# 7. Write a Python program that takes a list and returns a new list containing only the unique elements using list comprehension.

#    elements = [1, 2, 3, 2, 4, 5, 6, 3, 7]
e = [1, 2, 3, 2, 4, 5, 6, 3, 7]
l=[i for i in e if e.count(i)==1]
print(l)

#    Output: [1, 4, 5, 6, 7]

# 8.  Given a list of integers, return a list with all negative numbers removed.

#    numbers = [-1, 2, -3, 4, -5, 6]
n = [-1, 2, -3, 4, -5, 6]
l=[i for i in n if i>0]
print(l)

#    Output: [2, 4, 6]

    

# 9. Find the common elements in two lists using list comperhension.

list1 = [1, 2, 3, 4]

list2 = [3, 4, 5, 6]

l=[i for i in list1 if i in list2]
print(l)

#    Output: [3, 4]

        

# 10.Write a Python program that takes a list of integers and returns the count of the odd numbers using list comprehension.


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l=[i for i in n if i%2!=0]
print(len(l))



