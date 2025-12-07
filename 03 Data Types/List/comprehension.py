mylist = ["Bananas", "Pineapple", "Papaya", "Dragon Fruit", "Lychee"]
print(mylist)

mynewList = []

#problem
for x in mylist:
    if("a" in x):
        mynewList.append(x)

print(mynewList)

mynewList.clear()
#soluation

print(mynewList)
mynewList = [x for x in mylist if "a" in x]
print(mynewList)

myrangelist = [x for x in range(1,11)]
print(myrangelist)
myrangelist = [x for x in range(1,11) if x > 5]
print(myrangelist)

mynewList = [x.upper() for x in mylist]
print(mynewList)