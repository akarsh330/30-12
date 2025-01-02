sales_item=[]
print(type(sales_item))
val={}
print(type(val))
val={1}
print(type(val))




sales_2023={1,2,3}
sales_2024={3,4,5}
print(sales_2023.union(sales_2024))
print(sales_2023.intersection(sales_2024))
print(sales_2023.difference(sales_2024))
print(sales_2024.difference(sales_2023))
print(sales_2023.symmetric_difference(sales_2024))




sql={1,2,3,4,5}
python={1,6,7,8}
print(sql.intersection(python))
print(python.difference(sql))
print(sql.union(python))
print(sql.intersection(python))
print(sql.difference(python))












sql={1,2,4,5}
python={1,6,7,8}
aws={1,4,5,6,99}
print((sql),(python).intersection(aws))