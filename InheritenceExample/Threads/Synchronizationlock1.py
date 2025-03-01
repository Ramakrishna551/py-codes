#synchronizaation locks 
from time import sleep 
from threading import Thread,Lock
from concurrent.futures import ThreadPoolExecutor

class Counter:
    def __init__(self):
        self.value =0
        self._lock=Lock()
        
    def update(self,name):
        print("Update started on thread :"+str(name))
        with self._lock:
            print("Lock Acquired by :"+str(name))
            val =self.value
            val+=1
            sleep(1)
            self.value=val
            print("Lock Released by :"+str(name))
        print("Update ended on thread :"+str(name))
        
counter =Counter()
counter.update(1)
with ThreadPoolExecutor(max_workers=2) as executor:
    for index in range(2):
        executor.submit(counter.update,index)
print(counter.value)
print("DONE")
        