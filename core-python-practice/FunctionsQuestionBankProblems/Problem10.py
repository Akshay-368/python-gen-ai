# problem 10 
# function overloading simulator 

def calc(*args):
    if len(args) == 2 and isinstance(args[0], int):
        print(args[0] + args[1])
    elif len(args) == 2 and isinstance(args[0], str):
        print(args[0] * args[1])
    else:
        print("Not supported")

calc(2, 3)
calc("Hi", 3)