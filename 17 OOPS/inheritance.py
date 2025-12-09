class Car:
    def __init__(self):
        self.brand = ""
        self.model = ""
        self.colors = []
        self.prices = []

        self.engine = False
        self.ascalator = False
        self.started = False
    def startengin(self):
        self.engine = True
    def startascalator(self):
        self.ascalator = True
    def __start(self):
        if(self.engine and self.ascalator):
            self.started = True
        else:
            self.started = False
    def startstop(self):
          pass
    
class Mustang(Car):
    def __init__(self):
        super().brand = "Ford"
        super().model = "Mustang"
        super().colors = ["white","blue","black"]
        super().prices = [1000,2000,3000]

musta1 = Mustang()
Mustang.startengin()
Mustang.startengin()
Mustang.startengin()