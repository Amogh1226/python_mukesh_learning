#print("Welcome")
if 15>10:print("Yes")
#print("Bye")

marks=85
#print("A+") if marks>90 else print("A")

salary=input("Please enter your salary for loan :")
print(type(salary))
sal=int(salary)
print(type(sal))
#sal=50000
if sal>40000:
    print("Eligible for car loan")
    if sal>80000:
        print("Eligible for home loan")
	if sal>100000:
	    print("Premium customer- Eligible for all kind of loan")
else:
    print("Sorry we could not serve you")

