# problem 5 
# online store product catalog 

class Prod:
    def __init__(self, nam, prc, stock):
        self.nam = nam
        self.prc = prc
        self.stock = stock
    
    def add_stock(self, qty):
        self.stock = self.stock + qty
    
    def sell(self, qty):
        if ( qty <= self.stock ) :
            self.stock = self.stock - qty
        else:
            print("Not enough stock")

p = Prod("Laptop", 50000, 5)
p.sell(2)
print(p.stock)