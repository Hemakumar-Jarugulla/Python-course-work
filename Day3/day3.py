Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
t=999.999
type(a)
<class 'int'>
type(t)
<class 'float'>
c=9
t=i+j
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t=i+j
NameError: name 'i' is not defined. Did you mean: 'id'?
t=8+j
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t=8+j
NameError: name 'j' is not defined
c=12+8j
type(c)
<class 'complex'>
s="Hello"
type(s)
<class 'str'>
l=[1,2,3,4]
id(l)
2165444221184
l.append(50)
l.append(60)
l
[1, 2, 3, 4, 50, 60]
id(l)
2165444221184
l
[1, 2, 3, 4, 50, 60]
s={1,2,3,4,5,6}
type(s)
<class 'set'>
s=set()
s={45678,546,3456,13423}
a
10
s
{3456, 546, 45678, 13423}
s={1,1,1,1,1,1,4}
s
{1, 4}
d={'name':'abc':'age':100,'course':'PFS'}
SyntaxError: invalid syntax
>>> d={'name':'abc','age':100,'course':'PFS'}
>>> d
{'name': 'abc', 'age': 100, 'course': 'PFS'}
>>> type(d)
<class 'dict'>
>>> status=True
>>> status=False
>>>  l=[]
...  
SyntaxError: unexpected indent
>>> t=()
>>> t=(1,2,34,5,6,67)
>>> t
(1, 2, 34, 5, 6, 67)
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> l=['post1.png','reel1.mp4']
>>> l
['post1.png', 'reel1.mp4']
>>> t=()
... t=(1,2,34,5,6,67)
... t
... (1, 2, 34, 5, 6, 67)
SyntaxError: multiple statements found while compiling a single statement
>>> type(t)
<class 'tuple'>
>>> status=True
... status=False
SyntaxError: multiple statements found while compiling a single statement
>>> type(status)
<class 'bool'>
>>> a=None
>>> type(a)
<class 'NoneType'>
