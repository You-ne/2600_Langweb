import inspect
from functools import wraps

# a revoir, pas opti

def checktypes(function):
    @wraps(function)
    def checker(*args, **kws):
            
        #Loads function signature, param names, and annotations dict 
        fsign = inspect.signature(function)
        fparams = [param for param in fsign.parameters]          
        assigned_t = function.__annotations__      
        
        #If no assigned types, nothing to check
        if not assigned_t:
            return(function(*args, **kws))
            
        #Else check non arbitrary arguments
        else:
            i = 0
            for param  in fparams:
                if param in assigned_t:
                        
                    awaited_t = str(assigned_t[param])[8:-2]
                    if awaited_t[0] == '_':
                        awaited_t = awaited_t[9:]
                    arg_t = str(type(args[i]))[8:-2]
                    if arg_t[0] == '_':
                        arg_t = arg_t[9:]
                        
                    if arg_t != awaited_t:
                        raise Exception(f'f: wrong type of \'{param}\' argument, \'{awaited_t}\' expected, got \'{arg_t}\'')
                i += 1

            #If no error raised within args, run the function and checks return's type if assigned
            if assigned_t['return']:
                result = function(*args, **kws)
                result_t = str(type(result))[8:-2]
                awaited_ret_t = str(assigned_t['return'])[8:-2]
                if result_t != awaited_ret_t:
                    raise Exception(f'f: wrong return type, {awaited_ret_t} expected, got {result_t}')
                return result
            else:
                return(function(*args, **kws))

    return checker  