import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.day)
print(x.month)

print(x.strftime("%A"))

y = datetime.datetime(2022,10,12)
print(y)
print(y.strftime("%B"))

listoftypestrf = list(("%a","%A","%w","%d","%b","%B","%m","%y","%Y","%H","%I","%p","%M","%S","%f","%z","%Z","%j","%U","%W","%c","%C","%x","%X","%%","%G","%u","%V",))

for form in listoftypestrf:
    print(form , " = " ,x.strftime(form))