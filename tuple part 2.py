Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# tuple - part 2

# tuple is immutable, it is impossible to add, remove element from tuple. but we can do delete etire tuple.

# we can create empty tuple.
# tuple can store duplicate values.
# we can create a tuple with single element.
# concantanation is possible with tuple.

# tuple do not support the resizing. append, extend.

# as we know the tuple is immutable in nature. its value contents we cannot be changed once created. but we can unpack the contents of tuple.

# unpacking tuple means splitiing the tuple's contents into individual variables.

tuple = ("pritam", "cradle", "mumbai", 28, "thane", 1994)
tuple
('pritam', 'cradle', 'mumbai', 28, 'thane', 1994)

(a,b,c,d,e,f) = tuple

a
'pritam'
b
'cradle'
c
'mumbai'
d
28
e
'thane'
f
1994

# this is called packing unpacking of tuple.

# another way of unpacking

(x,*y,z) = tuple

x
'pritam'
y
['cradle', 'mumbai', 28, 'thane']
z
1994

# we have used the * with the y variable. hence, y variable contains the elements.

###########33

# tuple is use for a static data. fixed size and know datatype.

# memory efficient than list

###############

# packing of tuple

a= ("p",12,10,"pritam",1994)
a
('p', 12, 10, 'pritam', 1994)

giving the data in single variable is called the packing.
SyntaxError: invalid syntax

(p,q,r,s,t)=a
p
'p'
q
12
r
10
s
'pritam'
t
1994

assigning the no of variables to single tuple is called unpacking...
SyntaxError: invalid syntax

#######

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

# using sum function
tuple3 = sum((tuple1, tuple2), ())
print(tuple3)
# Output (1, 2, 3, 4, 5, 3, 4, 5, 6, 7)
SyntaxError: multiple statements found while compiling a single statement

a
('p', 12, 10, 'pritam', 1994)

a = (10,12,15,16,4)
b = (1,2,3,4,5,6)

c=sum(a,b())
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    c=sum(a,b())
TypeError: 'tuple' object is not callable

c = sum((a,b),())
c
(10, 12, 15, 16, 4, 1, 2, 3, 4, 5, 6)

##################################

# when to use tuple.

# There are no append() or extend() to add items and similarly no remove() or pop() methods to remove items. This ensures that the data is write-protected. As the tuples are Unchangeable, they can be used to represent read-only or fixed data that does not change.
As they are immutable, they can be used as a key for the dictionaries, while lists cannot be used for this purpose.
As they are immutable, the search operation is much faster than the lists. This is because the id of the items remains constant.
Tuples contain heterogeneous (all types) data that offers huge flexibility in data that contains combinations of data types like alphanumeric characters.
SyntaxError: invalid syntax

####

tuple = (10,20,30,40,50)

tuple[-4:-1]
(20, 30, 40)

# -4 is 20 whereas -1 is 50, but as per the positive slicing, last element is inclusive. not considered.

########
tuple = (1120,"a")
max(tuple)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    max(tuple)
TypeError: '>' not supported between instances of 'str' and 'int'

# here we can see max option doesnt support the two datatypes in tuple.

tuple = ("1120","a")
tuple
('1120', 'a')
max(tuple)
'a'

# here 1120 is capsulated in the double quote. hence it becomes the string. and a is also string, hence value of max is a

min(tuple)
'1120'

tuple = (10,120,"a","x","python")
max(tuple)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    max(tuple)
TypeError: '>' not supported between instances of 'str' and 'int'

# different datatype

tuple = ("10","120","a","x","python")
tuple
('10', '120', 'a', 'x', 'python')

max(tuple)
'x'
min(tuple)
'10'

# alphabet having larger values than integers

######################

# nested tuple
tuple = ("Orange", [10, 20, 30], (5, 15, 25))
tuple
('Orange', [10, 20, 30], (5, 15, 25))

tuple[1][1]  # if we want to find the "20"
20

len(tuple)
3

################

tuple = "orange"

type(tuple)
<class 'str'>

tuple = ("orange")
type(tuple)
<class 'str'>

# here python understand the orange as a string.
# to create the single element tuple we have to put the one comma after the element.

tuple = ("orange",)
type(tuple)
<class 'tuple'>

# very very imporatnt

$
SyntaxError: invalid syntax

#
