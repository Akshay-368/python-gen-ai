# problem 7 level 3 
# shape hierarchy with polymorphism 

import math

class Shape:
    def area(self):
        return 0

class Rect(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w

class Circ(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

shapes = [Rect(10, 5), Circ(7)]

for s in shapes:
    print(round(s.area(), 2))