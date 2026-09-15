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

give index number'''

s="i love india"
print(s.find("y"))


#index()
'''find the index of the element in the string

syntax: string.index(value)

give index number'''

s="i love india"
print(s.index("i"))


