num=[1,2,3,4]
print(num)
letter=['a','b','c','d']
print(letter)
stg=["get","certified","get","ahead"]
print(stg)
mix=[1,6,"amoghitschool","get","certified"]
print(mix)

mat=[[1,2],['a','b']]
print(mat)

print(mix)
print(mix[3])
print(mix[-2])
print(mix[:3])
print(mix[3:])
print(mix[2:4])
print(mix[::2])
print(mix[::-1])

z=[0]*100
print(z)

print(letter)
print(stg)
conc= letter + stg
print(conc)
var= list("hey there")
print(var)
print(num)
one, *other= num
print(one)
print(other)

print(num)
num.append(6)
print(num)
num.extend(stg)
print(num)
num.insert(5,"amoghitschool")
print(num)
num.remove("amoghitschool")
print(num)
var1=['b','f','a','q','r']
var1.sort()
print(var1)

x = [9,17,14,4,90,55]
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
print(sum(x)/len(x))

list1= list(range(1,11))
print(list1)
odd=list1[::2]
print(odd)
even=list1[1::2]
print(even)