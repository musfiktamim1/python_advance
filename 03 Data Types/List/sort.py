mynumlist = [20,30,40,50,60,70,80,90,100]
mylist = ["Bananas", "Pineapple", "Papaya", "Dragon Fruit", "Lychee"]
mynumlist.sort()
print(mynumlist)
mynumlist.sort(reverse=True)
print(mynumlist)
mynumlist.sort()
print(mynumlist)
mynumlist.sort(reverse=True)

def myfunc(x):
    return abs(x % 2)

mynumlist.sort(key= myfunc)
print(mynumlist)

print(mylist)
mylist.sort(key=str.upper)
print(mylist)