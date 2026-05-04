# problem 1 level 1 
# vehicle info system 

class Veh:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        print("Brand:", self.brand, ", Model:", self.model)

v = Veh("Tesla", "Model 3")
v.display()

# this is basic class with constructor and method 
# in c# we use public class 
# in js we use class keyword too