# problem 5 
# animal sound simulator 

class Animal:
    def make_sound(self):
        print("Some sound...")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animals = [Dog(), Cat()]

for a in animals:
    a.make_sound()

# polymorphism in action - same method different output 
# very useful concept