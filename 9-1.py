a=10
b=10
print(a is b)
print(id(a))
print(id(b))





lst1=[[10,20],[20,30]]
lst2=lst1
lst1[1][0]=300
print(lst1)
print(lst2)





import copy
lst1=[[10,20],[20,30]]
lst2=copy.copy(lst1)
lst1[1][0]=300
print(lst1)
print(lst2)





import copy
lst1=[[10,20],[20,30]]
lst2=copy.deepcopy(lst1)
lst1[1][0]=300
print(lst1)
print(lst2)



lst=[10,20,30,40,50]
for i,j in enumerate(lst):
    print(i,j)




lst=[10,20,30,40,50,20]
print(lst.count(20))




lst=[10,20,30,40,50,20]
print(lst.count(20))
print(lst.index(40))




