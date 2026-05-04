# problem 7 level 3 
# shape area calculator 

import math

class Shape:
    def area(self):
        return 0

class Rect(Shape):
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
    
    def area(self):
        return self.len * self.wid

class Circ(Shape):
    def __init__(self, rad):
        self.rad = rad
    
    def area(self):
        return math.pi * self.rad * self.rad

r = Rect(10, 5)
c = Circ(7)
print(r.area())
print(round(c.area(), 2))