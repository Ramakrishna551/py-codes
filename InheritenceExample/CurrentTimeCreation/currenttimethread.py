import logging 
import threading 
import time
if __name__=="__main__":
    format="%(asctime)s: %(message)s"
    logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("main:before  starting a thread ")