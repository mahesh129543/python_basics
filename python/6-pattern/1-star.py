# star patten

#using the while looop
#5*5 star pattern

i=1
while i<=5:
    j=1
    while j<=5:
        print("*",end=" ")
        j=j+1
    print() 
    i=i+1

i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print() 
    i=i+1

print("using for loop")
# using for loop

for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()


i=1
while i<=5:
    j=5
    while j>=i:
        print("*",end=" ")
        j=j-1
    print() 
    i=i+1



i = 1

while i <= 5:


    j = 5
    while j > i:
        print(" ", end=" ")
        j = j - 1

    
    k = 1
    while k <= i:
        print("*", end=" ")
        k = k + 1

    print()
    i = i + 1


i = 1

while i <= 5:
    

    j = 1
    while j < i:
        print(" ", end=" ")
        j = j + 1


    k = 1
    while k <= 6 - i:
        print("*", end=" ")
        k = k + 1

    print()
    i = i + 1




i = 1

while i <= 5:
  
    j = 1
    while j <= 5 - i:
        print(" ", end="")
        j += 1

  
    j = 1
    while j <= i:
        print("* ", end="")
        j += 1

    print()
    i += 1    

i = 1

while i <= 5:


    j = 5
    while j > i:
        print(" ", end=" ")
        j = j - 1

    
    k = 1
    while k <= i:
        print("*  ", end=" ")
        k = k + 1

    print()
    i = i + 1
print("new pattern")

i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print() 
    i=i+1


i=1
while i<=4:
    j=4
    while j>=i:
        print("*",end=" ")
        j=j-1
    print() 
    i=i+1

print("odd pyramid")

i = 1

while i <= 4:
  
    j = 1
    while j <= 4 - i:
        print("  ", end="")
        j += 1

  
    j = 1
    while j <= i*2-1:
        print("* ", end="")
        j += 1

    print()
    i += 1    

