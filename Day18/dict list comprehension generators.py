'''
d={'sugar':40,'salt':20,'cooking oil':80,'chilli':60}
res=dict(map(lambda i: (i[0],i[1]+i[1]*0.18),d.items()))
res1=dict(map(lambda i: (i[0],i[1]-i[1]*0.5),d.items()))
print(res)
print(res1)

d={'sugar':40,'salt':20,'cooking oil':80,'chilli':60}
res=dict(filter(lambda i:i[1]>50,d.items()))
res1=dict(filter(lambda i:i[1]<50,d.items()))
print(res,res1)

res=[]
for i in range(1,11):
    res.append(i)
print(res)

res1=[]
for i in range(1,11):
    res1.append(i)
    
res2= [i for i in range(1,11)]
print(res1)
print(res2)

res3=[]
for i in range(3,31,3):
    res3.append(i)
res4=[i for i in range(3,31,3)]
print(res3)
print(res4)
res5=[]
for i in range(2,52,1):
    res5.append(i)
print(res5)


res6=[i for i in range(2,52,2)]
print(res5)
print(res6)

a= 'Python Programming'
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(a)
print(l)

l1= [i for i in a if i in 'aeiouAEIOU']
print(l1)

a= [1,2,4,5,6,8,9,11,2,32,45,65,67,80]
l=[]
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(i)
print(l)

l=[val for var in seq]
l=[val for var in seq if condition]
l=[val if condition else val for var in seq]

l=[int(input(f"Enter the number - {i+1}: ")) for i in range(10)]
print(l)

l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)

l1=[j for i in range(3) for j in range(1,4)]
print(l1)

l = [val if condition else val for var in seq ]

l=[[j for j in range(1,4)] for i in range(3)]
print(l)

s=set()
for i in range(1,11):
    s.add(i)
s1= {i for i in range(1,11)}
print(s,s1)

d={}
for i in range(1,11):
    d[i]=i*i
print(d)
res={i:i*i for i in range(1,11)}
print(res)

d={'hemanth':20,'sekhar':30,'rakesh':50,'rajesh':60}
for i in d:
    print(i,d[i])

res={input("Enter the name: "):int(input("Enter the mark: "))
     for i in range(5)}
print(res)
'''
def display():
    l=['1..50','51..100','101..150','151..200']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]
    
scroll = display()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
