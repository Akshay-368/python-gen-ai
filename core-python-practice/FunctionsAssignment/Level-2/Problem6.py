# problem 6 
# performance timer 
# measure how long a function takes 

import time     # for timing

def meas_time(func):
    start = time.time()      # record start time
    func()                   # run the function
    end = time.time()        # record end time
    print("Execution time:", end - start, "seconds")

meas_time(lambda: sum(range(100000)))

# higher order function - function that takes another function 
# this concept is similar in js but different in c#