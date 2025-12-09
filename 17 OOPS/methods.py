class Numbers:
    def __init__(self,*kwd):
        self.numarr = list(kwd)

    def sum(self):
        total = 0
        for num in self.numarr:
            total += num
        return total
    def avg(self):
        return self.sum() / len(self.numarr)
    def min(self):
        minnum = self.numarr[0]
        for x in self.numarr:
            if(minnum > x):
                minnum = x
        return minnum

    def max(self):
        maxnum = self.numarr[0]
        for x in self.numarr:
            if(maxnum < x):
                maxnum = x
        return maxnum
    

num1 = Numbers(10,20,30,40,50)
print(num1.sum())
print(num1.avg())
print(num1.min())
print(num1.max())