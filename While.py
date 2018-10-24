"""
x=1
while x<=10:
    print(x)
    x+=1
"""
"""
x=int(input("Enter Numbers:"))
add=0
i=1
while i<=x:
    add=add+i
    i+=1
print(add)
"""
"""
x=""
while x!="Durga":
    x=input("Enter Name:")
"""
"""
i=0
while True:
    i=i+1
    print("Hello:",i)
"""
"""
x=int(input("Enter any number:"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
"""
x=int(input("Enter any Number:"))
for i in range(x):
    print('*'*x)
"""
"""
x=int(input("Enter any Number:"))
for i in range(x):
    for j in range(x):
        print('*',end='')
    print()
"""
"""
x=int(input("Enter any Number:"))
for i in range(1,x+1):
    for j in range(i):
        print('*',end='')
    print()
"""
"""
n=int(input("Enter any Integer:"))
if n<=1000:
    for num in range(2,n):
        if num<=1000:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num,end=' ')
"""
"""
n=int(input())
a=0
for i in range(1,n+1):
    a=i*i
"""
"""
n=input()
b=int(input())
for i in n:
    a=chr(ord(i)+b)
    print(a,end='')
"""
"""
n,a,b=[int(x) for x in input().split()]
c=0
for y in range(n,a+1):
    if y%b==0:
        c+=1
print(c)
"""
"""
class Student:
    ''''This class developed by durga for demo purpose'''

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

    def talk(self):
        print("Hello My Name is:",self.name)
        print("My Rollno is:",self.rollno)


s = Student(120,'Mohit')
print(s.name)
print(s.rollno)

s1 = Student(200,'Bunny')
s1.talk()
"""

s=input("Enter String")
count=0
for i in s:
    if





























