class MyClass:
    x = 10

p1 = MyClass()
p1.x = 20

del p1

print(MyClass.x)
# print(p1.x)