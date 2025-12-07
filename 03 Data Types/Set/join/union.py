"""common , uncomon , unique"""

set1 = set(("a","b","c"))
set2 = set((1,2,3))
set3 = set(("e","f","g"))
set4 = set((4,5,6))

print(set1.union(set2))

print(set1 | set2)


print(set1.union(set2,set3,set4))
print(set1 | set2 | set3 | set4)


print(set1.update(set2))
print(set1)
print(set1.update(set2,set3,set4))

print(set1)