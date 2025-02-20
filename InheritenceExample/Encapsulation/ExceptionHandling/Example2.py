class MyException(Exception):
    def __init__(self):
        super(Exception,self).__init__()
        self.args=("Raised Myexception",)

try:
    raise MyException()
except MyException as exe:
    print(exe)
    
    
        