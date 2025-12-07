thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
}

print(thisdict)
print(type(thisdict))

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "year":2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "year":2020,
    "colors":["red","white","blue"]
}
print(thisdict)

print(len(thisdict))

thisdict = dict(brand="Ford",model="Mustang",year=2020,colors=["red","white","blue"])
print(thisdict)