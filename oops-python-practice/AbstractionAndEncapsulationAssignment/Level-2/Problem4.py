# problem 4 level 2 
# hospital patient system 
# hide sensitive disease info 

class Pat:
    def __init__(self, nam, dis):
        self.nam = nam
        self.__disease = dis       # private 
    
    def get_info(self):
        print("Patient:", self.nam, "| Disease: Confidential")

p = Pat("John", "Flu")
p.get_info()

# we dont show real disease outside 
# this is encapsulation for privacy