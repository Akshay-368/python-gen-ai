# problem 9 
# operator overloading in bank account 

class Bankacc:
    def __init__(self, bal):
        self.balance = bal
    
    def __add__(self, other):
        newbal = self.balance + other.balance
        return Bankacc(newbal)

a1 = Bankacc(5000)
a2 = Bankacc(3000)
a3 = a1 + a2
print(a3.balance)

# __add__ lets us use + operator on objects 
# in c# we overload + operator too 
# in js not directly possible like this