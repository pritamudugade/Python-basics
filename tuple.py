Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


.


#Tuple


#background data structure of tuple is ARRAY

# tuple is immutable.-- not able to change--add/remove/modify

#can be sliced, concatenated, and indexed..
#starts with 0 and ends n-1
#comma separated values in sequence. opetinally we can put those data in parenthesis
SyntaxError: invalid syntax

#Delete opetion like list

a=10,12,161,89

a
(10, 12, 161, 89)

del a

a
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a
NameError: name 'a' is not defined

#delete all the data from a tuple


tuple= (10,15,16,18,1920,12,45,62)

#len like list

len(tuple)
8

#concatenate

a=10,15116,62

a

a
(10, 15116, 62)

b=tuple+a

b
(10, 15, 16, 18, 1920, 12, 45, 62, 10, 15116, 62)

#repitation
a*3
(10, 15116, 62, 10, 15116, 62, 10, 15116, 62)

#membership

3 in a
False

62 in b
True

15 in tuple
True


#builtin functions same like list
#length of tuple

len(tuple)
8

len(a)
3

len(b)
11

#maximu

max(tuple)
1920
max(a)
15116
max(b)
15116

#minimum

min(tuple)
10
min(a)
10
min(b)
10

#conversion-- typecasting
#we can convert the string and list into the tuple

x= ("python")

x
'python'

tuple(x)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    tuple(x)
TypeError: 'tuple' object is not callable

#FOR CONVERSION ----tuple(string/list)


#iteration

tuple
(10, 15, 16, 18, 1920, 12, 45, 62)

for i in tuple:
    print("value of i is:", i)

    
value of i is: 10
value of i is: 15
value of i is: 16
value of i is: 18
value of i is: 1920
value of i is: 12
value of i is: 45
value of i is: 62

#this is called iteration.. that is taking a single value from tuple and iterate the same.

dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


#count and index-- are only 2 methods of tuple...

tuple
(10, 15, 16, 18, 1920, 12, 45, 62)

tuple.count(15)
1

a
(10, 15116, 62)

b
(10, 15, 16, 18, 1920, 12, 45, 62, 10, 15116, 62)

b.count(10)
2

a.count(15)
0

#count-- if value/object/element is not rpresent in tuple then it gives o/p as "0" zero...

#index

tuple
(10, 15, 16, 18, 1920, 12, 45, 62)

tuple.index(45)
6

tuple.index(11)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    tuple.index(11)
ValueError: tuple.index(x): x not in tuple

#if elememt is not avaiable in tuple then it gives the value error.. x not in tuple

#slicing and indexing

tuple
(10, 15, 16, 18, 1920, 12, 45, 62)

tuple[]
SyntaxError: invalid syntax

tuple[:]
(10, 15, 16, 18, 1920, 12, 45, 62)

tuple[5]
12

tuple[:100]
(10, 15, 16, 18, 1920, 12, 45, 62)

#in slicing end index number is more than length of tuple then full tuple shows in result....

tuple[-6]
16

tuple[::-1]
(62, 45, 12, 1920, 18, 16, 15, 10)

tuple.reverse()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    tuple.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'

tuple[2:7]
(16, 18, 1920, 12, 45)

tuple[3:6]
(18, 1920, 12)


############################