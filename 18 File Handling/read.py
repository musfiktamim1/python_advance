f = open("18 File Handling/db.txt")
print(f.read())
f.close()
# print(f.read())

# using with 
with open("18 File Handling/db.txt") as F:
    print(F.read())
    print(F.read(5))