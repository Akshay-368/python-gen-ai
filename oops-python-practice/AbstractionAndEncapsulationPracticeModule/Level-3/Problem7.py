# problem 7 level 3 
# banking interface with abstraction 

from abc import ABC, abstractmethod

class Acc(ABC):
    @abstractmethod
    def deposit(self, amt):
        pass
    @abstractmethod
    def withdraw(self, amt):
        pass
    @abstractmethod
    def get_balance(self):
        pass

class Savacc(Acc):
    def __init__(self, nam, bal):
        self.nam = nam
        self.__bal = bal
    
    def deposit(self, amt):
        self.__bal = self.__bal + amt
        print("Deposited in Savings")
    
    def withdraw(self, amt):
        if ( amt <= self.__bal ) :
            self.__bal = self.__bal - amt
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__bal

s = Savacc("Alex", 5000)
s.deposit(2000)
s.withdraw(1000)
print(s.get_balance())