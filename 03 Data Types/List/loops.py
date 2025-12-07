mylist = list(("banana","apple","sraves","mango"))

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1

print("compression")
[print(x) for x in mylist]