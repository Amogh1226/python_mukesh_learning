s1={"Hello","This is a set","Hello"}
print(s1)
print(type(s1))
print(len(s1))

s2={1,2,3,4,5,6,7,8}
print(s2)
print(max(s2))
print(min(s2))
print(sum(s2))
print(sum(s2)/len(s2))

s3={"Hello User or Viewer",12,3.0,True}
print(s3)

s2.add("Hello How are you")
print(s2)
s2.remove("Hello How are you")
print(s2)
s2.pop()
print(s2)
s2.union(s3)
s2.difference(s3)
print(s2)
# s2.clear()
# print(s2)

s4=set(("Hello My name is Amogh"))
print(s4)

l1=list(s3)
print(l1)

print(s1==s2)
print(s1>s2)
print(3 in s2)
print(53 in s2)
print(3 not in s2)
print(s1 ^ s2)