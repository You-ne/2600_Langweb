import functools, inspect

def         checktypes(f):
    
    @wraps(f)
    def     checker(*arg, **karg):
        
        def type_check(*arg, **karg):
            errors[] = None

            for var in karg:

        #Check vars type for an error
        if !(type_check(arg, karg) == 'good'):
            raise Exception(errors)
        
        #Else run the decorated function
        else:            
            return f(*args, **kw)
       
    #Why isn't the coding part just here??? Wtf wrap
    return checker  
