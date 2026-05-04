# problem 3 
# abstract payment example 

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amt):
        pass

class Cardpay(Payment):
    def process_payment(self, amt):
        print("Processing card payment of", amt)

p = Cardpay()
p.process_payment(1000)

# abstract class forces every child to implement the method 
# same idea in c# with abstract 
# in ts we use interface 