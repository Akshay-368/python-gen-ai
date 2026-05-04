# problem 4 level 2 
# student report system 
# decide pass or fail based on marks 

class Stud:
    def __init__(self, nam, marks):
        self.nam = nam
        self.marks = marks
    
    def grade(self):
        if ( self.marks >= 50 ) :
            print("Pass")
        else:
            print("Fail")

student = Stud("Alex", 75)
student.grade()

# if else inside method 
# simple conditional logic in class