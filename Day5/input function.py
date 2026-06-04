Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input()
hemanth
name
'hemanth'
name=input("Enter your name: ")
Enter your name: Hemanth
name
'Hemanth'
age=input("Enter your age: ")
Enter your age: 22
age
'22'
cgpa=input("Enter your cgpa: ")
Enter your cgpa: 7.8
cgpa
'7.8'
type(cgpa)
<class 'str'>
cgpa=float(input("Enter the cgpa: "))
Enter the cgpa: 7.8
cgpa
7.8
type(cgpa)
<class 'float'>
'Rajesh Sekhar Hemanth Rakesh Sathish'
'Rajesh Sekhar Hemanth Rakesh Sathish'
names=input("Enter the names: ").split()
Enter the names: Rajesh Sekhar Hemanth Rakesh Sathish
names
['Rajesh', 'Sekhar', 'Hemanth', 'Rakesh', 'Sathish']
Products=input("Enter the products: ").split()
Enter the products: laptop keyboard mouse desktop touchpad
products
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    products
NameError: name 'products' is not defined. Did you mean: 'Products'?
products
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    products
NameError: name 'products' is not defined. Did you mean: 'Products'?
products=input("Enter the products: ").split()
Enter the products: laptop keyboard mouse desktop touchpad
SyntaxError: multiple statements found while compiling a single statement
products=input("Enter the products: ").split()
Enter the products: laptop mouse charger keyboard
products
['laptop', 'mouse', 'charger', 'keyboard']
topics=tuple(input("Enter the topics: ").split())
Enter the topics: token statement variables comments
topics
('token', 'statement', 'variables', 'comments')
op=set(input("Enter the oper: ").split())
Enter the oper: in not in is is not and or not
op
{'not', 'or', 'and', 'in', 'is'}
marks=input("Enter the marks: ").split()
Enter the marks: 34 76 89 21 12
marks
['34', '76', '89', '21', '12']
map(int,input("Enter the marks: ").split())
Enter the marks: 5 6 7 9 0
<map object at 0x0000027DAAE1FB80>
list(map(int,input("Enter the marks: ").split()))
Enter the marks: 1 3 5 85 345
[1, 3, 5, 85, 345]
prices=tuple(map(int,input("Enter the prices: ").split()))
Enter the prices: 4356 43567 456 8976 45 87
prices
(4356, 43567, 456, 8976, 45, 87)
rating=set(map(int,input("Enter the rating: ").split()))
Enter the rating: 4 3 4 5 3 3 2
rating
{2, 3, 4, 5}
per=list(float(map(input("Enter the per :").split()))
per's =list(map(float,input("Enter the per's : ").split()))
         
SyntaxError: unterminated string literal (detected at line 2)
per=list(map(float,input("Enter the per's: ").split()))
         
Enter the per's: 56.3 23.3 78.9 34.5
per
         
[56.3, 23.3, 78.9, 34.5]
prices=tuple(map(float,input("Enter the prices: ").split()))
         
Enter the prices: 567 45678 4567 5678 7896 45
prices
         
(567.0, 45678.0, 4567.0, 5678.0, 7896.0, 45.0)
prices=set(map(float,input("Enter the prices: ").split()))
         
Enter the prices: 5467 34567 54678 65
prices
         
{65.0, 5467.0, 54678.0, 34567.0}
a,b=10,20
         
a
         
10
b
         
20
a,b=(10,20)
         
a
         
10
b
         
20
username&password=input("Enter the username&password: ").split()))
SyntaxError: unmatched ')'
username&password=input("Enter the username&password: ").split()
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
username,password=input("Enter the username & password: ").split()
Enter the username & password: hemanth @Hemanth1
username,password
('hemanth', '@Hemanth1')
a,b,c,d=list(map(int,input("Enter the 4 sides: ").split()))
Enter the 4 sides: 8 5 3 8
a
8
b
5
c
3
d
8
price,discount=list(map(float,input().split()))
345678 89.0
price
345678.0
discount
89.0
a=eval(input())
34567
a
34567
a=eval(input())
4567.54678
a
4567.54678
a=eval(input())
[1,2,3,4,4]
a
[1, 2, 3, 4, 4]
a=eval(input())
(1,2,3,4)
a
(1, 2, 3, 4)
a=eval(input())
a=eval(input())
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    a=eval(input())
           ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
a=eval(input())
{1,2,3,4}
a
{1, 2, 3, 4}
a=eval(input())
{3:9,4:16,5:25}
a
{3: 9, 4: 16, 5: 25}
a=eval(input())
true
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a='hemanth'
>>> b='srikakulam'
>>> a+b
'hemanthsrikakulam'
>>> h*9
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    h*9
NameError: name 'h' is not defined
>>> H*10
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    H*10
NameError: name 'H' is not defined
>>> a*10
'hemanthhemanthhemanthhemanthhemanthhemanthhemanthhemanthhemanthhemanth'
>>> b*3
'srikakulamsrikakulamsrikakulam'
>>> 'python ' *6
'python python python python python python '
