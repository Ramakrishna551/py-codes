#polymorphism using classes 
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # Calls the appropriate speak() method
