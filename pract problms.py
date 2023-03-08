# practice probelm

# fiboncii nums
a = 0
b = 1
c = 0
for i in range(1, 15):
    print(c, end=" ")
    a = b
    b = c
    c = a + b
    
a = 0
b = 1
c = 0
n = 5
for i in range(0, n):
    print(c, end=" ")
    a = b
    b = c
    c = a + b
   
print()

# we can use recursion

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        for i in range(0, n):
            c = a + b
            a = b
            b = c
            print(c, end=" ")
result = fib(10)
print(result)
            
n = 101
if n%2 == 0:
    print("even")
else:
    print("odd")

# area of trinagle
a = 4.0
b = 3.0
c = 6.0

s = (a+b+c)/2
import math
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)

# avg of integers
a = int(input("enter entries:"))
num = []
for i in range(a):
    num.append(int(input("please enter num:")))
for i in range(len(num)):
    print(i[1], num[i])

total = sum(num)
avg = total/len(num)
print(avg)

