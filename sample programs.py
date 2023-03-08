Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# sample examples

# Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.

num = int(input("please enter number:"))
please enter number:922

def test(num):
    return num > 4 ** 4 and num % 34 == 4
print("the answer is:", test(num))
SyntaxError: invalid syntax


#############################################

nums = [19, 19, 15, 5, 3, 5, 5, 2]

#write a program with one number occurace 2 times and  one number occures atleast 3 times

def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3
print("the answer is:", test(nums))
SyntaxError: invalid syntax

answer- true
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    answer- true
NameError: name 'answer' is not defined

############################################

#Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list.

nums = [19, 19, 15, 5, 5, 5, 1, 2]

def test(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3
print("the answer is:", test(nums))
SyntaxError: invalid syntax

# answer is True

########################################

# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.

num = int(input("please enter number:"))
please enter number:2

def test(num):
    return [num+2 * i for i in range(num)]
    print("the answer is:", test(num))

    
# ans- [2,4]
# input- 5 ans- [5,7,9,11,13] (total 5 entries)

######################################

# List of integers where the sum of the first i integers is i
nums = [1,1,1,1,1]


def test(nums):
    return all([sum(nums[:i]) == i for i in range(len(nums))])
print(test(nums))

SyntaxError: multiple statements found while compiling a single statement

###################

# whether the given strings are palindromes or not.
# what is palindromes- the word who can write/read straigt and reverse same as iti is. example= mom, eye

string = ['palindrome', 'madamimadam', '', 'foo', 'eyes']


def test(string):
    return [s == s[::-1] for s in string]
print("answer", test(string))
SyntaxError: multiple statements found while compiling a single statement

# answer- [False, True, True, False, False]

######################################

# Strings in the said list starting with a given prefix
strs =  ['cat', 'car', 'fear', 'center']
prefix = "ca"

def test(strs, prefix):
    return [s for s in strs if s.startswith(prefix)]
print(test(strs, prefix))


#######################################
SyntaxError: multiple statements found while compiling a single statement

# to find longest string

string = ['cat', 'dog', 'fear', 'center']

def test(words):
    return max(words, key=len)
print("longest string is", test(word))
SyntaxError: invalid syntax
print("longest string:", test(string))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print("longest string:", test(string))
  File "<pyshell#42>", line 2, in test
    return [num+2 * i for i in range(num)]
TypeError: 'list' object cannot be interpreted as an integer

def test(words):
    return  max(words, key=len)
strs =  ['cat', 'car', 'fear', 'center']
print("Original strings:")
print(strs)
print("Longest string of the said list of strings:")
print(test(strs))
SyntaxError: invalid syntax

##############################

# find the length of list

list = ['cat', 'car', 'fear', 'center']

def test(list)
SyntaxError: expected ':'

def test(list):
    return [*map(len, list)]
print("lenght is:", test(list))
SyntaxError: invalid syntax
# lenght is: [3, 3, 4, 6]

#####################################

list= ['100','102.1','101.2']

max(list)
'102.1'

################
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if x % 2:
    	     count_odd+=1
        else:
    	     count_even+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

SyntaxError: multiple statements found while compiling a single statement
##############

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]

datalist
[1452, 11.23, (1+2j), True, 'w3resource', (0, -1), [5, 12], {'class': 'V', 'section': 'A'}]

for item in datalist:
    print("type of", item "is", type(item))
    
SyntaxError: invalid syntax

for item in datalist:
        print("type of",item,"is", type(item))

        
type of 1452 is <class 'int'>
type of 11.23 is <class 'float'>
type of (1+2j) is <class 'complex'>
type of True is <class 'bool'>
type of w3resource is <class 'str'>
type of (0, -1) is <class 'tuple'>
type of [5, 12] is <class 'list'>
type of {'class': 'V', 'section': 'A'} is <class 'dict'>

for item in datalist:
    print("type of", item, "is", type(item))

    
type of 1452 is <class 'int'>
type of 11.23 is <class 'float'>
type of (1+2j) is <class 'complex'>
type of True is <class 'bool'>
type of w3resource is <class 'str'>
type of (0, -1) is <class 'tuple'>
type of [5, 12] is <class 'list'>
type of {'class': 'V', 'section': 'A'} is <class 'dict'>

############

color = {"c1": "Red", "c2": "Green", "c3": "Orange"}

for key in color:
    print("key is:")

    
key is:
key is:
key is:

for key in color:
    print("key is:", key)

    
key is: c1
key is: c2
key is: c3

for item in color:
    print("item in color is:", item)

    
item in color is: c1
item in color is: c2
item in color is: c3

for value in color.values():
    print("value is:", value)

    
value is: Red
value is: Green
value is: Orange

#############################

list = [10,15,16,128,20]

middle_index= len(list) // 2

middle_index
2

first_half = [:middle_index]
SyntaxError: invalid syntax
first_half = list[:middle_index]
print(first_half)
[10, 15]
last_half = list[middle_index:]
last_half
[16, 128, 20]

############

s='hi, this is pritam, an engineer, mechanical wala'
s
'hi, this is pritam, an engineer, mechanical wala'
s.split()
['hi,', 'this', 'is', 'pritam,', 'an', 'engineer,', 'mechanical', 'wala']
s.split(",")
['hi', ' this is pritam', ' an engineer', ' mechanical wala']
###########