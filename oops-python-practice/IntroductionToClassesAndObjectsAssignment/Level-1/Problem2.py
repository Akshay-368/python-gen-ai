# problem 2 
# temperature converter class 

class Temp:
    def to_fahrenheit(self, c):
        return (c * 9/5) + 32
    
    def to_celsius(self, f):
        return (f - 32) * 5/9

t = Temp()
print(t.to_fahrenheit(0))