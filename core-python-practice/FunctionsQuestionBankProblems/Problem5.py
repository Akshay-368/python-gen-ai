# problem 5 
# function execution timer decorator 

import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print("Execution Time:", round(end-start, 3), "s")
        return result
    return wrapper

@timer
def test():
    sum(range(100000))

test()