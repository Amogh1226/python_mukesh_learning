t1=("Hello Everyone","How are you")
print(t1)
print(len(t1))

t2=("Hello",12,1.0,True)
print(t2)

t3=("Hello",12,"Hello")
print(t3)

t4=tuple([("Hello"),("How are you")])
print(t4)

t5=(12,23,34,45,56,67,78,89,90)
print(t5)
print(len(t5))
print(max(t5))
print(min(t5))
print(sum(t5))
print(sum(t5)/len(t5))
print(type(t5))

t6 = 9+3
print(t6)

t7 = 9-3
print(t7)

t8 = 9*3
print(t8)

t9 = 9/3
print(t9)

t10 = 9//3
print(t10)

t11 = 9^3
print(t11)

l1 = list(t5)
print(l1)

s1 = set(t5)
print(s1)

t5=(12,23,34,45,56,67,78,89,90)
print(t5[0:3])
print(t5[:3])
print(t5[::3])
print(t5[:])
print(t5[::-2])
print(t5[-2::-2])