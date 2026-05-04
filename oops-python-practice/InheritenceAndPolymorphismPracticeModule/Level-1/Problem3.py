# problem 3 
# student inheritance 

class Stud:
    def __init__(self, nam, marks):
        self.nam = nam
        self.marks = marks

class Gradstud(Stud):
    def __init__(self, nam, marks, thesis):
        super().__init__(nam, marks)
        self.thesis = thesis
    
    def display(self):
        print("Student:", self.nam, "| Marks:", self.marks, "| Thesis:", self.thesis)

g = Gradstud("Riya", 90, "AI in Healthcare")
g.display()