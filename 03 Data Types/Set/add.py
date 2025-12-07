thisset = set(("musfik","tamim","rahman",1,True,False,0))

thisset.add("Rahman")
print(thisset)

thisset = set(("musfik","tamim","rahman",1,True,False,0))
thisset.update(set(("Hello","World")))
print(thisset)

thisset = set(("musfik","tamim","rahman",1,True,False,0))
thisset.update(list(("Hello","World")))
print(thisset)