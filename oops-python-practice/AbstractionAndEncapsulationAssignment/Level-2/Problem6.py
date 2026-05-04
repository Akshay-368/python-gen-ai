# problem 6 
# protected attribute example 
# _single underscore means protected 

class Anal:
    def __init__(self, dat):
        self._data = dat      # protected 
    
    def show_data(self):
        print("Data:", self._data)

a = Anal("Raw Data")
a.show_data()

# subclasses can access _data but outsiders should not 
# this is convention in python