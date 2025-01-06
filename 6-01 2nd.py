lst=[1,2,3,4]
emp=[]
for x in lst:
    emp.append(x**3)
print(emp)


print([x**3 for x in [1,2,3,4]])






lst=[1,2,3,4]
print({x:x**3 for x in lst})
print({x:x**2 for x in lst})



lst=[10,[20,30,40]]
