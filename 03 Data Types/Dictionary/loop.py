thisdict = dict(brand="Ford",model="Mustang",year=2020,colors=["red","white","blue"])

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x,y in thisdict.items():
    print("{} = {}".format(x,y))