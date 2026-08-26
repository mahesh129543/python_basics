#alphabate pattern
# using hte chr() remember the chr fuction name not use the (char) fuction to get the character in program

i=1
while i<=5:
    j=1
    while j<=5:
        print(chr(64+i),end=" ")
        j=j+1

    print() 
    i=i+1   

for i in range(1,7):
    print(chr(64+i),end=" ")


print("right angle triangle")



for i in  range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

print("left angle triangle")


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

for i in  range(1,6):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()


for i in range(7,0,-1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
num=65
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(num),end=" ")
        num=num+1
    print()

#odd even pattern alphabates

num=65
for i in range(1,6):
    for j in range(1,i+1):
        if(num%2==0):
            print(chr(num),end=" ")
        else:
            print(chr(num+32),end=" ")
        num=num+1
    print()


