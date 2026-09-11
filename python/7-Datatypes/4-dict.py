




# frequency cont of char

s="apple"
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)



# 1. Convert two list into one dictionary. (using zip function and without zip function)


l1=[1,2,3]
l2=["a","b","c"]

d={}
for i in range(len(l1)):
    d[l1[i]]=l2[i]
print(d)

 

# 2. Write a Python script to sort (ascending and descending) a dictionary by value.



d={"a":67,"b":43,"c":45}

l=d.items()

l1=list(l)
l2=[]

for i in l1:
    print(i[1])
    l2.append(i[1])
print((l2))

l2.sort()
print(l2)
d3={}

for i in l2:
    for j in d:
        if i==d[j]:
            print(j)
            d3[j]=i

print(d3) 

d={"apple":78, "banana": 45, "grapes": 100}
l=d.items()
l=(list(l))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i][1] > l[j][1]:
            l[i], l[j] = l[j], l[i]
print(dict(l))
#{'banana': 45, 'apple': 78, 'grapes': 100)





 

# 3. Write a Python program to combine two dictionary by adding values for common keys.

d1={"rohit":45, "virat":89, "laxman":34} 
d2={"dhoni":7,"rohit": 10, "rahul":56}

d3={}

for i in d1:
    if i in d2:
        d3[i]=d1[i]+d2[i]
    else:
        d3[i]=d1[i]
print(d3)

d1={"rohit":45, "virat":89, "laxman":34} 
d2={"dhoni":7,"rohit": 10, "rahul":56}
d=d1.copy()

for k,v in d2.items():
    if k in d:
        d[k]=d[k]+v
    else:
        d[k]=v
print(d)




 

# 4. Write a Python function to count the frequency of each word in a given text document 

#    and return a dictionary with word frequencies.

s="mahesh is good boy is good boy"
d={}
for i in s.split():
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

 

# 5. Given two dictionaries, write a function to find and return a new dictionary containing 

#    only the common keys and their corresponding values.

d1={"a":23,"b":43,"c":45}
d2={"b":43,"c":45,"d":67}

d3={}
for i in d1:
    if i in d2:
        d3[i]=d1[i]
print(d3)


    

# 6. Develop a function that finds the element with the maximum frequency in a list 

#     and returns the element along with its frequency.

l1=[1,2,3,4,3,5,6,5,4,3,2,4,4,4,4,4,5,6]

d={}
for i in l1:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
max=0
for i in d:
    if d[i]>max:
        max=d[i]
       
print(max)

    

# 7. Write a Python script to concatenate the following dictionaries to create a new one.

#     d1={1:20,2:30,3:70}

#     d2={4:89,5:90,6:87}

#     d3={7:90,8:34,9:63}
d1={1:20,2:30,3:70}

d2={4:89,5:90,6:87}

d3={7:90,8:34,9:63}
d4={}
for i in d1:
    d4[i]=d1[i]
for i in d2:
    d4[i]=d2[i]
for i in d3:
    d4[i]=d3[i]
print(d4)

 

# 8. WAP and Find the Key with Maximum Value.

d={"apple":78, "banana": 45, "grapes": 100}

max=0
for i in d:
    if d[i]>max:
        max=d[i]
print(max)
for i in d:
    if d[i]==max:
        print(i)


 

# 9. Write a function to invert a dictionary, swapping keys and values.(with duplicates value)

d={"apple":78, "banana": 45, "grapes": 100}

d1={}

for i in d:
    d1[d[i]]=i
print(d1)

 

# 10. Find the common keys between two dictionaries and return a dictionary with common keys 

#     and their values from the first dictionary.

d1={"rohit":45, "virat":89, "laxman":34} 
d2={"dhoni":7,"rohit": 10, "rahul":56}

d3={}

for i in d1:
    if i in d2:
        d3[i]=d1[i]
print(d3)

# check palindrom

l=[1,2,1]
i=0
j=len(l)-1
while i<j:
    if l[i]==l[j]:
        print("palindrom")
    else:
        print("not palindrom")
    i=i+1
    j=j-1




