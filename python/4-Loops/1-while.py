# while loop

#defination: a loop that executes a block of code as long as a certain condition is true.

#syntax:

'''
while condition:
    statement1
    statement2
    statement3
    statement4

'''
#there are 4-5 imp point in while loop
#1. initialization
#2. condition  
# print/block of code 
#3. increment
#4. decrement


#example

i=1
while i<=10:
    print(i,end=" ")
    i=i+1

j=10
while j>=1:
    print(j,end=" ")
    j=j-1

#print even


print("\n")

i=1

while i<=20:
    if i%2==0:
        print(i,end=" ")
    i=i+1

print("\n")



#write program to all natural numbers 1-n



n=int(input("enter the number:"))
i=1
while i<=n:
    print(i,end=" ")
    i=i+1

n=int(input("enter the number:"))
i=n
while i>=1:
    print(i,end=" ")
    i=i-1



i=1

while i<=50:
    if i%2!=0:
        print(i)
    i=i+1