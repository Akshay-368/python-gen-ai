# problem 5 
# product discount calculator 

class Prod:
    def __init__(self, nam, prc):
        self.nam = nam
        self.price = prc
    
    def apply_discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))

p = Prod("Laptop", 70000)
p.apply_discount(10)
print(p.price)

# we are modifying price inside method 
# self.price means current object's price