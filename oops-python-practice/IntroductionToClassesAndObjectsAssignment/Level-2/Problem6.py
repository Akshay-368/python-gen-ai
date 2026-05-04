# problem 6 
# invoice generator 

class Invoice:
    def __init__(self, client, amt):
        self.client = client
        self.amt = amt
    
    def generate_invoice(self):
        return "Invoice for " + self.client + " | Amount: " + str(self.amt)

inv = Invoice("Riya", 5000)
print(inv.generate_invoice())