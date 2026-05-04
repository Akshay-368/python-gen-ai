# problem 7 level 3 
# bank loan eligibility system 

class Loanapp:
    def __init__(self, nam, sal, credit):
        self.nam = nam
        self.sal = sal
        self.credit = credit
    
    def is_eligible(self):
        if ( self.sal > 50000 ) and ( self.credit > 700 ) :
            return True
        else:
            return False

applicant = Loanapp("Riya", 80000, 750)
print(applicant.is_eligible())