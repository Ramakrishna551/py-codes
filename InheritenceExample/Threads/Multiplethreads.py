from time import sleep
from threading import Thread
def thread_funtion(name):
    print("Thread {0} started ".format(name))
    sleep(2)
    print("Thread {0} ended ".format(name))
    
threads=[]
for i in range(3): #0,1,2 threads formed here 
    print("Main :: creating and starting  thread {0}".format(i,))
    t =Thread(target = thread_funtion,args=(i,))
    threads.append(t)
    t.start()
for i,thread in enumerate(threads):
    print("Main :: before joining thread {0}".format(i,))
    thread.join()
    print("Main :: after joining thread {0}".format(i,))
    