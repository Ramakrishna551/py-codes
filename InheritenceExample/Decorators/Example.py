def claculate_time(fun):
     def inner1(*args,**kwargs):
        print("Before exec....")
        returnValue=fun(*args,**kwargs)
        print("After exec")
        
        return returnValue
        
     return inner1    

@claculate_time   
def sum(x,y):
    print("this is sum function ")
    return x+y
x,y =2,5
print("Sum is ",sum(x,y))
    