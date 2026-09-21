"""String: Sequence data type:
-- String is a collection of homogeneous as well as hetrogeneous data.
Indexed and ordered
Im-Mutable (not changable)
Allows duplicate
String are collection of characters which enclosed in single double triple coates"""


s="i love mahesh" 
print(s)
print(type(s))
print(len(s))
print(s[2])
print(s[2:5])


text = "Hello, World!"

#o/p:Hello by +ve slicing
print(text[0:5])

#o/p:World! by +ve slicing
print(text[7:])

#o/p:Hello by -ve slicing
print(text[-13:-8])


#o/p:World! by -ve slicing
print(text[-6:])

# revere the string
s="mahesh"
print(s[::-1])

s="mahesh"
s1=""
i=len(s)-1
while i>=0:
    s1=s1+s[i]
    i=i-1
print(s1)

s="mahesh narke"
s1="" 
for i in s:
    s1=i+s1
print(s1)


# inbuit methods in string

#upper()
'''convert the string into upper case'''
s="mahesh"

res=s.upper()
print(res)

#lower()
'''convert the string into lower case'''
s="MAHEsh"
print(s.lower())


#swapcase()
'''convert the string into upper case'''
s="MAHEsh"
print(s.swapcase())

# strip()
'''remove the space from the string'''
s=" mahesh "
print(s.strip())


# lstrip()
'''remove the space from the string'''
s=" mahesh "
print(s.lstrip())


# rstrip()
'''remove the space from the string'''
s=" mahesh "
print(s.rstrip())

#split()
'''split the string and return the list and by default it will split by space
 '''
s="i love pune and i am happy to be here"
print(s.split())

s="i love #pune"
print(s.split("#"))


# s=input("enter the full name:")

# res=s.split(" ")
# if len(res)==3:
#     print(f"first name is {res[0]} and Middle name is {res[1]} and last name is {res[2]}")

# else:
#     print("please enter the full name")


# replace()
'''replace the string'''
s="i love pune"
print(s.replace("pune","mumbai"))

#capitalize()
'''capitalize the string first letter to upper case'''
s="i love pune"
print(s.capitalize())


# title()
'''capitalize the string each word first letter to upper case'''
s="i love pune"
print(s.title())


# format()
'''format the string and sequence is same at format
place holder is {} is use to replace the value'''
s="i love {} and {}"
print(s.format("pune","mumbai"))


# count all vowels from the string

s="i love india"
d={}
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
print(d)

l=["mahesh","pune","india","at"]
l1=[]

for i in l:
    if i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u":
        l1.append(i)
print(l1)



#count()
'''count the element in the string  give number of cout of specied element

syntax: string.count(value)'''

s="i love india"
print(s.count("i"))

#startswith()
'''check the string start with specific value or not

syntax: string.startswith(value)

give true or false'''

s="i love india"
print(s.startswith("i"))

#endswith()
'''check the string end with specific value or not

syntax: string.endswith(value)

give true or false'''

s="i love india"
print(s.endswith("a"))

l=["mahesh","pune","india","at"]

for i in l:
    if i.startswith("a") or i.startswith("e") or i.startswith("i") or i.startswith("o") or i.startswith("u"):
        print(i)



# find()
'''find the index of the element in the string

syntax: string.find(value)

give index number but if not present it will give -1'''

s="i love india"
print(s.find("y"))


#index()
'''find the index of the element in the string

syntax: string.index(value)

give index number but if not present it will give error'''

s="i love india"
print(s.index("i"))

#rfind()
'''find the last index of the element in the string

syntax: string.rfind(value)

give index number but if not present it will give -1'''

s="i love india"
print(s.rfind("i"))


#rindex()
'''find the last index of the element in the string

syntax: string.rindex(value)

give index number but if not present it will give error'''

s="i love india"
print(s.rindex("i"))





#automorphic number
'''number which is same as its square last digit is same'''




# n = int(input("Enter the number: "))

# sq = n * n

# if str(sq).endswith(str(n)):
#     print("Automorhic number")
# else:
#     print("Not an autorphic number")





#center()
'''center the string using the given length and also 
add the character in between the string ohterwise it will add the space
'''

s="mahesh"
print(s.center(9,"*"))

#isalnum()
'''check the string is alphanumeric or not

syntax: string.isalnum()

give true or false'''

s="mahesh123"
print(s.isalnum())

s="mahesh"
print(s.isalnum())


#isalpha()
'''check the string is alphabetical or not

syntax: string.isalpha()

give true or false'''

s="mahesh"
print(s.isalpha())

s="mahesh123"
print(s.isalpha())


#isdigit()
'''check the string is digit or not

syntax: string.isdigit()

give true or false'''

s="123"
print(s.isdigit())

s="mahesh"
print(s.isdigit())

#isascii()
'''check the string is ascii or not

syntax: string.isascii()

give true or false

'''

s="mahesh"
print(s.isascii())

s=""
print(s.isascii())


#islower()
'''check the string is lowercase or not

syntax: string.islower()

give true or false'''

s="mahesh"
print(s.islower())

s="MAHEsh"
print(s.islower())


#isupper()
'''check the string is uppercase or not

syntax: string.isupper()

give true or false'''

s="MAHEsh"
print(s.isupper())

s="mahesh"
print(s.isupper())

#isspace()
'''check the string is space or not

syntax: string.isspace()

give true or false'''

s=" "
print(s.isspace())

s="mahesh"
print(s.isspace())

#istitle()
'''check the string is title or not

syntax: string.istitle()

give true or false'''

s="Mahesh"
print(s.istitle())

s="mahesh"
print(s.istitle())

# join()
'''join the string using the given character

syntax: string.join(iterable)'''

l=["mahesh","pune","india","at"]
res=" ".join(l)
print(res)               


# 1. WAP to print all the consonants char from the String.
s="i love india"
l=[]

for i in s:
    if i not in "aeiouAEIOU":
        l.append(i)
print(l)

# 2. Print the words which starts from vowels in list.["amayra","rohit","illina","virat"]
l=["amayra","rohit","illina","virat"]

for i in l:
    if i[0] in 'aeiouAEIOU':
        print(i)
# 3. WAP to convert all the consonants char in lowercase case.
s="I LOVE INDIA"
res=""
for i in s:
    if i not in "aeiouAEIOU":
        res=res+i.lower()
    else:
        res=res+i
print(res)
# 4. WAP to check whether the all strings are in upper case or not:
s="MAHESH"
if s==s.upper():
    print("all strings are in upper case")
else:
    print("all strings are not in upper case")


# 5.WAP to check whether the all strings are in lower case or not:
s="MAHESH"
if s==s.lower():
    print("all strings are in lower case")
else:
    print("all strings are not in lower case")



s=" i name is mahesh"
res=""
for i in s:
    if i in "aeiouAEIOU":
        res=res+i.replace(i,"#")
    elif i in " ":
        res=res+i
    else:
        res=res+i.replace(i,"*")
print(res)
# WAP to replace all the even position char to %


s="my name is mahesh"
res=""
for i in range(len(s)):
    if i%2==0:
        res=res+s[i].replace(s[i],"%")
    elif s[i] in " ":
        res=res+s[i]
    else:
        res=res+s[i]
print(res)



#Write a Python program that takes a list of words 
# # and return the longest word


l=["mahesh","pune","india","at"]
res=""

for i in l:
    if len(i)>len(res):
        res=i
       
print(res)


# and return the longest word and the length of the longest one.
list1 = ["hii", "hello", "welcome"]

op = []

for i in list1:
    op.append((i, len(i)))

print(op)


#Reverse the words, order should be maintained
# string="Hello world"
#output: "olleh dlrow"

s="Hello world"
res=s.split(" ")
s1=""

for i in res:
    s1=s1+" "+(i[::-1])

print(s1)


s=" i like python"
word=s.split(" ")
res=""

for i in range(len(word)-1,-1,-1):
    res=res+word[i]+" "
    

print(res)

l=[1,2,3]
s=""
for i in l:
    s=s+str(i)
print(s)
print(type(s))



s="1,2"
l=s.split(",")
l1=[]
for i in l:
    l1.append(int(i))
print(l1)



#partition()
'''partition the string and return tuple 
it will separet the string in the specific values.
syntax: string.partition(substring)
partition will count in threeparts'''
s="i love india"
print(s.partition("love"))

#rpartition()
'''partition the string and return tuple 
it will separet the string in the specific values from the right.
syntax: string.rpartition(substring)
partition will count in threeparts'''
s="i love india"
print(s.rpartition("india"))

#zfill()
'''fill the string with zero in the left side
syntax: string.zfill(width)

width is the length of the string plus zeors
length of string is equal to the width'''
s="mahesh"
print(s.zfill(10))


# sorted()
'''sort the string 
sort the aplhabets in acsending order and give the list 
syntax: sorted(string)
return the list'''
s="i love india"
print(sorted(s))

# anagram string

# to check the giving strings are anagram or not

# s1=input("enter string:")
# s2=input("enter string:")
# d={}
# for i in s1:
#     d[i]=d.get(i,0)+1
# for i in s2:
#     d[i]=d.get(i,0)-1
# for i in d:
#     if d[i]!=0:
#         print("not anagram")
#         break
# else:
#     print("anagram")


# s1=input("enter string:")
# s2=input("enter string:")
# l=[]
# for i in s1:
#     l.append(i)
# for i in s2:
#     if i in l:
#         l.remove(i)
#     else:
#         print("not anagram")
#         break
# else:
#     print("anagram")





# 1.WAP to print the username only from the list of email

# # input= ["virat@gmail.com","dhoni@gmail.com","rohit@gmail.com"]
input= ["virat@gmail.com","dhoni@gmail.com","rohit@gmail.com"]

l=[]
for i in input:
    l.append(i.split("@")[0])
print(l)

# # output: [virat,dhoni,rohit]

 

# 2.Count Words in a Sentence:

# # Given a sentence, count the number of words in it using the split method.

sentence = "I like to code in Python"

l=sentence.split(" ")
print(len(l))

 

# 3.Extract Domain Names from Emails:

# # Given a list of email addresses, extract the domain names using the split method

input= ["user1@example.com", "user2@domain.com", "user3@company.org"]

l=[]
for i in input:
    l.append(i.split("@")[1])
print(l)

 

# 4.Convert a Sentence into a List of Words.



sentence = "I like to code in Python"

l=sentence.split(" ")
print(l)

 

# 5. Find the Longest Word in a Sentence:

# # Given a sentence, find the longest word using the split method.

sentence = "Identify the longest word in this sentence."

l=sentence.split(" ")
res=""
for i in l:
    if len(i)>len(res):
        res=i
       
print(res)

# # output: 'sentence.'

 

# 6.Check for Palindrome Words in a Sentence:

# #Given a sentence, check which words are palindromes using the split method.

sentence = "Madam Arora teaches malayalam"

l=[]
s=sentence.split(" ")
for i in s:
    rev=""
    for j in i.lower():
        rev=j+rev
    if rev==i.lower():
        l.append(i)
print(l)

# #output: ['madam', 'Arora', 'malayalam']


s="hello this is my world"

#you need to print most frequent element.

d={}
max=0
key=""
for i in s:
    d[i]=d.get(i,0)+1


for i in d:
    if i!=" " and d[i]>max:
        max=d[i]
        key=i
print(max,key)

l=["mango", "lichi", "grapes", "banana", "apple"]

# most frquent element

d1={}
for i in l:
    for j in i:
        d1[j]=d1.get(j,0)+1

max=0
key=""
for i in d1:
    if d1[i]>max:
        max=d1[i]
        key=i
print(max,key)

# String Expansion:
s="a2b3c5"
i=0
op=""
while i<len(s):
    if s[i].isalpha():
        op=op+s[i]
    else:
        op=op+s[i-1]*(int(s[i])-1)
    i=i+1
print(op)
# op="aabbbccccc"


s="aabbbccCCC"
d={}
for i in s:
    i=i.lower()
    d[i]=d.get(i,0)+1
print(d)
for k,v in d.items():
    print(k+str(v),end="")



   


#res="a2b3c5"


# longest substring without repeating characters
s="hello"

l=[]
max=0
srt=""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        if len(sub)==len(set(sub)):
            l.append(sub)
            if len(sub)>max:
                    max=len(sub)
                    srt=sub
print(l)
print(srt)

s="hello"
cur=""
log=""
for i in s:
    if i in cur:
        cur=cur[cur.index(i)+1:] #1
    cur=cur+i 
    if len(cur) > len (log):
        log=cur
print(log)


s="ad#b"

s1=[]
for i in s:
    if i =='#':
        s1.pop()
    else:
        s1.append(i)
print("".join(s1))

s="ah#b"
res=""
for i in s:
    if i=="#":
        res=res[:-1]
    else:
        res=res+i
#ah
print(res)
s="ab"


s="i live in pune2 and my code is 42201"
#Print the sum of all the numbers so op = 11

sum=0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
print(sum)

# Write a function to find the first non-repeating character in a string.

def nonrep(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    for k,v in d.items():
        if v==1:
            return k
        
  
print(nonrep("hsdgsfhgyteefbsdb"))