Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'K1':'v1','k2':'v2'}
d
{'K1': 'v1', 'k2': 'v2'}
d[1]='int'
d
{'K1': 'v1', 'k2': 'v2', 1: 'int'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d({1,2,3,4)}='tuple'
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
d[(1,2,3)]='tuple'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', (1, 2, 3): 'tuple'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', (1, 2, 3): 'tuple', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[223]=23.4
d[3]='fdghjk'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]=(1,3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
d[7]=(1,3)
d[7]={1,3}
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 223: 23.4, 3: 'fdghjk', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
d={}
d[1]='int'
d
{1: 'int'}
d[1]=12
d
{1: 12}
d[1]=14
d
{1: 14}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[1]
2
d[4]
8
d={}

d={'hemanth':90,'sekhar':75,'krishna':45,'mallesh':65,'narsinga':35}
d
{'hemanth': 90, 'sekhar': 75, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
d{'krishna'}
SyntaxError: invalid syntax
d['krishna']
45
d['mallesh']
65
d['hemanth']
90
d['sekhar']
75
d.get('krishna')
45
d.get('hemanth')
90
d.get('rakesh','user not found')
'user not found'
d.get('sekhar','user not found')
75
'hemanth' in d
True
'rakesh'  not in d
True
'sekhar' not in d
False
d.keys()
dict_keys(['hemanth', 'sekhar', 'krishna', 'mallesh', 'narsinga'])
d.values()
dict_values([90, 75, 45, 65, 35])
d.items()
dict_items([('hemanth', 90), ('sekhar', 75), ('krishna', 45), ('mallesh', 65), ('narsinga', 35)])
sorted(s)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    sorted(s)
NameError: name 's' is not defined
sorted(d)
['hemanth', 'krishna', 'mallesh', 'narsinga', 'sekhar']
max(d)
'sekhar'
min(d)
'hemanth'
len(d)
5
d
{'hemanth': 90, 'sekhar': 75, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
d['hemanth']=100
d
{'hemanth': 100, 'sekhar': 75, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
d['sekhar']=89
d
{'hemanth': 100, 'sekhar': 89, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
d.update({'krishna'} {'mallesh'})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d.update({'krishna':56},{'mallesh':78})
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    d.update({'krishna':56},{'mallesh':78})
TypeError: update expected at most 1 argument, got 2
d.update
<built-in method update of dict object at 0x00000132DA729AC0>
d.update({'gopal':70,'chitti':80})
d
{'hemanth': 100, 'sekhar': 89, 'krishna': 45, 'mallesh': 65, 'narsinga': 35, 'gopal': 70, 'chitti': 80}
d.popitem()
('chitti', 80)
d
{'hemanth': 100, 'sekhar': 89, 'krishna': 45, 'mallesh': 65, 'narsinga': 35, 'gopal': 70}
>>> d.popitem()
('gopal', 70)
>>> d
{'hemanth': 100, 'sekhar': 89, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
>>> d.pop('sekhar')
89
>>> d
{'hemanth': 100, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
>>> del d['hemanth']
>>> d
{'krishna': 45, 'mallesh': 65, 'narsinga': 35}
>>> d.clear()
>>> d{}
SyntaxError: invalid syntax
>>> d
{}
>>> d
{}
>>> d={'hemanth':90,'sekhar':75,'krishna':45,'mallesh':65,'narsinga':35}
>>> d
{'hemanth': 90, 'sekhar': 75, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
>>> d.setdefault('hemanth',0)
90
>>> d
{'hemanth': 90, 'sekhar': 75, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
>>> d.setdefault('sekhar',0)
75
>>> d
{'hemanth': 90, 'sekhar': 75, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
>>> d.setdefault('krishna',0)
45
>>>  d
...  
SyntaxError: unexpected indent
>>> d
{'hemanth': 90, 'sekhar': 75, 'krishna': 45, 'mallesh': 65, 'narsinga': 35}
>>> d.setdefault('krishna',0)
45
