"""uncomon , unique,have"""
set1 = set(("a","b","c"))
set2 = set((1,2,3))
set3 = set(("e","f","g"))
set4 = set((4,5,6))
set5 = set(("a","e",1,4))

print(set1.difference(set5))
print(set1 - set5)

set1.difference_update(set5)
print(set1)
