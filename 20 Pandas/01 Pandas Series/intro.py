import pandas as pd

a = [1,2,3,4]

myvar = pd.Series(a)
print(myvar)
print(myvar[0])
print(myvar[1])
myvar = pd.Series(a,index=["W","X","Y","Z"])
print(myvar)
print(myvar["W"])


mydata = {
    "day1":420,
    "day2":380,
    "day3":390
}

myvar = pd.Series(mydata)
print(myvar)
print(myvar["day1"])

myvar = pd.Series(mydata,index=["day1","day2"])
print(myvar)