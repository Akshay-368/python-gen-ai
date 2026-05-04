# problem 9 
# abstract data pipeline 

from abc import ABC, abstractmethod

class Datapipe(ABC):
    @abstractmethod
    def extract(self):
        pass
    @abstractmethod
    def transform(self):
        pass
    @abstractmethod
    def load(self):
        pass

class Csvpipe(Datapipe):
    def extract(self):
        print("Extracting CSV data...")
    def transform(self):
        print("Transforming data...")
    def load(self):
        print("Loading data into database...")

p = Csvpipe()
p.extract()
p.transform()
p.load()