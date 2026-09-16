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
    
