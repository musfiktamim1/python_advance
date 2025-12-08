import simplejson

x = dict(name="musfik",age=19,color="white")

y = simplejson.dumps(x)
print(y)