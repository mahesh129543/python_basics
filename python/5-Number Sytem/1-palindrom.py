# what is the palindrom
#
# defination: a word, phrase, or sequence that reads the same backward as forward, such as madam or a man, a plan, a canal: Panama.
# example: madam, kayak, radar, level, kayak

# check the num is palindrom or not

num=int(input("enter the num:"))
temp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

if temp==rev:   
    print("palindrom")
else:
    print("not palindrom")


# WAP to print that palindrom number who's sum is greater then 9
# input: 545
# output: this is palindrome number who's sum is greater then 9


num=int(input("enter the num:"))
temp=num
rev=0
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    rev=rev*10+rem
    num=num//10

if temp==rev and sum>9:   
    print("palindrom and sum is greater then 9")
else:
    print("not palindrom")
