'''
def function_name(arg):
    #stmts
    return
function_name(para)

def wish(name):
    print(f' Welcome to the python course {name}')

wish('hemanth')
wish('sekhar')
wish('rajesh')
wish('rakesh')

def isEven(num):
    if num%2==0:
       return f"{num} - Even Number"
    else:
       return f"{num} - Odd Number"
    
print(isEven(10))
print(isEven(6))

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num=int(input("Enter the number: "))
print("Factorial:",factorial(num))

def isprime(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
num=int(input("Enter the number:"))
isprime(num)


def isprime(num):
    for  i in range(2,num//2):
         if num%i==0:
             return f"{num} - not a prime number"
    return f"{num} - Prime Number"
    
num=int(input("Enter the number: "))
print(isprime(num))

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display(name='hemanth',email='hemanth@gmail.com',pwd='hemanth@123')
display(email='hemanth@gmail.com',name='hemanth',pwd='hemanth@123')
display(email='hemanth@gmail.com',pwd='hemanth@123',name='hemanth')



 '''            
def display(*names):
    print("Names:",names)
display('sekhar','hemanth','rakesh','sathish','rajesh')
display('rajesh')
display('sekhar','hemanth')


def display(**names):
    print("Names:",names)
display(k1='sekhar',k2='hemanth',k3='rakesh')
display(k1='rajesh')
display(k1='sekhar',k2='hemanth')

