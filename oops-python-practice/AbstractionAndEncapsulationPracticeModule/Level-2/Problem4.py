# problem 4 level 2 
# secure bank account 
# protect balance and account number 

class Bankacc:
    def __init__(self, accno, bal):
        self.__account_number = accno
        self.__balance = bal
    
    def deposit(self, amt):
        self.__balance = self.__balance + amt
        print("Deposited :", amt)
    
    def withdraw(self, amt):
        if ( amt <= self.__balance ) :
            self.__balance = self.__balance - amt
            print("Withdrawn :", amt)
        else:
            print("Not enough balance")
    
    def get_balance(self):
        return self.__balance

acc = Bankacc(101, 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())