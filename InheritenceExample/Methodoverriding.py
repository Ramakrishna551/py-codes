#method overriding 
class Base:
    def add(self,a,b):
        return a+b
class Derived(Base):
    def add(self,a,b):
        return a+b+1
derived =Derived()
base = Base()
print(base.add(1,2))
print(derived.add(2,3))