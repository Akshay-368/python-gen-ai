# problem 3 
# method with computation 
# calculate annual salary from monthly 

class Sal:
    def __init__(self, monthly):
        self.monthly_salary = monthly
    
    def annual_salary(self):
        return self.monthly_salary * 12     # simple calculation 

sal = Sal(50000)
print(sal.annual_salary())

# methods can do calculations and return values 
# good practice to keep logic inside class