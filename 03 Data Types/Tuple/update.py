mytuple = tuple(("apple","banana","cherry","orange"))

y = list(mytuple)
y[0] = "Apple"
mytuple = tuple(y)

print(mytuple)

y = list(mytuple)
y.append("999")
mytuple = tuple(y)

print(mytuple)

mytuple += ("9999",)

print(mytuple)


y = list(mytuple)
y.remove("9999")
mytuple = tuple(y)

print(mytuple)

y = list(mytuple)
y.clear()
mytuple = tuple(y)

print(mytuple)