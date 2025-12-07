#global variable

x = 10

def myChange():
    x = 20
myChange()

print(x)
def myChange1():
    global x
    x = 300
myChange1()

print(x)