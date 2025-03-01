#Race conditionds code 
from time import sleep 
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

class Counter:
    def __init__(self):
        self.value =0
    
    def update(self,name):
        print("update started on Thread :"+str(name))
        val = self.value
        val+=1
        sleep(1)
        self.value=val
        print("update ended on Thread :"+str(name))
counter =Counter()
counter.update(1)
with ThreadPoolExecutor(max_workers=2,) as executor:
    for index in range(2):
        executor.submit(counter.update,index)
print(counter.value)
print("DONE")