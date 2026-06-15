'''
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
      if i<=m:
          print('* '*(i+1),end=' ')
      else:
          print('* '*(n-i),end=' ')
      print()

n=int(input("Enter the size: "))
m=n//2

for i in range(n):
    if i<=m:
        print(' '*(m-i),end=' ')
        print('*'*(i+1),end=' ')
    else:
        print(' '*(i-m),end=' ')
        print('*'*(n-i),end=' ')
    print()

n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    if i<=m:
        print(' '* (m-i)+'* '*(i+1),end=' ')
    else:
        print(' '* (i-m)+'* '*(n-i),end=' ')
    print()



n=int(input("Enter the size:"))
mid=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or  i==mid or j==0 or j==n-1 or j==i or i+j==n-1 or j==mid:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
