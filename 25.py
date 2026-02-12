# 5. Write a function inside another function.

def outer():
    
    def inner():
        print("This is inner function")
    
    inner() 
outer()      
