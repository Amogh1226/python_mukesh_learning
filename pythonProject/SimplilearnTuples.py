emp=()
print(type(emp))
print(emp)
city="Pune",
print(type(city))
city=("Pune")
print(city)
city=("Pune",)
print(city)
city= ("Pune", "Bangalore", "Delhi", "Mumbai")
print(city)
list1=[1,2,3,4]
tuple1=(1,2,3,4)
list1.append(5)
print(list1)
# tuple1.append(5)
# print(tuple1)

print(city)
print(city[1])
print(city[-1])
print(city)
num=1,2,3,4
print(city+num)

nest=(city,num)
print(nest)

rep=("Python",)*5
print(rep)

rep=("Python",)
print(rep*10)
print(rep)

print(num)
print(num[1:])
print(num[::-1])

tuple("amoghitschool")
print(num)
a,b,c,d=num
print(a,b,c,d)
a,*b,c=num
print(a,b,c)

# tuple1=(1,2,3,4)
# print(tuple1)
# del tuple1
# print(tuple1)

num1=(3,5,2,2,2,2,6,5,8)
print(num1.count(2))
print(sum(num1))
print(len(num1))
print(max(num1))
print(min(num1))

lst=[1,2,3,4]
print(type(lst))
tpl=tuple(lst)
print(tpl)
print(type(num1))

lst=[(1,2,3),(4,5,6)]
lst.append(("Tuple","Inside","List"))
print(lst)
lst.remove((1,2,3))
print(lst)

tpl=(['a','b','c'],['d','e','f'])
print(tpl)
tpl[0].append('z')
print(tpl)
tpl[0].remove('z')
print(tpl)
# tpl.append(['x','y','z'])
print(tpl)

series=(0,1,2,3,4,5,6,7,8,9)
print(series)

series1=series+(10,)
print(series1)
series3=series1[:11]+series[::-1]
print(series3)