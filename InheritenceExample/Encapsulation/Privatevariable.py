class Car:
    def __init__(self):
        self.__updatesoftware()
        self.__maxspeed=10
    def drive(self):
        print("driving car")
    def __updatesoftware(self):
        print("software updating ")
#to change the value of a private variable setter method is used 
    def setspeed(self,speed) :
        self.__maxspeed =speed
    def getspeed(self):
        print(self.__maxspeed)
    
    
car = Car()
# car.__maxspeed = 10
car.getspeed()
car.setspeed(320)
car.getspeed()
car.drive()



