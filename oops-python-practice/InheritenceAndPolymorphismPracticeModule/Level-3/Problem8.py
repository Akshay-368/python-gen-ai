# problem 8 
# multiple inheritance example 

class Logger:
    def log(self, msg):
        print("Log:", msg)

class Database:
    def save(self, data):
        print("Database entry saved:", data)

class Monisys(Logger, Database):
    pass      # it gets methods from both parents

sys = Monisys()
sys.log("Server started")
sys.save("Server running")

# multiple inheritance = one class can have many parents 
# powerful but can get complicated (diamond problem)