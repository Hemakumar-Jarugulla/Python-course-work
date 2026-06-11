# str list tuple set dict range()
'''

for var in seq:
    print(seq)
    
s='python programming'
for ch in s:
    print(ch)
l=['laptop','phone','charger','mouse','keyboard']
for item in l:
    print(item)


t=('1.intro','2.tokens','3.Datatypes')
for i in t:
    print(i)

s={'python','Dsa','gen ai','flask','my sql'}
for i in s:
    print(i)

'''
d={'name':'hemanth','batch':55,'course':'PFS','skiils':['python','my sql','java']
for i in d:
    print(i,d[i])

for i in range(10):
    pass
for i in range(10):
    if i==5:
        break
    print(i)
for i in range(10):
    if i==5:
        continue
    print(i)

for i in range(20,0,-1):
    print(i)
    

for i in range(30,2,-3):
    print(i)

#range(start,stop+1,step) => (0,n,1)
for i in range(1,11):
    print(i)
for i in range(2,51,2):
    print(i)
for i in range(5,101,5):
    print(i)
for i in range(20,0,-1):
    print(i)
seq=[1,2,3,4]
for var in seq:
    print(seq)
    
s='python programming'
for ch in s:
    print(ch)
l=['laptop','phone','charger','mouse','keyboard']
for item in l:
    print(item)


t=('1.intro','2.tokens','3.Datatypes')
for i in t:
    print(i)

s={'python','Dsa','gen ai','flask','my sql'}
for i in s:
    print(i)
s='looping statements'
for i in range(len(s)):
    print(i,s[i])
    
s='looping'
for i in enumerate(s):
    print(i[0],i[1])
l=[7,2,4,8,3,1,5]
for i in enumerate(l):
    print(i[0],i[1])
t=[7,2,4,8,3,1,5]
for i in enumerate(t):
    print(i[0],i[1]) 
    
k={7,2,4,8,3,1,5}
for i in enumerate(t):
    print(i[0],i[1])
    
s='looping statements'
for i in s:
    if i in 'aeiouAEIOU':
       print(i)
       
l=[56,76,32,3,34,2,3,5,97,45,13,23,45,23,98,76,32]
for i in l:
    if i%2==0:
       print(i)
d={'laptops':0,'chargers':2,'keyboard':15,'phone':15,'tab':0,'mouse':5}
for i in d:
    if d[i]:
        print(i)

t=(9,2,13,4,5,6)
for i in  range(len(t)):
    print(i*t[i])
    
name=('hemanth','sekhar','mallesh','krishna')
for i in name:
    print(i.upper())
