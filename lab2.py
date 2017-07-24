Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=5
>>> b=10
>>> a=b
>>> b=a
>>> a
10
>>> b
10
>>> a=5
>>> b=10
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
5
>>> four='4'
>>> print(four*3)
444
>>> five=4
>>> print(five*3)
12
>>> my_name = 'students'
>>> print("hi," + myName')
      
SyntaxError: EOL while scanning string literal
>>> print("Hi, "+my_name)
Hi, students
>>> my_age = 15
>>> print('I am'+my_age+'years old')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print('I am'+my_age+'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> my_age = '15'
>>> print('I am ' + my_age + 'years old')
I am 15years old
>>> score = 1
>>> total=score+(count*2)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    total=score+(count*2)
NameError: name 'count' is not defined
>>> print(total)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(total)
NameError: name 'total' is not defined
>>> count=5
>>> score=1
>>> total=score+(count*2)
>>> print(total)
11
>>> 
