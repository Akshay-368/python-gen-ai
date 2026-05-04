# problem 12 
# function retry wrapper 

def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    print("Attempt", i+1, "failed")
            print("All attempts failed")
        return wrapper
    return decorator

@retry(times=3)
def unstable():
    raise Exception("Network error")

unstable()