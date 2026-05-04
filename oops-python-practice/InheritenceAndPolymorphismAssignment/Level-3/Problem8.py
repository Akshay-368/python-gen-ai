# problem 8 
# data export system 

class Exporter:
    def export(self, data):
        print("Exporting data...")

class Csvexp(Exporter):
    def export(self, data):
        print("Exporting data as CSV...")

class Jsonexp(Exporter):
    def export(self, data):
        print("Exporting data as JSON...")

for e in [Csvexp(), Jsonexp()]:
    e.export({"name": "Alex"})