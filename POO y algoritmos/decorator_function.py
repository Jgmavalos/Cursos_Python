def decorator_function(func_param):
    
    def internal_function():
        # additional actions that decorate 
        print("Let's to do a calculation")
        
        func_param()
        # additional actions that decorate
        print('We have finished the calculation ')
    return internal_function

@decorator_function
def suma():
    print(15+20)
    

@decorator_function
def resta():
    print(30-10)
    

suma()
resta()
