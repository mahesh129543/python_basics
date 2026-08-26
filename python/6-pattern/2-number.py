# generating the num pattern

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    print() 
    i=i+1

n = 4
i = 0

while i < n:
    # Spaces
    space = 0
    while space < n - i - 1:
        print("  ", end="")
        space += 1

    # Numbers
    j = 0
    while j < 2 * i + 1:
        print(j + n - i, end=" ")
        j += 1

    print()
    i += 1


n = 4
i = 0

while i < n:

    space = 0
    while space < n - i - 1:
        print("  ", end="")
        space += 1

 
    j = 0
    while j < 2 * i + 1:
        print(j + n - i, end=" ")
        j += 1

    print()
    i += 1


n = 4

for i in range(n):
    
    print("  " * (n - i - 1), end="")

   
    for j in range(i * 2 + 1):
        print(j + n - i, end=" ")

    print()

print("triangle")


n = 4

for i in range(1, n + 1):

    for j in range(n - i):
        print("  ", end="")

    
    for j in range(1, 2 * i):
        print(j, end=" ")

    print()
print(" iverted triangle")

n = 4

for i in range(n, 0, -1):

    
    for j in range(n - i):
        print("  ", end="")

    for j in range(1, 2 * i):
        print(j, end=" ")

    print()