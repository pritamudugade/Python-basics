
for i in range(0,6):
    print(chr(64+i)*i)


num = 121
a = str(num)
b = "".join(reversed(a))
print(a)
print(b)

if a == b:
    print("palindrome")
else:
    print("not")

# other method

num = 121
a = str(num)
b = a[::-1]

if a == b:
    print("palindrome")
else:
    print("not")

num = 1211
temp = num
reverse = 0
while temp > 0:
    rem = temp % 10
    reverse = reverse*10 + rem
    temp =temp // 10

if num == reverse:
    print("palindrome")
else:
    print("not")

a = 123456
print(len(str(a)))

temp = a
n = 0
while temp>0:
    rem = rem % 10
    n = n + 1
    temp = temp // 10

print(n)
    

    
for num in range(1,1000):   
    temp = num
    n = len(str(num))
    sum = 0

    while temp > 0:
        rem = temp % 10
        sum = sum + rem**n
        temp = temp // 10

    if num == sum:
        print("armstrong num:", num)


num = 6
for i in range(num):
    for j in range(num-i-1):             # 6-1-1 = 5 spaces
        print(end=" ")                   # for printing spaces
    for j in range(i+1):                 # 0+1 = 1 star
        print("*", end=" ")              # for priting *
    print()


a = 0
b = 1
c = 0
for i in range(15):
    print(c, end=" ")
    a = b
    b = c
    c = a + b

print()

num = 5
fact = 1
for i in range(1, num+1):
    fact = fact * i
print("factorial of given num:", fact)


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)             # recursion- function calls itself

print(fact(5))

from math import factorial as f
print(f(5))

num = 5
fact = 1
while num > 0:
    fact = fact * num
    num = num - 1
print(fact)

n = 5

for i in range(1,11):
    table = n * i
    print("mul table:", table)


for num in range(1,1000):
    temp = num
    sum = 0
    n = len(str(num))
    while temp > 0:
        rem = temp % 10
        sum = sum + rem**n
        temp = temp // 10
    if num == sum:
        print("armstrong num:", sum)

sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)

sum = 0
num = 100
while num>=0:
    sum = sum + num
    num = num - 1
print(sum)


num = 10          # bydefault number in decimal
# binary
a = bin(num)
print(a)

b = hex(num)
print(b)

from math import factorial as f
print(f(6))

num = 6
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(fact)

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))


num = 5
fact = 1
for i in range(1, num+1):
    fact = fact * i
print("factorial of given num:", fact)

num = 6
fact = 1
while num > 0:
    fact = fact * num
    num = num - 1
print(fact)


a = [10,20,30,40]
sum = 0
for i in a:
    sum = sum + i
print(sum)




import random
a = random.random()
print(a)

    
    
