#single inheritence example 
class Person:
    def __init__(self,name):
        self.name=name
    def sayName(self):
        print(self.name)
class Engineer(Person):
      def __init__(self,name):
        super().__init__(name)
      def sayProfession(self):    
        self.profession="Engineer"
        print(self.profession)
engineer =Engineer("RK")
engineer.sayName()
engineer.sayProfession()
        
        