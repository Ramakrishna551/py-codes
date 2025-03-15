import time
import math
def calculate_time(func):
    def inner1(*args,**kwargs):
        begin=time.time()
        func(*args,**kwargs)
        end=time.time()
        print("Total time taken :",func.__name__,end-begin)
    return inner1 

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
  
@calculate_time   
def square(num):
    time.sleep(2)
    print(num*num)

factorial(10)
square(10)