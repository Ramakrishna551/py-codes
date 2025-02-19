#polymorphism example:
class Worker:
    def work(self):
        print("working")
    def perform_task(self):
        print("performing task:",end='')
        self.work()
class DelivaryMan(Worker):
     def work(self):
        print("Delivery goods ")
class Lumberjack(Worker):
     def work(self):
        print("cutting wood ")
deliverman =DelivaryMan()
lumjack=Lumberjack()
deliverman.perform_task()
lumjack.perform_task()
        
    