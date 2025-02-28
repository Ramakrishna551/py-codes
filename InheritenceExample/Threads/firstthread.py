from time import sleep
from threading import Thread

def thread_funtion(name):
    print("Thread {0} started ".format(name))
    sleep(2)
    print("Thread {0} ended ".format(name))
print("Main Thread Started")
t=Thread(target=thread_funtion,args=("New",))
print("Main-Before starting thread ")
t.start()
print("Main-waiting for thread to finish ")
print("Main -Done")