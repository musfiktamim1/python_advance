x = lambda a:a+10
y = lambda a,b:a+b
print(x(20))
print(y(20,50))

def myfunc(n):
    return lambda a:a*n

mydouble = myfunc(2)
mytriple = myfunc(3)
print(mydouble(20))
print(mytriple(20))

numbers = [1,2,3,4,5]
doublednumber = list(map(mydouble,numbers))
triplednumber = list(map(mytriple,numbers))

print(doublednumber)
print(triplednumber)