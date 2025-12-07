#string

print("hello wolrd")
print('hello wolrd')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

#multiline string

a = """this is
my name
and this
is my
age"""

print(a)

a = '''this is
my name
and this
is my
age'''
print(a)

#string are array of charecter
a = "this is my name"

print(a[1])

#loping on array

for x in a:
    print(x,end=" ")
print()

#length of string

print(len(a))

#checking text exist or not
txt = "my name is tamim"
print("tamim" in txt)
print("tamim" not in txt)


#if else

if "tamim" in txt:
    print("Yes this have it")

if "tamim" not in txt:
    print("Not have it")

