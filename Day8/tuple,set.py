Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1)
t
(1, 1, 1, 1)
t=(1,1.1,'tryu',[])
t
(1, 1.1, 'tryu', [])
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
h=(90,80,70)
t+h
(10, 20, 30, 40, 50, 90, 80, 70)
t*h
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t*h
TypeError: can't multiply sequence by non-int of type 'tuple'
t*h
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t*h
TypeError: can't multiply sequence by non-int of type 'tuple'
t*4
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t
(10, 20, 30, 40, 50)
t[2]
30
t[3]
40
t[-2]
40
t[-1]
50
t
(10, 20, 30, 40, 50)
t[1]
20
t[4]
50
t[2]
30
t[1]
20
t[:3]
(10, 20, 30)
t[3:]
(40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[-1:]
(50,)
t[-1]
50
t[-1:-4:-1]
(50, 40, 30)
t[-1:-3]
()
t[-1:-3:]
()
t[-3:]
(30, 40, 50)
t
(10, 20, 30, 40, 50)
10 in t
True
30 in t
True
60 in t
False
10 in not t
SyntaxError: invalid syntax
t
(10, 20, 30, 40, 50)
len(t)
5
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
sum(t)
150
t.count(10)
1
t.index(10)
0
>>> t=1,2,3,4,5,6,7
>>> t
(1, 2, 3, 4, 5, 6, 7)
>>> a,b,c=(1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> a=(1,2,4)
>>> a
(1, 2, 4)
>>> x,y,z=a
>>> x
1
>>> y
2
>>> z
4
>>> t=(1,2,3,[4,5,6],7,8)
>>> t
(1, 2, 3, [4, 5, 6], 7, 8)
>>> t[2]
3
>>> t[4]
7
>>> t[3]
[4, 5, 6]
>>> t[3]
[4, 5, 6]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
>>>  s=set()
...  
SyntaxError: unexpected indent
>>> s={1,1,1,1,1}
>>> s
{1}
s={987,654,345,56,345,1,2,34}
 s={987,654,345,56,345,1,2,345,1,2,34,6,56}
s
SyntaxError: unexpected indent
s
{1, 2, 34, 56, 345, 987, 654}
s=set()
s
set()
s.add(1)
s
{1}
s.add(150.15)
s
{1, 150.15}
s.add("Hemanth")
s
{1, 150.15, 'Hemanth'}
s.add(True)
s
{1, 150.15, 'Hemanth'}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add{1,2,3,4}
SyntaxError: invalid syntax
s.add((1,2,3,4))
s
{(1, 2, 3, 4), 1, 150.15, 'Hemanth'}
s.add({1:2,2:1})
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s.add({1:2,2:1})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s
{(1, 2, 3, 4), 1, 150.15, 'Hemanth'}
l in s
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    l in s
NameError: name 'l' is not defined
1 in s
True
2 in s
False
False not in s
True
a ={1,2,3,5,6,8,10}
b={6,7,8,9}
a | b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{8, 6}
a & b
{8, 6}
a - b
{1, 2, 3, 5, 10}
a ^ b
{1, 2, 3, 5, 7, 9, 10}
# {1} {2} {3} {5} {1,3} {1,2} {8,10}
a <= {1}
False
a >= {1}
True
 a <= {1,2,3,4,5,6,8,10,11,12}
 
SyntaxError: unexpected indent
 a <= {1,2,3,4,5,6,8,10,11,12}
 
SyntaxError: unexpected indent
a <= {1,2,3,4,5,6,8,10,11,12}
True
a >= {6,10,8}
True
a
{1, 2, 3, 5, 6, 8, 10}
b
{8, 9, 6, 7}
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a
{1, 2, 3, 5, 6, 8, 10}
a.add(17)
a
{1, 2, 3, 17, 5, 6, 8, 10}
a.update({11,12,13})
a
{1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 17}
a.pop()
1
a.pop()
2
a.remove(17)
a
{3, 5, 6, 8, 10, 11, 12, 13}
a.remove(10)
a
{3, 5, 6, 8, 11, 12, 13}
 a.discard(6)
 
SyntaxError: unexpected indent
a.discard(6)
a
{3, 5, 8, 11, 12, 13}
a.discard(3)
a
{5, 8, 11, 12, 13}
b
{8, 9, 6, 7}
a.intersection_update(b)
a
{8}
b
{8, 9, 6, 7}
c=b
c.add(12)
c
{6, 7, 8, 9, 12}
{8, 9, 6, 7}
{8, 9, 6, 7}
b
{6, 7, 8, 9, 12}
d=c.copy()
d.add(10)
d
{6, 7, 8, 9, 10, 12}
c
{6, 7, 8, 9, 12}
len(c)
5
min(c)
6
max(c)
12
sum(c)
42
sorted(c)
[6, 7, 8, 9, 12]
