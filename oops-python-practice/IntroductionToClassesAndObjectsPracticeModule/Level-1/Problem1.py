# problem 1 level 1 
# basic class creation 
# alex needs employee class with name and department 

# in python we use class keyword 
# in c# its class Employee { } with public fields 
# in js / ts also class but constructor is different 

class Emp:
    def __init__(self, nam, dept):
        self.nam = nam          # instance variable 
        self.dept = dept
    
    def display_details(self):
        print("Name:", self.nam, ", Department:", self.dept)

emp1 = Emp("Alex", "IT")
emp1.display_details()

# __init__ is constructor 
# self is like this in c# and js 