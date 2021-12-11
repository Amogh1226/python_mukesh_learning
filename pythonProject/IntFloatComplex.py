# num=5
# print(type(num))
#
# num=2343445545
# print(type(num))
#
# num=5.4
# print(type(num))
#
# num=2+5j
# print(type(num))
#
# print(num.real)
# print(num.imag)
#
# num=-5647.675
# print(num)
#
# num1=10
# num2=2
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(10/3)
# print(10//3)
# print(num1**num2)
# print(num1%num2)
#
# x = "192"
# print(type(x))
#
# print(int(x))
#
# x=int(x)
# print(type(x))
#
# x=float(x)
# print(x)
#
# x=complex(x)
# print(x)
#
# print(complex(2,6))
#
# x= -7.5
# print(abs(x))

# import math
# x=10
# print(math.exp(x))
# print(math.e)
# print(math.pi)
# print(math.sqrt(6))
#
# print(max(1,34,4986,3254,687))
# print(min(1,34,4986,3254,687))
n=input("Enter a number ")
n=int(n)
flag=0
for i in range(2,n):
    if n%i ==0:
        flag=1
        print("%d is not a prime number"%n)
        break
if flag==0:
    print("%d is a prime number"%n)

import math
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=b*b-4*a*c
if d<0:
    sol1=-b/(2*a)
    sol2=math.sqrt(-d)/2*a
    print("The solutions are:\n",complex(sol1,sol2))
    print(complex(sol1,-sol2))
else:
    sol1=-(b-math.sqrt(d))/(2*a)
    sol2=-(b+math.sqrt(d))/(2*a)
    print("the solutions are:\n",sol1)
    print(sol2)