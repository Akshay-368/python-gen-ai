# problem 9 
# employee hierarchy manager 

class Emp:
    def __init__(self, nam, dept):
        self.nam = nam
        self.dept = dept

class Man(Emp):
    def __init__(self, nam, dept, teamsize):
        super().__init__(nam, dept)
        self.teamsize = teamsize
    
    def display(self):
        print("Manager:", self.nam, "| Department:", self.dept, "| Team Size:", self.teamsize)

m = Man("Alex", "IT", 10)
m.display()