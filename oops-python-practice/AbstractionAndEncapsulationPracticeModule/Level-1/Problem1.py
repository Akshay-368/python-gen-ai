# problem 1 level 1 
# employee data protector 
# we need to hide salary so no one can change it directly 

# in python private variable starts with __ 
# in c# we use private keyword clearly 
# in js / ts its #salary or just _salary by convention 

class Emp:
    def __init__(self, nam, sal):
        self.nam = nam
        self.__salary = sal      # this is private now 
    
    def set_salary(self, new_sal):
        self.__salary = new_sal
    
    def get_salary(self):
        return self.__salary

emp = Emp("Alex", 50000)
emp.set_salary(55000)
print(emp.get_salary())

# only through setter and getter we can touch salary 
# this is basic encapsulation 