Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


### Set

#  set is collection of items like tuple, list and dictionary
#
# every set elemnt is unique (no duplication allowed)
# set is immutable

## set is mutable- we can add or remove data in set

# set has no any syntax, but normally we use curly braces to express the set

#empty {} are dictionary, to show empty set er can use set()

a={}

a
{}

type(a)
<class 'dict'>

a= set()

a
set()

type(a)
<class 'set'>


a= {10,15,10,23,555}

type(a)
<class 'set'>

a= {78,2.3,566,6.6}
type(a)
<class 'set'>

a={'pritam', 55, 1.5}
type(a)
<class 'set'>

#Sets are mutable. However, since they are unordered, indexing has no meaning.

#We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.

# in set duplicate entries are not allowed.

set= {10,1,15,10,5,6}
set
{1, 5, 6, 10, 15}

set
{1, 5, 6, 10, 15}

len(set)
5


# indexing and slicing not possible in set

# methods
# add()
set.add(123)
set
{1, 5, 6, 10, 123, 15}

# update- if multiple objects needs to be added

set.update(45,18,6)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    set.update(45,18,6)
TypeError: 'int' object is not iterable

set.update(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    set.update(1,2,3,4)
TypeError: 'int' object is not iterable

set.update([12,15,16,18])

set
{1, 5, 6, 10, 12, 15, 16, 18, 123}

# to update we have to either use list or tuple form

##Removing methods
# discard and remove

#discard

set
{1, 5, 6, 10, 12, 15, 16, 18, 123}

set.discard(123)

set
{1, 5, 6, 10, 12, 15, 16, 18}

set
{1, 5, 6, 10, 12, 15, 16, 18}

# remove
set.remove(18)

set
{1, 5, 6, 10, 12, 15, 16}

set.discard()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    set.discard()
TypeError: set.discard() takes exactly one argument (0 given)

set.remove()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    set.remove()
TypeError: set.remove() takes exactly one argument (0 given)

# both discard and remove requires atleast one argument.

set.discard(100)

set
{1, 5, 6, 10, 12, 15, 16}

## difference between dicard and remove
# when unkonwn elemnt entered in argument for remove or discard purpose. discard will return none that is program can run further but remove gives the error.

set.remove(100)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    set.remove(100)
KeyError: 100

# remove gives the key error.

# we can use pop method to remove element. but set is unordeed so thre willbe poped aribarty selected

set
{1, 5, 6, 10, 12, 15, 16}

set.pop(10)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    set.pop(10)
TypeError: set.pop() takes no arguments (1 given)

set.pop()
1

set
{5, 6, 10, 12, 15, 16}

set.pop()
5

# pop doenst take any argument.. and poped out any number from the set.
# usually removes the 1st value..

## clear.

# if we want to clear alll set then we can use clear3

set.clear()

set
set()

# o/p is blank set

######## set opertions
# Union- 123456,56789= 123456789
# intersection- common in both
# difference- a-b = 123456-56789= 1234
# difference- b-a = 123456-56789= 789
# symmetric difference- a-b = 123456-56789= 56
# symmetric difference- b-a = 123456-56789= 56

a= {1,2,3,4,5,6}
b= {5,6,7,8,9,10}

a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# union takes all the entries but no repitation.. use (|)
# syntax- |

a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# intersection

a & b
{5, 6}

# intersection  takes only common values..
# syntax- &

# difference - it gives difference between two sets.
# if a-b then uncommon from set 1 gives the o/p

a - b
{1, 2, 3, 4}

# if b-a then it gives the o/p uncommon values from set 2

b - a
{8, 9, 10, 7}

# symetric difference- it returns the symenttic difference.

a ^ b
{1, 2, 3, 4, 7, 8, 9, 10}

# common values are eliminate

b ^ a
{1, 2, 3, 4, 7, 8, 9, 10}


## python methods

# add

set
set()

set= {10,15,1,19,6,30,55,64,76,85}

set.add(100)

set
{64, 1, 100, 6, 10, 76, 15, 19, 85, 55, 30}

# copy
set.copy()
{64, 1, 100, 6, 10, 76, 15, 19, 85, 55, 30}

set
{64, 1, 100, 6, 10, 76, 15, 19, 85, 55, 30}

# in copy. shallow copy has been done

## difference

set1= {23,15,6,89,63,85,30}

set.difference(set1)
{64, 1, 100, 10, 76, 19, 55}

set
{64, 1, 100, 6, 10, 76, 15, 19, 85, 55, 30}
set1
{85, 6, 23, 89, 63, 30, 15}

set1.difference(set)
{89, 63, 23}

## difference update

set.difference_update(set1)

set
{64, 1, 100, 10, 76, 19, 55}

#inplace output


# difference_update- this is inplace o/p. it gives the difference between two set but with wrt 1st set.

## discard
set.discard(100)
set
{64, 1, 10, 76, 19, 55}

set.discard(60)

set
{64, 1, 10, 76, 19, 55}

# if unknown value given in argumnet then it showns the none

#intersection

set.intersection(set1)
set()

set
{64, 1, 10, 76, 19, 55}

set1
{85, 6, 23, 89, 63, 30, 15}

# when nothing is intersected or common in set 1 and set 1 then it return the none..

# if something is common then it return the common values

set2= {85,16,98}

set.intersect(set2)
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    set.intersect(set2)
AttributeError: 'set' object has no attribute 'intersect'. Did you mean: 'intersection'?

set.intersection(set2)
set()

set
{64, 1, 10, 76, 19, 55}
set2
{16, 98, 85}

set1.intersection(set2)
{85}

# it returns the common value otherwise blank

# intersection_update

# this method update the intersection and gives the o/p

set1.intersection_update(set2)

set1
{85}

set2
{16, 98, 85}

# intersection_update - updates the set with new set but with same name.


## isdisjoint

set1.isdisjoint(set)
True

set1
{85}
set
{64, 1, 10, 76, 19, 55}

# output is true, beacuase there is no any intersection between set1 and set. nothing is common.

set3= {60,15,16,36,55,10}

set.isdisjoint(set3)
False

# isdisjoint- it gives the false if any item is common in both the sets.

# issubset-

set.issubset(set3)
False

set1.issubset(set2)
True

set1.issubset(set3)
False

# it gives the True if the one set consist the another set

set1.issubset(set2)
True
set1
{85}
set2
{16, 98, 85}
set2.issubset(set1)
False

# in 1st case, output is true beacuse value of set1 (85) purely consiting in set2 (85,16,98)
# in 2nd case all values of set2 (85,16,98) doenst consiting in set1 (85)...thats why o/p is false


# issuperset

set1
{85}
set2
{16, 98, 85}

set1.issuperset(set2)
False

set2.issuperset(set1)
True

# this is vice versa of above statment. that is this set contacins the another set..

# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set

# pop- use for the removing purpose. it never takes the argumant
# syntax- set.pop()

set.pop()
64

set
{1, 10, 76, 19, 55}

set2
{16, 98, 85}

set2.pop()
16

# it always returns the 1st value. it returns the arbitary value

# inpalce method

# remove
# it removes the object from set

set2.remove()
Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    set2.remove()
TypeError: set.remove() takes exactly one argument (0 given)

set2.remove(85)

set2
{98}

# argument must be the item in set


### symmetric difference

set
{1, 10, 76, 19, 55}
set2
{98}

set1
{85}
set3
{16, 36, 55, 10, 60, 15}

set1.symmetric_difference(set3)
{16, 36, 85, 55, 10, 60, 15}

set.symmetric_difference(set3)
{1, 76, 15, 16, 19, 36, 60}

set
{1, 10, 76, 19, 55}
set3
{16, 36, 55, 10, 60, 15}

# symmetric diffrence= all uncommon items will appper

# symmetric_diffrence_update

# uodates the set

set.symmetric_difference_update(set3)

set
{1, 36, 76, 15, 16, 19, 60}
set3
{16, 36, 55, 10, 60, 15}

### union= common

set
{1, 36, 76, 15, 16, 19, 60}
set1
{85}
set2
{98}
set3
{16, 36, 55, 10, 60, 15}

set.union(set3)
{1, 36, 10, 76, 15, 16, 19, 55, 60}

set
{1, 36, 76, 15, 16, 19, 60}
set3
{16, 36, 55, 10, 60, 15}

set.intersection(set3)
{16, 36, 60, 15}

# union- if values are common in both the sets then it will take one show both the set values in single set

## update

set
{1, 36, 76, 15, 16, 19, 60}
set.update(100)
Traceback (most recent call last):
  File "<pyshell#378>", line 1, in <module>
    set.update(100)
TypeError: 'int' object is not iterable

set.update(1)
Traceback (most recent call last):
  File "<pyshell#380>", line 1, in <module>
    set.update(1)
TypeError: 'int' object is not iterable


#######

other set operation
SyntaxError: invalid syntax

#membership

set
{1, 36, 76, 15, 16, 19, 60}

15 in set
True

6 in set
False


#### iterating  values
set
{1, 36, 76, 15, 16, 19, 60}

for i in set:
    print("the values from set is:")

    
the values from set is:
the values from set is:
the values from set is:
the values from set is:
the values from set is:
the values from set is:
the values from set is:

for i in set:
    print("the values from set:", i)

    
the values from set: 1
the values from set: 36
the values from set: 76
the values from set: 15
the values from set: 16
the values from set: 19
the values from set: 60

for i in set:
    sum= i+i
    print("the value of sum is:", sum)

    
the value of sum is: 2
the value of sum is: 72
the value of sum is: 152
the value of sum is: 30
the value of sum is: 32
the value of sum is: 38
the value of sum is: 120


## built in function

set.all()
Traceback (most recent call last):
  File "<pyshell#414>", line 1, in <module>
    set.all()
AttributeError: 'set' object has no attribute 'all'

all(set)
True

set
{1, 36, 76, 15, 16, 19, 60}

# if all values are true then it return the true. if set is blank then it returns the true

set
{1, 36, 76, 15, 16, 19, 60}

all(set)
True

any(set)
True

# any- if any value is true then it returns the true

# len
len(set)
7

# max
max(set)
76

min(set)
1

sum(set)
Traceback (most recent call last):
  File "<pyshell#438>", line 1, in <module>
    sum(set)
TypeError: 'int' object is not callable

enumerate(set)
<enumerate object at 0x0000022478FAECC0>

sorted(set)
[1, 15, 16, 19, 36, 60, 76]

sorted(set, reverse=True)
[76, 60, 36, 19, 16, 15, 1]

sum(set)
Traceback (most recent call last):
  File "<pyshell#446>", line 1, in <module>
    sum(set)
TypeError: 'int' object is not callable

sum('set')
Traceback (most recent call last):
  File "<pyshell#448>", line 1, in <module>
    sum('set')
TypeError: 'int' object is not callable


####################

''' Python Frozenset
Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.

Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.

Frozensets can be created using the frozenset() function.

This data type supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable, it does not have methods that add or remove elements. '''
" Python Frozenset\nFrozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.\n\nSets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.\n\nFrozensets can be created using the frozenset() function.\n\nThis data type supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable, it does not have methods that add or remove elements. "


