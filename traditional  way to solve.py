# palindrome
num = 121
temp = num
rev = 0
while temp > 0:
    remaining = temp % 10
    rev = (rev*10) + remaining
    temp = temp // 10
if num == rev:
    print("palindrome")
else:
    print("not palindrome")

# armstrong
num = 153
temp = num
sum = 0
times = 0
while temp>0:
    times = times + 1
    temp = temp // 10
print(times)

temp = num
sum = 0
while temp>0:
    remaining = temp % 10
    sum = sum + pow(remaining,times)
    temp = temp // 10
print("sum is", sum)

if num == sum:
    print("num is armstrong")
else:
    print("num is not armstrong")


a = [10,20,30]
b = [10,20,340,50]

print(a > b)

num = 12345
while num>0:
    a = num % 10
    num = num // 10
print(a)

num = 12345
a = num % 10
print(a)

""" 
n = int(input("pls enter total nums:"))
num = []
for i in range(n):
    num.append(int(input("enter value of %d:" % (i+1))))
for i in range(len(num)):
    print("elements of list n is:",num[i])

print()
n = int(input("enter total entries:"))
num = []
for i in range(n):
    num.append(int(input("please enter num:")))
for i in range(len(num)):
    print("nums are as follows:", num[i])

print(num)
"""


# palindrome
num = 121
string = str(num)
rev_string = string[::-1]
if string == rev_string:
    print("palindrome")

import math
print(math.factorial(3))

fact = 1
for i in range(1,6):
    fact = fact * i
print(fact)


# fact with recursion
n = 5
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
result = fact(n)
print(result)
"""
from turtle import *
speed(1000)
color("cyan")
bgcolor("black")
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
"""


n = 12
for i in range(2,n+1):
    if n % i == 0:
        print(i, end= " ")
print()

for num in range(1, 1001):
    temp = num
    sum = 0
    l = len(str(num))
    while temp > 0:
        remaining = temp % 10
        sum = sum + remaining**l
        temp = temp // 10

    if num == sum:
        print(" given num is armstrong num:", num)

num = 123212
str = str(num)
rev_str = str[::-1]
if str == rev_str:
    print("given num is palindrome")
else:
    print("not palindrome")

a = "madam"
rev_a = "".join(reversed(a))
if a == rev_a:
    print("palindrome")
else:
    print("not palindrome")

num = 12321
temp = num
rev = 0
while temp>0:
    remaining = temp % 10
    rev = (rev*10) + remaining
    temp = temp // 10

if num == rev:
    print("palindrome")
else:
    print("not")



num = "153"
sum = 0
for i in num:
    digit = int(i)**len(num)
    sum = sum + digit
if sum == num:
    print("palindrome")



num = 153
temp = num
times = 0
while temp>0:
    rem = temp % 10
    times = times + 1
    temp = temp // 10

temp = num
sum = 0
while temp>0:
    rem = temp % 10
    sum = sum + rem**times
    temp = temp // 10

if num == sum:
    print("armstrong num")
else:
    print("not armstrong")


num = 121
temp = num
rev = 0
while temp > 0:
    rem  = temp % 10
    rev = rev*10 + rem
    temp = temp // 10

if num == rev:
    print("palindrome")
else:
    print("not palindrome")




















