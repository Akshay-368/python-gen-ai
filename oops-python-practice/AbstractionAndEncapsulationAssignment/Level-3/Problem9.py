# problem 9 
# data processor framework 

from abc import ABC, abstractmethod

class Dataproc(ABC):
    @abstractmethod
    def load_data(self):
        pass
    @abstractmethod
    def process_data(self):
        pass
    @abstractmethod
    def export_data(self):
        pass

class Salesproc(Dataproc):
    def load_data(self):
        print("Loading sales data...")
    def process_data(self):
        print("Processing sales data...")
    def export_data(self):
        print("Exporting processed data to report.csv...")

processor = Salesproc()
processor.load_data()
processor.process_data()
processor.export_data()