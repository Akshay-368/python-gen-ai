# problem 2 
# product info wrapper 
# id should not be changed after creation 

class Prod:
    def __init__(self, nam, pid):
        self.nam = nam
        self.__id = pid        # private id 
    
    def get_id(self):
        return self.__id

p = Prod("Laptop", 1001)
print(p.get_id())

# no setter for id so its read only 
# good for things that should never change 