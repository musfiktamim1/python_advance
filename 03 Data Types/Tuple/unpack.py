mytuple = tuple(("apple","banana","cherry","orange"))

(apple,banana,cherry,orange) = mytuple

print(apple)
print(banana)
print(cherry)
print(orange)

(apple,banana,*key) = mytuple
print(apple,banana,key)

(apple,*key,orange) = mytuple

print(apple,key,orange)