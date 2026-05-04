# problem 2 
# vehicle hierarchy 
# method overriding example 

# same method name different behaviour in child classes = polymorphism 

class Veh:
    def start(self):
        print("Vehicle started")

class Car(Veh):
    def start(self):
        print("Car started")

class Bike(Veh):
    def start(self):
        print("Bike started")

v1 = Car()
v2 = Bike()
v1.start()
v2.start()

# this is method overriding 
# in c# we use virtual and override keywords 
# in js its just redefine the method