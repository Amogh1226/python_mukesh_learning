print("Example's of Tuple's")
thistuple = ("CPU", "Monitor", "TV")
print(thistuple)

mytuple = ("Keyboard", "Mouse", "CPU", "Monitor", "TV")
print(mytuple)

easytuple = tuple(("CPU", "Monitor", "TV"))
print(len(easytuple))

favoratetuple = ("apple",)
print(type(favoratetuple))

#Not a tuple
favoratetuple = ("apple")
print(type(favoratetuple))

Datatypes1 = ("apple", "banana", "cherry")
Datatypes2 = (1,5,7,9,3)
Datatypes3 = (True, False, False)

print(Datatypes1)
print(Datatypes2)
print(Datatypes3)

SuperTuple = ("abc", 34, True, 40, "male")

print(SuperTuple)

Typetuple = ("CPU", "Monitor", "TV", "Mouse", "Keyboard")

print(type(mytuple))

Tupleconstructor = tuple(("CPU", "Monitor", "TV", "Keyboard", "Mouse"))
print(Tupleconstructor)

print("Real Example's of Tuple's")

Realtuple = ("CPU", "Monitor", "TV", "Mouse", "Keyboard")
print(Realtuple)

Lentuple = ("CPU", "Monitor", "TV", "Keyboard", "Mouse")
print(Lentuple[3])

Changetuple = ("CPU", "Monitor", "Tv")
Changetuple = "CV"

# the value in still the same:
print(Changetuple)

Newtuple = ("CPU", "Monitor", "TV")
for x in Newtuple:
    print(x)

Truetuple = ("CPU", "Monitor", "TV", "Keyboard", "Mouse")
if "TV" in Truetuple:
    print("Yes, 'TV' is in the mechanic tuple")

Numbertuple = ("CPU", "Monitor", "TV")
print(len(thistuple))

# Errortuple = ("CPU", "Monitor", "TV")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

Differenttuple = tuple(("CV", "Monitor", "TV"))
print(Differenttuple)