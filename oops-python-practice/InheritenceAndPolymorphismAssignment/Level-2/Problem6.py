# problem 6 
# multi level transport example 

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Electriccar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery
    
    def display(self):
        print("Brand:", self.brand, "| Model:", self.model, "| Battery:", self.battery, "%")

ec = Electriccar("Tesla", "Model X", 90)
ec.display()