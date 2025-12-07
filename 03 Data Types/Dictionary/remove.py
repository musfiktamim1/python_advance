thisdict = dict(brand="Ford",model="Mustang",year=2020,colors=["red","white","blue"])
print(thisdict)
thisdict.pop("model")
print(thisdict)

thisdict = dict(brand="Ford",model="Mustang",year=2020,colors=["red","white","blue"])
print(thisdict)
thisdict.popitem()
print(thisdict)

thisdict = dict(brand="Ford",model="Mustang",year=2020,colors=["red","white","blue"])
print(thisdict)
del thisdict["colors"]
print(thisdict)

thisdict = dict(brand="Ford",model="Mustang",year=2020,colors=["red","white","blue"])
print(thisdict)
thisdict.clear()
print(thisdict)