
list =['a','b','c','d','b','m','c','c']

duplicate =[]

for value in list:
    if list.count(value) >1  and (value not in duplicate):
        duplicate.append(value)
print(duplicate)