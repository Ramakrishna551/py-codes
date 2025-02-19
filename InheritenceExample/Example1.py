class Person:
    def __init__(self,name):
        self.name=name
    def sayName(self):
        print("My name is :{}".format(self.name))
class Engineer(Person):
      def __init__(self,name):
        super().__init__(name)
      def sayProfession(self):    
        self.profession="Engineer"
        print(self.profession)
class Doctor(Person):
      def __init__(self,name):
        super().__init__(name)
      def sayProfession(self):    
        self.profession="Doctor"
        print(self.profession)
engineer =Engineer("RK")
engineer.sayName()
engineer.sayProfession()
doctor=Doctor("Raghu")
doctor.sayName()
doctor.sayProfession()
        
        