#how to access private method 
class Car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("updating software")
redcar=Car()
redcar.drive()
#accessing a private method like this 
redcar._Car__updatesoftware()