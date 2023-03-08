Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

# string - part 2

# strings are immutable.

# The String is immutable, so its value cannot be changed. If the String doesn't remain immutable, any hacker can cause a security issue in the application by changing the reference value. The String is safe for multithreading because of its immutableness.

# Once String object is created its data or state can't be changed but a new String object is created.

# you cannot modify the string once created. If you change a string, Python creates a new string with the updated value and assigns it to the variable.

a = 'pritam'
b = str('pritam')

a == b
True

a is b
True

id(a)
2306738679984

id(b)
2306738679984

str1 = "my isname isisis jameis isis bond";
sub = "is";

print(str1.count("is", 4))
6
6
6

# here syntax of string is :
# syntax of count is: count("charachter which needs to be count", index start, index end)
# if nothing is given then python take whole string to find

# above example, is needs to be count after 4th index hence count is 6

# a = "pritam"
b = ["abc","pritam","xyz"]

a == b
False

a == b[1]
True

a is b[1]
True

id(b[1])
1876118238128

id(a)
1876118238128
SyntaxError: multiple statements found while compiling a single statement

## function to get the ASCII code of a character- ord()
## function to get the character from ASCII number- char(number)
## function to get the ASCII code of a character- ord()
# ## function to get the ASCII code of a character- ord('charachter')

a = 'python
SyntaxError: unterminated string literal (detected at line 1)

a='python'
b='ptyhon'

a

a > b
True

a < b
False

### it operates on max of charachters..

### it operates on max of charachters..

###

# partition() - to perform partition in string.

# partition is same as split option. split gives the output in list format. whereas the partiton gives the o/p in tuple with only 3 element.

a = "my name is pritam and i am an engineer"
a
'my name is pritam and i am an engineer'

a.split()
['my', 'name', 'is', 'pritam', 'and', 'i', 'am', 'an', 'engineer']

# split gives the number of elements of list equal to the words involved in the list.

a.partition("and")
('my name is pritam ', 'and', ' i am an engineer')

# partition gives the tuple of 3 element.. in which 1st is before the separator 2nd separator itself and 3rd is after the separator.

# split will give the list of string at each occurance of delimiter.
# if delimiter(separator) not mentioned, it will split the string based on white spaces.

# partition split the string at first occurance of delimiter.
# if delimiter not mentioned then it will return the Typeerror.

a
'my name is pritam and i am an engineer'

a = "hi, i am pritam and i am engineer"
SyntaxError: unexpected indent
a = ("hi, i am pritam and i am engineer")
a
'hi, i am pritam and i am engineer'

a.split("am")
['hi, i ', ' prit', ' and i ', ' engineer']
a.split(",")
['hi', ' i am pritam and i am engineer']

a.partition("am")
('hi, i ', 'am', ' pritam and i am engineer')
('hi, i ', 'am', ' pritam and i am engineer')
('hi, i ', 'am', ' pritam and i am engineer')
# here am is the separator - 3 tuples - before separator , separator, after separator.
# am occurace two times. but python considered only 1st occurance.

# rpartition- this is same as partition. it takes the occurance from right side. last occurannce considered.

a = ("i am pritam and i am engineer and mechanic")
a
'i am pritam and i am engineer and mechanic'

a.rpartition("and")
('i am pritam and i am engineer ', 'and', ' mechanic')

# here two occrance of and. rpartition considered the second and and split the string.

# Zfill() - to add the 000 "zeros" at the start of string, from left side.

a = "pritam"

a.zfill()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a.zfill()
TypeError: str.zfill() takes exactly one argument (0 given)

# syantax- same as center, we need to provide the width of string

a.zfill(10)
'0000pritam'

###########

# rsplit- split the string from right side
# The only difference between split() and rsplit() is the use of the maxsplit argument. If the maxsplit argument is set, the rsplit() function splits a string from the right side (from the final character), whereas the split() method splits from the left side (from the first character).

a = "'i am pritam and i am engineer and mechanic'"
a
"'i am pritam and i am engineer and mechanic'"
a.split()
["'i", 'am', 'pritam', 'and', 'i', 'am', 'engineer', 'and', "mechanic'"]
a.rsplit()
["'i", 'am', 'pritam', 'and', 'i', 'am', 'engineer', 'and', "mechanic'"]
a.partition()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    a.partition()
TypeError: str.partition() takes exactly one argument (0 given)
a.partition("and")
("'i am pritam ", 'and', " i am engineer and mechanic'")
a.rpartition("and")
("'i am pritam and i am engineer ", 'and', " mechanic'")

a.split("and")
["'i am pritam ", ' i am engineer ', " mechanic'"]
a.rsplit("and")
["'i am pritam ", ' i am engineer ', " mechanic'"]

# splitlines() - use to perform the split the lines.

a= 'i am pritam\n i am engineer\n and mechanic'
a
'i am pritam\n i am engineer\n and mechanic'

a.splitlines()
['i am pritam', ' i am engineer', ' and mechanic']

# it split the line in \n at new line.


### getting the size of string

import sys
a = 'i am pritam and i am engineer and mechanic'
sys.getsizeof(a)
91

###################