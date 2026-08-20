# # 1. Write a Python program to print the reverse of a number using a loop.

# num=234
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10

# print(rev)

# # 2. Write a Python program to check if a number is a palindrome or not.

# n1=int(input("enter the number:"))
# rev=0
# temp=n1
# while n1>0:
#     rem=n1%10
#     rev=rev*10+rem
#     n1=n1//10

# if temp==rev:   
#     print("palindrom")
# else:
#     print("not palindrom")


# # 3. Write a Python program to check if a number is an Armstrong number.
# n2=int(input("enter the number:"))
# sum=0
# temp=n2
# while n2>0:
#     rem=n2%10
#     sum=sum+rem*rem*rem
#     n2=n2//10

# if temp==sum:
#     print("armstrong")
# else:
#     print("not armstrong")
 

# # 4. Write a Python program to check if a number is a perfect number.
# n3= int(input("Enter a number: "))

# sum = 0

# for i in range(1, num):
#     if num % i == 0:
#         sum = sum + i

# if sum == num:
#     print("Perfect number")
# else:
#     print("Not a perfect number")

 

# # 5. Write a Python program to print all prime numbers up to a given number.
# n4=int(input("enter the number:"))
# for i in range(2,n4):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# # 6. Write a Python program to check if a number is prime or not.
# n5=int(input("enter the number:"))
# for i in range(2,n5):
#     if n5%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")

 

# # 7. Write a Python program to find all perfect numbers in a given range.
# n6=int(input("enter the number:"))
# for i in range(1,n6):
#     sum=0
#     for j in range(1,i):
#         if i%j==0:
#             sum=sum+j
#     if sum==i:
#         print(i)

 

# # 8. Write a Python program to find all Armstrong numbers in a given range.
# n7=int(input("enter the number:"))
# for i in range(1,n7):
#     sum=0
#     temp=i
#     while temp>0:
#         rem=temp%10
#         sum=sum+rem*rem*rem
#         temp=temp//10
#     if sum==i:
#         print(i)

 

# # 9. Write a Python program to find the sum of digits of a number using a loop.
# n8=int(input("enter the number:"))
# sum=0
# while n8>0:
#     rem=n8%10
#     sum=sum+rem
#     n8=n8//10
# print(sum)

 

# # 10. Write a Python program to count the number of even and odd digits in a number.
# n9=int(input("enter the number:"))
# e=0
# o=0
# while n9>0:
#     rem=n9%10
#     if rem%2==0:
#         e=e+1
#     else:
#         o=o+1
#     n9=n9//10
# print("even:",e)
# print("odd:",o)

# 11. Write a Python program to check if a number is a strong number.
num1=int(input("enter the number:"))
temp=num1
sum=0
while num1>0:
    d=num1%10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    num1=num1//10
if sum==temp:   
    print("strong")
else:
    print("not strong")
 

# 12. Write a Python program to print Fibonacci series up to a given number using a loop.
num2=int(input("enter the number:"))
a=0
b=1
print(a)
print(b)
for i in range(2,num2+1):
    c=a+b
    print(c)
    a=b
    b=c



 

# 13. Write a Python program to print all the divisors of a number.
num3=int(input("enter the number:"))
for i in range(1,num3+1):
    if num3%i==0:
        print(i)

 

# 14. Write a Python program to check if a number is an abundant number.
num4=int(input("enter the number:"))
sum=0
for i in range(1,num4):
    if num4%i==0:
        sum=sum+i

if sum>num4:
    print("abundunt")
else:
    print("not abundant")

 

# 15. Write a Python program to check if a number is a perfect square using a loop.
num = int(input("Enter a number: "))


if num < 0:
    print("not perfect square.")
else:
    i = 0
    perfect = False
    
   
    while i * i <= num:
        if i * i == num:
            perfect = True
            break
        i += 1
        
 
    if perfect:
        print("perfect square.")
    else:
        print("not perfect square.")