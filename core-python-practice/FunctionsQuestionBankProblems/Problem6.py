# problem 6 
# dynamic argument aggregator using *args 

def aggregate(*args):
    total = 0
    for a in args:
        total = total + a
    count = len(args)
    avg = total / count if count > 0 else 0
    print( (total, round(avg,1), count) )
    return (total, round(avg,1), count)

aggregate(10, 20, 30, 40)

# *args lets us take any number of arguments 
# very useful feature in python