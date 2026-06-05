Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='Python Programming'
len(s)
18
max(s)
'y'
min(s)
' '
sorted(s)
[' ', 'P', 'P', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'r', 'r', 't', 'y']
chr(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    chr(a)
NameError: name 'a' is not defined
ord('A')
65
chr(57)
'9'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.swapcase()
'pYTHON pROGRAMMING'
s.casefold()
'python programming'
s
'Python Programming'
s.title()
'Python Programming'
s
'Python Programming'
s.center(48,'*')
'***************Python Programming***************'
s.ljust(58,'-')
'Python Programming----------------------------------------'
s.rjust(68,'*')
'**************************************************Python Programming'
s.zfill(9)
'Python Programming'
'345'.zfill(9)
'000000345'
s
'Python Programming'
s.find('0')
-1
s.find('o')
4
s.rfind('o')
9
s.find('z')
-1
s.index('o')
4
s.rindex('o')
9
s.count('o')
2
s
'Python Programming'
s.replace('python','java')
'Python Programming'
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
translate(s.maketrans('python','123456')
s.translate(s.maketrans('python','123456')
            
SyntaxError: '(' was never closed
s.translate(s.maketrans('python','123456'))
            
'P23456 Pr5grammi6g'
s=('python,java,c,c++')
            
s
            
'python,java,c,c++'
s.split(',')
            
['python', 'java', 'c', 'c++']
s.rsplit(',',2)
            
['python,java', 'c', 'c++']
s.splitlines()
            
['python,java,c,c++']
s.join(@)
            
SyntaxError: invalid syntax
>>> s.join('@')
...             
'@'
>>> s
...             
'python,java,c,c++'
>>> s
...             
'python,java,c,c++'
>>> s=['python','java','c','c++']
...             
>>> s
...             
['python', 'java', 'c', 'c++']
>>> s='python','java','c','c++','js'
...             
>>> s
...             
('python', 'java', 'c', 'c++', 'js')
>>> s.partition(',')
...             
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s.partition(',')
AttributeError: 'tuple' object has no attribute 'partition'
>>> s='python,java,c,c++,js'
...             
>>> s
...             
'python,java,c,c++,js'
>>> s.partition(',')
...             
('python', ',', 'java,c,c++,js')
>>> s.rpartition(',')
...             
('python,java,c,c++', ',', 'js')
>>> s.replace('java','react')
...             
'python,react,c,c++,js'
