import logging 
import threading 
import time


def thread_function(name):
    logging.info("Thread  %s : starting",name)
    time.sleep(4)
    logging.info("Thread %s : finishing ",name)
    



if __name__=="__main__":
    format="%(asctime)s: %(message)s"
    logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("main:before  starting a thread ")
    
    x=threading.Thread(target = thread_function,args=(1,))
    logging.info("main: before running thread")
    #start a thread
    x.start()
    logging.info("main wait for thread to finish")
    x.join()
    logging.info("main: All operations are done finally ")