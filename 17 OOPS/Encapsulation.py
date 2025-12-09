class Vehicle:
    def __init__(self,brand:str,rate:float):
        self.__brand = brand
        self.__rate = rate

    def getBrand(self):
        return self.__brand
    def getPrice(self):
        return self.__rate
    
v1 = Vehicle("Ford",20000)
# print(v1.__brand)
print(v1.getBrand())