# problem 2 
# abstract device interface 

# abstract class means we cannot make object of it directly 
# in python we use ABC 
# in c# we use abstract class 
# in ts we use interface 

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def connect(self):
        pass

class Phone(Device):
    def connect(self):
        print("Phone connected.")

class Tablet(Device):
    def connect(self):
        print("Tablet connected.")

d1 = Phone()
d2 = Tablet()
d1.connect()
d2.connect()