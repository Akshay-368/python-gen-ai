# problem 6 
# class variable demonstration 

class Emp:
    company = "Capgemini"      # class variable shared by all objects 
    
    def __init__(self, nam):
        self.nam = nam         # instance variable different for each 

emp1 = Emp("Alex")
emp2 = Emp("John")
print(emp1.company)
print(emp2.company)

# company is same for everyone 
# name is different for each employee 
# this is difference between class and instance variables