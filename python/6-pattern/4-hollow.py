# hollow pattern :

i=1
while i<=5:
    j=1
    while j<=5:
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print() 
    i=i+1

for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or j == i or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(1, i + 1):
        if  j == i or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if i==3 or j==3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if  j==i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        if  j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if j==i or j==6-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if j==i or i==1 or j==5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 10):
        if j==i or j==10-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if j==i or j==1 or j==5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# m shape

for i in range(1, 6):
    for j in range(1, 10):
        if j==i or j==10-i or j==1 or j==9:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#pyramid

for i in range(1, 6):
    for j in range(1, 10):
        if  j==5-i or j==5+i or i==5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



# butterfly

n=4
for i in range(1, n+1):
    print("*"*i + " " * (2*(n-i)) + "*" * i)

for i in range(n-1, 0, -1):
    print("*"*i + " " * (2*(n-i)) + "*" * i)

