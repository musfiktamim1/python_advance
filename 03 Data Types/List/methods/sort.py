mylist = ["Bananas", "Pineapple", "Papaya", "Dragon Fruit", "Lychee"]
print(mylist)
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

mylist.sort(key=str.lower)
print(mylist)
def myfunc(x):
    return str.lower(x)
mylist.sort(key=myfunc)
print(mylist)