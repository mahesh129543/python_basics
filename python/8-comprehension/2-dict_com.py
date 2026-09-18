#dictionary comprehension
''' 
similar to list comprehension

syntax:
d={key:value for item in list if condition}




'''

l=[1,2,3,4,5,6]
l1=["even" if i%2==0 else "odd" for i in l]
print(l1)

d={i:i*i for i in range(1,6)}
print(d)


d={i:i*i for i in range(1,6) if i%2==0}
print(d)

d={i:i*i for i in range(1,6) if i%2!=0}
print(d)

#Create a dictionary where keys are names and values are their lengths.
list1=["jay", "mina", "leena", "komal"]
d={i:len(i) for i in list1}
print(d)

#Double the values in a dictionary:
o={'a': 1, 'b': 2, 'c': 3}
d={k:v*2 for k,v in o.items()}
print(d)


#Create a dictionary of first 6 natural numbers where
#key number, value "even" or "odd"
d={i:"even" if i%2==0 else "odd" for i in range(1,7)}
print(d)


#create a dictionary in values are only with length > 3
words =["apple", "bat", "banana", "cat"]
d={i:len(i) for i in words if len(i)>3}
print(d)
#Create a new dictionary with 10% increased price
#prices ("pen": 10, "book": 58, "bag": 408)

prices ={"pen": 10, "book": 58, "bag": 408}

d={k:(v*10)//100 +v for k,v in prices.items()}
print(d)



# Find all unique vowels present in a string using List comprehension.
# Find all unique digits present in a string
#text = "abc123def345xyz12"

text = "abc123def345xyz12"
l=[i for i in text if i in 'aeiouAEIOU']
print(l)

text = "abc123def345xyz12"
l=[i  for i in text if i.isdigit() and text.count(i)==1] 
print(l)


words = ["Python", "SQL", "PowerBI", "Excel", "Pandas"]

# Create a list containing the first letter in lowercase for words having length greater than 4.

l=[i[0].lower()+i[1:] for i in words if len(i)>4]
print(l)