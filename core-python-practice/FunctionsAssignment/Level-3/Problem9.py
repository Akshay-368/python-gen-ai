# problem 9 
# recursive fibonacci 
# generate fib series using recursion 

def gen_fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = gen_fib(n-1)           # recursive call 
    fib.append(fib[-1] + fib[-2])
    return fib

print(gen_fib(6))

# recursion is simple but slow for big numbers 
# in c# and js same logic but same performance issue