# problem 7 level 3 
# abstract payment gateway system 

from abc import ABC, abstractmethod

class Paygate(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def authorize(self):
        pass
    @abstractmethod
    def complete(self):
        pass

class PayPal(Paygate):
    def connect(self):
        print("Connecting to PayPal...")
    def authorize(self):
        print("Authorizing payment via PayPal...")
    def complete(self):
        print("Transaction completed using PayPal.")

class Stripe(Paygate):
    def connect(self):
        print("Connecting to Stripe...")
    def authorize(self):
        print("Authorizing payment via Stripe...")
    def complete(self):
        print("Transaction completed using Stripe.")

gateways = [PayPal(), Stripe()]

for g in gateways:
    g.connect()
    g.authorize()
    g.complete()