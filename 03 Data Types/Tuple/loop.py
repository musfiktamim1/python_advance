mytuple = tuple(("apple","banana","cherry","orange"))

for x in mytuple:
    print(x)
print("second")
for x in range(len(mytuple)):
    print(mytuple[x])
i = 0
while i<len(mytuple):
    print(mytuple[i])
    i += 1