lst1 = ['a','b','c']
lst2 = [1,2,3]
print(lst1 + lst2)

lst1.extend(lst2)
print(lst1)

lst1 = ['a','b','c']
lst2 = [1,2,3]

newlist = [ [x,y] for [x,y] in zip(lst1,lst2)]
print(newlist)

newlist = [ x for x in zip(lst1,lst2)]
print(newlist)