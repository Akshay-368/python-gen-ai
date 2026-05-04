# problem 4 level 2 
# banking system with inheritance 

class Account:
    def __init__(self, nam, bal):
        self.nam = nam
        self.balance = bal
    
    def deposit(self, amt):
        self.balance = self.balance + amt

class Savacc(Account):
    def add_interest(self):
        self.balance = self.balance * 1.05     # 5% interest 

s = Savacc("Alex", 10000)
s.deposit(5000)
s.add_interest()
print(s.balance)