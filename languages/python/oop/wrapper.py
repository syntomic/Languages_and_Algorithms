from functools import wraps 

def log(text=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            if text is None:
                print('{} {}():'.format('excute', func.__name__))
            else: 
                print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('ex')
def now():
    print('2324')

print(now.__name__) # now = log(text)(now)
