# problem 3 
# employee count tracker 

class Emp:
    count = 0          # class variable 
    
    def __init__(self, nam):
        self.nam = nam
        Emp.count = Emp.count + 1     # increase count

e1 = Emp("Alex")
e2 = Emp("Riya")
print(Emp.count)