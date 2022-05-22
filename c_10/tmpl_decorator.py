# this is a very reusable pattern for creating decorators

from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute Before calling the decorated function.
        # 2. Calling the decorated function and returning from the results received from it 
        #    return func(*args, **kwargs)
        # 3. Code to execute instead of calling, decorate functions
     return wrapper     