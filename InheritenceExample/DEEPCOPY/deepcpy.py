from copy import deepcopy
def passbyvalue(func):
    def new(*args1):
        cargs1=[deepcopy(arg) for arg in args1]
       
        return func(*cargs1)
    return new 
@passbyvalue
def myfunc(a):
    a.append(3)
    return a
a=[1]
b= myfunc(a)
print(b)
a[0]=2
print(b)
print(" ")
#deepcopy here 
print("deep copy ")
print(" ")
x=[20]
y=deepcopy(x)
x[0]=30
print(x)
print(y)
