i = 0
while i < 100000:
    if(i % 10 == 0):
        i +=1
        continue
    print("i number is {}".format(i))
    i +=1

i = 1
while i < 1000000:
    if(i % 10 == 0):
        break
    print("i number is hey {}".format(i))
    i +=1
        