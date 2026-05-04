# problem 11 
# error logging decorator 

def err_log(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Error Logged:", str(e))
            # in real code we would write to file
    return wrapper

@err_log
def divide(a, b):
    return a / b

divide(10, 0)