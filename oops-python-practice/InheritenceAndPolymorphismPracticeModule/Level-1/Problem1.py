# problem 1 level 1 
# employee inheritance example 
# base class employee and manager subclass 

# inheritance means child class gets everything from parent 
# in c# we use : for inheritance 
# in js we use extends 
# python uses () after class name 

class Emp:
    def __init__(self, nam, eid):
        self.nam = nam
        self.eid = eid
    
    def display_info(self):
        print("Employee Name:", self.nam)
        print("ID:", self.eid)

class Man(Emp):
    def __init__(self, nam, eid, dept):
        super().__init__(nam, eid)      # calling parent constructor 
        self.dept = dept
    
    def display_info(self):
        super().display_info()          # calling parent method 
        print("Department:", self.dept)

m = Man("Alex", 101, "Finance")
m.display_info()

# super() is very important in python inheritance 
# without it parent stuff wont initialise properly