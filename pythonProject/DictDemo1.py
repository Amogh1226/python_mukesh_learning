#emp={"QA":"Amogh","Dev":"Akash","DevOps":"John","Security":90,50:"Python"}
#print(emp)
#print(type(emp))
#print(emp["QA"])
#print(emp.get("Dev"))
emp={"QA":["Amogh", "Rahul","David"],"Dev":"Akash","DevOps":"John"}
#print(emp["QA"][1])
emp1=emp["QA"]
#print(emp1[4])

emp={"QA":"Amogh", "Dev":{"frontend":"Rajeev","backend":"Neha"}}
# print(emp.get("Dev").get("frontend"))
# print(emp["Dev"]["frontend"])
emp1=emp.get("Dev")
emp_name=emp1.get("backend")
print(emp_name)
print(emp["Dev"]["backend"])

emp["Manager"]="XYZ"
print(emp)

emp["Manager"]="Satya"
print(emp)

#emp.pop("QA")
#print(emp)
print("**********************************************************************")
print(emp)
emp.popitem()
print(emp)




