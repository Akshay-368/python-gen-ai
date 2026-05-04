# problem 5 
# file reader interface 

from abc import ABC, abstractmethod

class Fileread(ABC):
    @abstractmethod
    def read(self):
        pass

class Textread(Fileread):
    def read(self):
        print("Reading text file...")

class Csvread(Fileread):
    def read(self):
        print("Reading CSV file...")

readers = [Textread(), Csvread()]

for r in readers:
    r.read()