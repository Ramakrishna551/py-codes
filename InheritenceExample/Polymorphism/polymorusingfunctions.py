#polymorphism with functions
class Bird:
    def fly(self):
        return "Flies high in the sky"

class Airplane:
    def fly(self):
        return "Flies using jet engines"

class Rocket:
    def fly(self):
        return "Flies beyond the atmosphere"

def flying_object(obj):
    print(obj.fly())

# Using polymorphism
objects = [Bird(), Airplane(), Rocket()]
for obj in objects:
    flying_object(obj)
