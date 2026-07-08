
with open('sample.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
'''
with open('.txt','a') as file:
    file.write('sathish\nmallesh\nkrishna')

import re
pattern='[A-Z]'
text='Python version is 3.11'

res=re.match(pattern,text)

print(res.group() if  res else "No Match Found")

import re

pattern= '[0-9]'
text='Python version 3.11'
res=re.findall(pattern,text)
print(res)
#print(res.group() if res else "No Match Found")

import re

pattern= '[0-9]'
text='Python version 3.11'
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())

file=open('sample.txt','r')
print("File is not there")
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

with open('sample.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())

with open('sample.txt','a') as file:
    file.write('sathish\nmallesh\nkrishna')

with open('sample.txt','w') as file:
    file.write('sathish\nmallesh\nkrishna')

import os
os.mkdir('Sample')
os.rmdir('Sample')

import re

pattern='[a-z]{9}'
text= 'hemakumar'
res=re.fullmatch(pattern,text)
print(res.group() if res else "No Match Found")


import re

pattern='r[a+yn]'
text= 'java,python,c++'

res= re.split(pattern,text)
print(res)

import re

pattern=r'[0-9]{2}'
text= 'python:54,java:89,my sqql:78,html:67'

res= re.sub(pattern,'**',text)
print(res)
'''


