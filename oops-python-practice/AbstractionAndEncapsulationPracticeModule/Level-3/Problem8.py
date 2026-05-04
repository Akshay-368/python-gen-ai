# problem 8 
# secure employee records 
# add validation in setter 

class Emprec:
    def __init__(self, nam, sal):
        self.nam = nam
        self.__salary = sal
    
    def set_salary(self, newsal):
        if ( newsal > 0 ) :           # basic validation 
            self.__salary = newsal
        else:
            print("Salary cannot be negative or zero")
    
    def get_salary(self):
        return self.__salary

emp = Emprec("Riya", 40000)
emp.set_salary(45000)
print(emp.get_salary())