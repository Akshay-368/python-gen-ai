# problem 7 level 3 
# banking account class 

class Bankacc:
    def __init__(self, holder, bal):
        self.account_holder = holder
        self.balance = bal
    
    def deposit(self, amt):
        self.balance = self.balance + amt
    
    def withdraw(self, amt):
        if ( amt <= self.balance ) :
            self.balance = self.balance - amt
        else:
            print("Not enough money")

acc = Bankacc("Alex", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.balance)