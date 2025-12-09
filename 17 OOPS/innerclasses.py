class Computer:
    def __init__(self):
        self.cpu = self.__CPU()
        self.ram = self.__RAM()

    class __CPU:
        def proccess(self):
            print("proccessing...")
    class __RAM:
        def store(self,data="undefined"):
            print("storing data...")
            print("stored this data",data)

comp1 = Computer()
comp1.cpu.proccess()
comp1.ram.store("Hello world")