def lower(func):
    def myinner():
        return str.lower(func())
    return myinner
    

def upper(func):
    def myinner(x):
        return str.upper(func(x))
    return myinner

def hello(func):
    def myinner(name):
        return f"hello {name}"
    return myinner

@lower
def mylowername():
    return "MUSFIK"

@upper
def myname(name):
    return name

@upper
@hello
def myhey(name):
    return name

print(mylowername())

print(myname("musfik"))

print(myhey("musfikur rahman"))