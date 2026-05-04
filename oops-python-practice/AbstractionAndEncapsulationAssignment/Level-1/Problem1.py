# problem 1 level 1 
# encapsulated student data 
# we need to protect marks using private attribute 

# in python we use __double underscore for private 
# in c# we use private keyword 
# in js / typescript we use #private or just convention 

class Stud:
    def __init__(self, nam):
        self.nam = nam
        self.__marks = 0       # this is private now
    
    def set_marks(self, m):
        self.__marks = m       # only through this method we can set
    
    def get_marks(self):
        return self.__marks    # only way to see marks

s = Stud("Alex")
s.set_marks(85)
print(s.get_marks())

# this is basic encapsulation 
# outside code cannot directly change __marks