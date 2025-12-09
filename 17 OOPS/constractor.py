class Car:
    def __init__(self,brand:str,model:str,price:int,colors:list):
        self.brand = brand
        self.model = model
        self.price = price
        self.colors = colors
        print("car is created.")

car1 = Car("Ford","Mustang",20000,["white","black","blue"])
print(car1.brand)
print(car1.model)
print(car1.price)
print(car1.colors)