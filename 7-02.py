a=[10,10,20]
for x in a:
    print(x,'--->',a.count(x))
print([a.count(x) for x in a])




a=[10,10,20]
for x in set(a):
    print(x,'--->',a.count(x))
print([a.count(x) for x in a])




val='armani'
vowels='aeiou'
for x in val:
    if x in vowels:
        print(x)



lst=[10,20,30,40,50]
print(lst)
lst.pop(3)
print(lst)