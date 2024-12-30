atoms = [1,66,4,56,88,99]
atoms.sort()
print(atoms[0]+atoms[-1])



atoms = [1,66,4,56,88,99]
print(max(atoms)+min(atoms))




val=[1,3,4,5,6,7]
emp_lst=[]
for x in val:
    if x%2==1:
        emp_lst.append(x)
    else:
        pass
print(emp_lst)




print([x for x in [1,3,4,5,6,7] if x%2==1])


val=[1,2,3]
print([f'even value{x}'if x%2==0 else f'{x} odd value'for x in val])