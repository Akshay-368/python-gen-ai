# problem 4 level 2 
# payment system hierarchy 

class Payment:
    def process_payment(self):
        print("Processing generic payment...")

class Creditcard(Payment):
    def process_payment(self):
        print("Processing credit card payment...")

class Upi(Payment):
    def process_payment(self):
        print("Processing UPI payment...")

p1 = Creditcard()
p2 = Upi()
p1.process_payment()
p2.process_payment()