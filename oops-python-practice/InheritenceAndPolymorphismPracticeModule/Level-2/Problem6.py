# problem 6 
# multi level inheritance 

class Person:
    def __init__(self, nam, age):
        self.nam = nam
        self.age = age

class Employee(Person):
    def __init__(self, nam, age, empid):
        super().__init__(nam, age)
        self.empid = empid

class Manager(Employee):
    def __init__(self, nam, age, empid, dept):
        super().__init__(nam, age, empid)
        self.dept = dept
    
    def display(self):
        print("Name:", self.nam, "| Age:", self.age, "| Department:", self.dept)

m = Manager("Alex", 35, 101, "Finance")
m.display()