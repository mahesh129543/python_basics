a=23
b=35

print("the value of a is",a)
print("the value of b is",b)

temp=a
a=b
b=temp

print("the value of a is",a)
print("the value of b is",b)

#swapping number without the  3rd variable

a=12
b=22

print("the value of a is",a)        
print("the value of b is",b)

a=a+b
b=a-b
a=a-b

print("the value of a is",a)
print("the value of b is",b)

#de structuring
a=12
b=23
(a,b)=(b,a )

print("the value of a is",a)
print("the value of b is",b)