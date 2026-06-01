Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
a//b
2
9//2
4
a**2
400
6**3
216
a5b
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a5b
NameError: name 'a5b' is not defined
a%b
0
17%4
1
17%3
2
a>b
True
a<=b
False
10<=b
True
a>=b
True
a==b
False
a!=b
True
y=5
y
5
y=y+10
y
15
y=y+5
y
20
20y
SyntaxError: invalid decimal literal
y=5
y
5
y=y+5
y
10
y=y+10
y
20
y+=10
y
30
y-=10
y
20
y*=10
y
200
y/=10
y
20.0
y//=20
y
1.0
y%=2
y
1.0
y+=10
y
11.0
y/=2
y
5.5
y
5.5
a
20
b
10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 or b%20==0 or a<b
True
a%22==0 or b%20==0 or a<b
False
not a>b
False
 #str,list,tuple,set,dict
a= 'python Programming'
a
'python Programming'
'y' in a
True
'g' in a
True
'z' not in a
True
'r' not in a
False
l=['java','Python','mysql','c++','c','html']
'mysql' in l
True
'python' in l
False
'Python' in l
True
'javascript' in l
False
'c' not in
SyntaxError: invalid syntax
'c' not in l
False
t=('laptop','mobile','mouse','keyboard')
t
('laptop', 'mobile', 'mouse', 'keyboard')
'laptop' in t
True
'charger' in t
False
t={1,2,4,56,7,78,235,23}
t
{1, 2, 4, 7, 235, 78, 23, 56}
4 in t
True
d={'egg':8,'oil':120,'sugar':40,'salt':30}
'oil'  in d
True
120 in d
False
'sugar' in d
True
'chilli' in d
False
'water' not in d
True
'milk' not in d
True
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
n==m
True
l is m
False
n is m
True
id(l)
1512190338304
id(m)
1512190612736
id(n)
1512190612736
l is m
False
n is m
True
id(l)
1512190338304
id(m)
1512190612736
id(n)
1512190612736
l is not m
True
n is not l
True
8 & 14
8
8 & 7
0
8 |7
15
10^11
1
~12
-13
 8>>2
 
SyntaxError: unexpected indent
15>>1
7
8>>2
2
15>>1
7
15>>3
1
15>>2
3
>>> 16>>1
8
>>> 16<<1
32
>>> 4<<2
16
>>> print("a=",a,'b=',b,'c=',c,sep='',end='\n\n')
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    print("a=",a,'b=',b,'c=',c,sep='',end='\n\n')
NameError: name 'c' is not defined
>>> a=
SyntaxError: invalid syntax
>>> a=12
>>> b=12.3
>>> c=python
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    c=python
NameError: name 'python' is not defined
>>> print("a=",a,'b=',b,'c=',c,sep='',end='@@@@')
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    print("a=",a,'b=',b,'c=',c,sep='',end='@@@@')
NameError: name 'c' is not defined
>>> a=12,b=12.34,c=python
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=12b=12.34,c=python
SyntaxError: invalid decimal literal
