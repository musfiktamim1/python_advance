def say_hello(fname:str,default:str = "hello"):
    return "{} {}".format(default,fname)

def mylistprint(marks:list):
    for mark in marks:
        print(mark)
    return (marks,len(marks))

print(say_hello("Musfik"))
say_hello(fname="musfik")
print(say_hello(fname="musfik",default="HEY"))

x,y = mylistprint(["hello","world","!"])
print(x,y)


#unknown arguments

def my_list(*kids):
    print(kids)

my_list("hello","world","whatsup","im","fine") #take like tuple

def greeting(greeting,*names):
    for name in names:
        print(greeting,name)
greeting("Hello","musfik","rahman","tamim")


def totalofnumber(*nums:int):
    total = 0
    for num in nums:
        total += num
    return total

print(totalofnumber(10,20,30,40,50,60,70,80,90,100))


def namecombine(**names):
    print(names)
namecombine(fname="musfik",lname="tamim") #like a dictionary

def namecombiner(**names):
    name = ""
    for x in names.values():
        name += " {}".format(x)
    return name

print(namecombiner(fname="musfik",mname="tamim",lname="rahman"))