'''
import re

pattern=r'h.t\b'
text='hot hit het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)

import re

pattern=r'^h'
text='hot  het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)
import re

pattern=r't$'
text='hot hit het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)

import re

pattern=r'ho*'
text='hot hit het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)

import re

pattern=r'ho+'
text='hot hit het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)


import re

pattern=r'to?'
text='hot hit het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)

import re

pattern=r'(python)'
text= 'pyth pythn python puthon'
res=re.findall(pattern,text)
print(res)

import re

pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
text= input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")

import re

pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
text= input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")

import re

pattern = r'^(?=.*[A-Z])(?=.*[[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,})'
text= input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")

'''
import re

pattern = r'^[a-zA-Z0-9]{5,15}$'
text= input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")
'''
r'h.t'->hot hit het hrt hjt h$t
r'^c'-> cat code copy
r'$g' - > ing,programmming
r'ab*' -> a ab abbbb abbbbbbb
r'ab+'-> ab abbbb abbbb
r'to?' => too to tot

r'[a-zA-Z0-9]' ->a b cd ABDC 7352
r'[aeiou]' -> aeioupen
r'[#@&*!]' -> #@

r'xx\.gmail.com'
r'{5}--->7386547705'
'''
