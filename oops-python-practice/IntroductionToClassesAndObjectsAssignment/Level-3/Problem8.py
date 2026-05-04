# problem 8 
# expense tracker 

class Exptrack:
    def __init__(self):
        self.transactions = []
    
    def add_expense(self, amt):
        self.transactions.append(amt)
    
    def total_expense(self):
        total = 0
        for t in self.transactions:
            total = total + t
        return total

e = Exptrack()
e.add_expense(200)
e.add_expense(300)
print(e.total_expense())