# problem 4 level 2 
# student attendance system 

class Stud:
    def __init__(self, nam):
        self.nam = nam
        self.attendance = "Not marked"
    
    def mark_present(self):
        self.attendance = "Present"
    
    def mark_absent(self):
        self.attendance = "Absent"

s = Stud("Alex")
s.mark_present()
print(s.attendance)