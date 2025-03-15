def hello_decorator(func):
    #inner1 is a function i.e wrapper 
    def inner1():
        print("Hello this is  before function exxecution")
        func()
        print("this is after execution")
    return inner1
    
def function_to_be_used():
    print("this is inside the function")
#passing funtion_to_be_used inside the decoartor to control its behavoir
function_to_be_used=hello_decorator(function_to_be_used)
#calling a function
function_to_be_used()