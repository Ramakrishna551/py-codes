from time import sleep
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def thread_funtion(name):
    print("Thread {0} started ".format(name))
    sleep(2)
    print("Thread {0} ended ".format(name))
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_funtion,range(3))