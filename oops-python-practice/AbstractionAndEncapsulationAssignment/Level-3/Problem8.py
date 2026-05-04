# problem 8 
# secure user account system 
# password must stay private 

class User:
    def __init__(self, nam, pwd):
        self.nam = nam
        self.__password = pwd      # very private 
    
    def verify_password(self, inputpwd):
        if ( inputpwd == self.__password ) :
            return True
        else:
            return False

u = User("Alex", "secure123")
print(u.verify_password("secure123"))