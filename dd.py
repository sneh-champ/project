#1 Arithmatic operator
'''
a=10
print(a)
print(type(a))
'''
#comment single Line integer

'''
a=10.0
print(a)
print(type(a))
'''
#float number

'''
a=2j
print(a)
print(type(a))
'''
#complex number


#comman Question
'''
a=10
b=10
c=10
print(a)
print("id a=",id(a))
print(b)
print("id b=",id(b))
print("id c=",id(c))
'''

#Same Memory Location

# 1 Arithmetic Operator

#a=2
#b=3
'''
a=int(input("Enter the First Number"))
b=int(input("Enter the Second Number"))

print("Add=",a+b)
print("sub=",a-b)
print("Multi=",a*b)
print("Div=",a/b)
print("Mod=",a%b)
print("floor Div=",a//b)
print("expo=",a**b)
'''


# 2 assinment operator
#a=2
#b=3

#a+=b
#a-=b
#a*=b
#a/=b
#a%=b
#a//=b
#a**=b
#print("A=",a)
#String Qustion

# 3 relational operator
'''
a=2
b=4
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)
print(a==b)
'''
#print(2*3**3*4)

# 4 logical operator

#a=10
#b=10

#c=a>b and a<=b

#c=a>b or a<=b

#c=not(a>=b and a<=b)

#print(c)

#5 bitwise operator
'''
a=10
b=2
'''
#c=a & b
#c=a|b
#c=~a
#c=a^b
#c=a<<b
#c=a>>b

#print(c)



#6 member ship operator
# 1 in
# 2 not in

#a=[1,2,3,4,5]

#print(3 in a)
#print(7 in a)

#print( 3 not in a)

#print( 7 not in a)

# 7 identity operator
# 1 is
# 2 is not

'''
a=10
b=10.0

if(a is not b):
    print("hello")
else:
    print("hi..")
'''

#example
'''
# Exception of the Python
if(a==b):
    print("hello")
else:
    print("hi..")
    
'''

#statements
'''
# if statement
a=int(input("Enter the value"))
if(a==1):
    print("hello")
'''    

# 2 if else statements
'''
a=int(input("Enter the first value"))
b=int(input("Enter the Second Value"))
if(a>b):
    print("A is Greater")
else:
    print("B is Greater")
'''
# 3 nested if else statements

'''
a=int(input("enter the first value"))
b=int(input("enter the second value"))
c=int(input("enter the third value"))

if(a>b):
    if(a>c):
        print("a is greater")
    else:
        print("c is greater")
else:
    if(b>c):
        print("b is greater")
    else:
        print("c is greater")
        
'''

# elif statement

'''
a=int(input("enter the value of a"))
if(a==1):
    print("sunday")
elif(a==2):
    print("Monday")
elif(a==3):
    print("Tuesday")
elif(a==4):
    print("Wednesday")
else:
    print("Wrong:")
'''

#loops
# 1 while
# for

'''
a=1
while(a<=5):
    print(a)
    a+=1
'''

#while else loop

'''
a=11
while(a<=5):
    print(a)
    a+=1
else:
    print("Executed")
    
'''
'''
a=2
f=0
n=int(input("Enter the Number"))
while(a<n):
    if(n%a==0):
        f=1
    a+=1

if(f==1):
    print("Not prime")
else:
    print("prime")
    
'''        

#list [] represent 
'''
a=[1,2,3,4,5,6]
print(a)
print(type(a))
'''
#Tuple () represent
'''
a=(1,2,3,3,4,5)
print(a)
print(type(a))
'''


#for loop
# list in loop
'''
a=[1,2,3,4,4,5,6]

for x in a:
    print(x)
'''

#tuple in loop

'''
a=(1,2,3,3,4,5,5,6,76)
for x in a:
    print(x)
'''

#String in Loop

'''
a="Computer in Global Touch"

for x in a:
    print(x,end='')
'''
'''
for x in "Computer":
    print(x)
'''


#for loop in range() function
'''
for x in range(1,10,1):
    print(x)
'''
'''
for x in range(10):
    print(x)
'''

'''
for x in range(2,11,2):
    print(x)
'''

#list

#a=[10,12,3,31,4,5,8]

#print(a)
#indexing in list forword
'''
i=0
while(i<7):
    print(i,"=",a[i])
    i+=1

'''
'''
a=[10,12,3,31,4,5,8]

for x in range(0,7):
    print(x,"=",a[x])
    
'''

#indexing in backword

'''
a=[1,2,3,4,5,6,7]
print(a[-1])
'''

#slicing in list forword

#a=[1,5,6,7,8,3,2,4,65]

#print(a[0:3])
#print(a[0:3:1]) #by default 1 step
#print(a[0:])

#print(a[:])

#print(a[:6])
#print(a[: :2])


#slicing bakword

#a=[1,5,6,7,8,3,2,4,65]
#print(a[-1:-5:-1]) #slicing me step dena must hota h(-)me

#print(a[-5:-1])

#tuple index
#same tuple and list
#a=(1,2,3,4,5,6)
#print(a[0])
#print(a[-1])


#String  in index and slicing

#a="computer"
#print(a[0])
#print(a[1])

#print(a[0:3])

#print(a[-1:-5:-1]) #backword slicing

#d={'id':'101','roll':'1200'}
#print(d)
#print(type(d))

#print(d['id'])
#print(d['roll'])
#print(d.keys())
#print(d.values())
#print(d.items())

'''
s={3,4,5,5,6,7,8}
print(s)
print(type(s))
'''

# Comman Question
'''
a=()
print(a)
print(type(a))
'''

'''
#bydefault Tuple
b=1,2,3,4,5
print(b)
print(type(b))

'''

'''
c={}
print(c)
print(type(c))
'''


#function in Python
#two types ke function hote

#user define function
# 1 No Return With No Parameter
'''

def raj():   #definaction of the Function 
    print("hello function")

raj()  # calling of the Function
raj()
raj()

#reusable code
'''

# 2 No Return with Parameter

'''
def raj(a,b):  #where is a and b is parameter
    print(a+b)

raj(2,4) # 2 and 4 is arguments
'''

# 3 return with no parameter
'''
def raj():
    a=10
    b=20
    c=a+b
    return c
'''
#4 return with parameter
'''
def raj(a):
    return a**2
'''

#x=raj(5)
#print(x)
#print(raj(5))


#arbitrary arguments
'''
def raj(*a):
    #print(a[0]) indexing of tuple
    print(a)

raj("raj","mohit","sonu")
'''


#keyword arguments
'''
def raj(a,b,c):
    print(a,b,c)

raj(c="10",b="20",a="40")
'''

#arbitrary keyword arguments
'''
def raj(**a):
    #print(a)
    print(a['fname'])

raj(fname="raj",lname="mohit")
'''

#default parameter
'''
def raj(a=10):
    print(a)

raj(100)
raj(200)
raj()
'''

#class and object
'''
class A:
    def raj(self):  #method (function) self parameter
        print("call function")
n=A() #object of the class
n.raj()
'''
'''
class B:
    def raj(self,a,b): #no return with parameter
        print(a+b)

n=B()
n.raj(10,20)
'''
#pass statement

'''
def raj():
    pass
'''

#lambda function
'''
x=lambda a:a+2
print(x(3))
'''

































    








































