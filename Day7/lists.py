Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='     hello     world   '
s
'     hello     world   '
s.strip()
'hello     world'
s.lstrip()
'hello     world   '
s.rstrip()
'     hello     world'
 s='strings.py'
 
SyntaxError: unexpected indent
s='strings.py'
s
'strings.py'
s.startswith('str')
True
s.startswith('gfh')
False
s.endswith('py')
True
s.endswith('js')
False
'sdfyui'.isalpha()
True
 'DSFGHJdftrryghjutyghj'.isalpha()
 
SyntaxError: unexpected indent
'DSFGHJdftrryghjutyghj'.isalpha()
True
'abcde12345'.isalnum()
True
'345678sdfghb'.isalnum()
True
'ewrtyuii'.islower()
True
'dfghj345678@#$%^&&'.islower()
True
'ADFGH#$%^65789'.isupper()
True
' '.isspace()
True
'hello       '.isspace()
False
'Hema Nth'.istitle()
True
'sek Har'.istitle()
False
'py_python'.isidentifier()
True
'py@123'.isidentifier()
False
 l=[]
 
SyntaxError: unexpected indent
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3,4]
m=[5,6,7,8]
l+m
[1, 2, 3, 4, 5, 6, 7, 8]
 l*4
 
SyntaxError: unexpected indent
l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l=[10,20,30,40,50]
l[4]
50
l[3]
40
l[2]
30
l[::-1]
[50, 40, 30, 20, 10]
l[-1:-4:-1]
[50, 40, 30]
l[::1]
[10, 20, 30, 40, 50]
l[1:5:2]
[20, 40]
l[1:4]
[20, 30, 40]
l[-3::-1]
[30, 20, 10]
l
[10, 20, 30, 40, 50]
20 in l
True
40 in l
True
70 not in l
True
80 in l
False
10 in l
True
 l[1]=70
 
SyntaxError: unexpected indent
l=[10,70,30,40,50]
l[1]=70
l
[10, 70, 30, 40, 50]
id(l)
3124666985408
l[4]=100
l
[10, 70, 30, 40, 100]
l.append(120)
l
[10, 70, 30, 40, 100, 120]
l.append(400)
l
[10, 70, 30, 40, 100, 120, 400]
l.insert(4,10)
l
[10, 70, 30, 40, 10, 100, 120, 400]
l.insert(4,50)
l
[10, 70, 30, 40, 50, 10, 100, 120, 400]
l.extend([80,90,110])
l
[10, 70, 30, 40, 50, 10, 100, 120, 400, 80, 90, 110]
l.pop()
110
l
[10, 70, 30, 40, 50, 10, 100, 120, 400, 80, 90]
l.pop(90)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    l.pop(90)
IndexError: pop index out of range
l.pop()
90
l
[10, 70, 30, 40, 50, 10, 100, 120, 400, 80]
l.pop()
80
l
[10, 70, 30, 40, 50, 10, 100, 120, 400]
l.pop(3)
40
l
[10, 70, 30, 50, 10, 100, 120, 400]
del 1[1]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    del 1[1]
TypeError: 'int' object does not support item deletion
l
[10, 70, 30, 50, 10, 100, 120, 400]
del l[1]
i
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    i
NameError: name 'i' is not defined. Did you mean: 'id'?
del l[1]
l
[10, 50, 10, 100, 120, 400]
del l[2]
l
[10, 50, 100, 120, 400]
l.clear()
[]
[]
l=[200,30,33,42,10,70,50,40,100,120,400]
sorted(l)
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
l
[200, 30, 33, 42, 10, 70, 50, 40, 100, 120, 400]
sorted(l)
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> l.sort()
>>> l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> min(l)
10
>>> max(l)
400
>>> l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> l.reverse()
>>> l
[400, 200, 120, 100, 70, 50, 42, 40, 33, 30, 10]
>>> l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> sorted(l,reverse=True)
[400, 200, 120, 100, 70, 50, 42, 40, 33, 30, 10]
>>> l
[400, 200, 120, 100, 70, 50, 42, 40, 33, 30, 10]
>>> l.index(120)
2
>>> l.index(50)
5
>>> l.count(30)
1
>>> l
[400, 200, 120, 100, 70, 50, 42, 40, 33, 30, 10]
>>> len(l)
11
>>> sum(l)
1095
>>> # 0 0.0 '' [] {} () set() False
>>> any([1,2,4,5,5,0,0,0,0,0])
True
>>> all([1,2,4,5,5,0,0,0,0,0])
False
