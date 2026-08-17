# for loop

# defination: a loop that executes a block of code a certain number of times.
# what is range function

# range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
# starting number of the sequence by deault is 0 and increment by 1 by default

# syntax:

'''
for variable in sequence:
    statement1
    statement2
    statement3
    statement4

'''
#there are 4-5 imp point in for loop
#1. initialization
#2. condition  
# print/block of code 
#3. increment
#4. decrement


#for i in range(num):
    #print(i)


#example

# for i in range(1,11):
#     print(i,end=" ")


# for i in range(11,21):
#     print(i,end=" ")


# print("\n")

# for i in range(2,11,2):
#     print(i,end=" ")

# for i in range(1,11,2):
#     print(i,end=" ")

# Q1.Display numbers from 1 to 100.

# for i in range(1,101):
#     print(i,end=" ")
# # Q2.Display all even numbers from 1 to 100. 
# for i in range(2,101,2):
#     print(i,end=" ")
# # Q3. Write a program to print all natural numbers from 1 to n. - using for loop
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     print(i,end=" ")
# # Q4. Write a program to print all natural numbers in reverse (from n to 1). - using for loop
# for i in range(n,0,-1):
#     print(i,end=" ")

# # Q5. Write a program to print all odd number between 1 to 100.

# for i in range(1,101,2):
#     print(i,end=" ")

# Q6. Write a program to find sum of all natural numbers between 1 to n.

# n=int(input("enter the number:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i   
# print(sum)

# # Q7. Write a program to find sum of all even numbers between 1 to n.
# n=int(input("enter the number:"))
# sum=0
# for i in range(2,n+1,2):
#     sum=sum+i   
# print(sum)
# # Q8. Write a program to find sum of all odd numbers between 1 to n.
# n=int(input("enter the number:"))
# sum=0
# for i in range(1,n+1,2):
#     sum=sum+i   
# print(sum)
# # Q9.Wap enter your name and print it five times.
# name=input("enter your name:")
# for i in range(5):
#     print(name)
# # Q10.Wap take two input and display all odd numbers between them and find sum and count.
# n1=int(input("enter the number:")) 
# n2=int(input("enter the number:"))
# sum=0
# cnt=0
# for i in range(n1,n2+1):
#     if i%2!=0:
#         print(i,end=" ")
#         sum=sum+i
#         cnt=cnt+1
# print()
# print(sum)
# print(cnt)
# # Q11.Wap take two inputs and display all even numbers between them and find sum and count.
# n1=int(input("enter the number:")) 
# n2=int(input("enter the number:"))
# sum=0
# cnt=0
# for i in range(n1,n2+1):
#     if i%2==0:
#         print(i,end=" ")
#         sum=sum+i
#         cnt=cnt+1
# print()
# print(sum)
# print(cnt)

# num1=int(input("enter the number:"))
# num2=int(input("enter the seond number:"))

# for i in range(num1,num2+1,2):
#     print(i)

#generate the table of 7

for i in range(1,11):
    print(7,"*",i,"=",7*i)