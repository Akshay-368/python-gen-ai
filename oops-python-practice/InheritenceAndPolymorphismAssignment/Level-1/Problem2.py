# problem 2 
# base and derived class interaction 
# method overriding 

class Machine:
    def start(self):
        print("Machine starting...")

class Printer(Machine):
    def start(self):
        print("Printer started printing...")

p = Printer()
p.start()

# child class changed the behaviour of start method 
# this is called method overriding 
# polymorphism in simple words