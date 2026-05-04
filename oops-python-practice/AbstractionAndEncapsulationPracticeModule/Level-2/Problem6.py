# problem 6 
# encapsulated vehicle info 
# hide engine number 

class Veh:
    def __init__(self, eng):
        self.__engine_number = eng
    
    def get_engine_info(self):
        print("Engine Number:", self.__engine_number)

v = Veh("1234-ENG")
v.get_engine_info()