# problem 5 
# polymorphic reporting system 

class Report:
    def generate(self):
        print("Generating generic report...")

class Pdfrep(Report):
    def generate(self):
        print("Generating PDF report...")

class Excelrep(Report):
    def generate(self):
        print("Generating Excel report...")

reports = [Pdfrep(), Excelrep()]

for r in reports:
    r.generate()

# same method name different output = polymorphism 
# very important in real projects