with open("18 File Handling/home.txt","w") as F:
    F.write("This is my hello world code")

with open("18 File Handling/home.txt","r") as F:
    print(F.read())
