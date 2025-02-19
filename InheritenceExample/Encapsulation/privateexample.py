class Account:
    def __init__(self):
        self.setbalance(10)
    def setbalance(self,balance):
        self.__balance=balance
    def getbalance(self):
        print(self.__balance)
acc=Account()
acc.getbalance() #first setted balance ==10
acc.setbalance(20) #updated balance ==20
acc.getbalance() 