# problem 1 from Inheritence And polymorphism assignment.pdf level 1 
# company employee hierarchy 
# base employee and manager subclass 

# inheritance lets child class reuse code from parent 
# in c# we use : 
# in js we use extends 

class Emp:
    def __init__(self, nam, sal):
        self.nam = nam
        self.sal = sal
    
    def total_salary(self):
        return self.sal

class Man(Emp):
    def __init__(self, nam, sal, bonus):
        super().__init__(nam, sal)      # calling parent 
        self.bonus = bonus
    
    def total_salary(self):
        return self.sal + self.bonus

m = Man("Riya", 60000, 10000)
print(m.total_salary())

# manager has extra bonus so we override total_salary 
# super() is must to call parent constructor