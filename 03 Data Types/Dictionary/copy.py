thisdict = dict(brand="Ford",model="Mustang",year=2020,colors=["red","white","blue"])
newdict = thisdict.copy()
newdict = dict(thisdict)
print(newdict)