'''
n=10
def display():
    print("Inside:",n)
display()
print("Outside:",n)

def display():
    global n
    n+=10
    print("Inside:",n)

    
n=10
display()
print("Outside:",n)

def outer():
    n=10
    def inner(n):
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner(n)
    print("Outer function:",n)
    
outer()

s='python'
print(len(s))

#int float complex str list tuple set dict bool
#int float complex str tuple bool
#list set dict
def update(n):
    n+=10
    print("Inside:",n)
n=10
update(n)
print("Outside:",n)


def update(n):
    n+=10.4
    print("Inside:",n)
n=10.0
update(n)
print("Outside:",n)

def update(n):
    n+=10+j
    print("Inside:",n)
n=10+j
update(n)
print("Outside:",n)

def update(n):
    n+="Hemanth"
    print("Inside:",n)
n='sekhar'
update(n)
print("Outside:",n)

def update(n):
    n+=[1,2,3,4]
    print("Inside:",n)
n=1,2,3,4
update(n)
print("Outside:",n)

recursion

def func()
    if bascondition:
    return
func()

def func(num):
    if num==0:
        return
    print(num,end=' ')
    func(num-1)
    print(num,end=' ')
func(5)
f(5)=>5,f(4)=>4,f(3)=>3,f(2)=>2,f(1)=>1


def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))

def power(base,pow):
    if pow==0:
        return 1
    return base * power(base,pow-1)
print(power(2,4))
print(power(3,3))
'''

def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)

l="Python Programming"
print(reverseofstr(l,len(l)-1))


