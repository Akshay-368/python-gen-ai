# problem 9 
# employee performance tracker 

class Emp:
    def __init__(self, nam, projects):
        self.nam = nam
        self.projects_completed = projects
    
    def performance(self):
        if ( self.projects_completed >= 10 ) :
            return "Excellent"
        elif ( self.projects_completed >= 5 ) :
            return "Good"
        else:
            return "Needs Improvement"

emp = Emp("Riya", 12)
print(emp.performance())

# different performance levels based on projects 
# good use of if-elif-else inside class