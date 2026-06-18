'''
syntax:

var = lambda arg:exp

add=  lambda a,b:a+b
print(add(12,13))
print(add(22,33))


wish= lambda name: f'Welcome the python course {name}'

print(wish('hemanth'))

gst = lambda price:price+price*1.18
print(gst(1000))
print(gst(180))
print(gst(1600))

greatest=lambda a,b:a if a>b else b
print(greatest(1500,300))
print(greatest(1200,400))
print(greatest(4000,2000))

iseven=lambda a:f"{a}-Even number" if a%2==0 else f"{a}-odd number"
print(iseven(4))
print(iseven(9))
print(iseven(16))


bill= lambda charge: charge if charge>99 else charge+30
print(bill(145))
print(bill(45))
print(bill(15))

login=True
instock=True
status=lambda login,instock:("You can buy product" if instock
else "Product is out of stock") if login else "Login to buy product"
print(status(login,instock))

l=['hemanth','sekhar','rajesh','sathish']
for i in range(len(l)):
    l[i]=l[i].title()
print(l)


d={'sugar':45,'salt':30,'Milk':25}
gst=dict(map(lambda i:,d.items()))
print(gst)

l=[1,2,3,4,5,6,7,8,9,10,11,12]
res=list(filter(lambda i:i%2==0,l))
print(res)

l=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i>5,l))
print(res)

l=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i%3==0,l))
print(res)

from functools import reduce

l=[1,2,3,4,5,6,7,8,9,10,11,12]

s=reduce(lambda sum,i: sum+i,l)
p=reduce(lambda pro,i: pro*i,l)
m=reduce(lambda max,i: max if max>i else i,l)
mi=reduce(lambda max,i:max if max<i else i,l)
print(s,p,m,mi)
'''
d={'krishna':50,'mallesh':40,'hemanth':60,'sekhar':80,'rakesh':70}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse= True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse= True)))



               

