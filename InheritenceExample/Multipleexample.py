#Multiple inheritence  Inheritence 
class A:
    def printA(self):
        print("From A ")
class B:
    def printB(self):
        print("From B")
class C(A,B):
    def printC(self):
        print('From C ')
obj = C()
obj.printA()
obj.printB()
obj.printC()
        