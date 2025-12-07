thisdict = dict(brand="Ford",model="Mustang",year=2020,colors=["red","white","blue"])
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("model"))
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

if "model" in thisdict:
    print("yes,model have")