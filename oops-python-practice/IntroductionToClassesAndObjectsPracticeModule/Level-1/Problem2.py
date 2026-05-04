# problem 2 
# constructor initialization 
# setting emp_id and name when object is created 

class Emp:
    def __init__(self, eid, nam):
        self.emp_id = eid       # using self to store values 
        self.name = nam

emp = Emp(101, "Riya")
print(emp.emp_id, emp.name)

# constructor runs automatically when we do Emp( )
# very important concept 
# in c# its public Employee(int eid, string nam)