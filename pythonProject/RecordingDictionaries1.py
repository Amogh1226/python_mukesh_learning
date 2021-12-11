d1={}
print(d1)
print(type(d1))
d2={1:"Welcome",2:"to",3:"Python",4:"tutorial"}
print(d2)

d3={"name":"Sam","age":22,"profession":"student"}
print(d3)

d4={1:"Welcome",2:"to",3:"Python",4:"tutorial"}
print(d4)

d5=dict([(1,"Welcome"),(2,"to"),(3,"Python"),(4,"tutorial")])
print(d5)

d6={"name":{"first":"Sam","last":"Crew"},"age":22,"profession":"student"}
print(d6)

d={}
d[0]="Welcome"
d[1]=("How","are", "you")
d["name"]="Sam"
d["name"]={"first":"Sam","last":"Crew"}
print(d)
print(d["name"]["first"])
print(d.get(1))

print(d.pop(0))
print(d.popitem())

print(d.values())
keys={'a','b','c','d'}
value=1
print(dict.fromkeys(keys,value))
d.clear()
print(d)