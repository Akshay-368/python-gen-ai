# problem 3 
# read only configuration class 

class Conf:
    def __init__(self, ver):
        self.__version = ver      # private so cannot change outside
    
    def get_version(self):
        return self.__version

c = Conf("v1.2.3")
print(c.get_version())

# no setter method so its read only 
# good for config that should not change