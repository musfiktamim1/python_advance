try:
    print(x)
except NameError:
    print("Doesont difined x")
except :
    print("error.")
finally:
    print("close")