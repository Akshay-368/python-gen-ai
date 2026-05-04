# problem 8 
# recursive factorial calculator 

# recursion = function calling itself 
# same concept in c# and js but python is cleanest syntax 

def fact(n):
    if ( n == 0 ) or ( n == 1 ) :
        return 1                # base case stop recursion
    else:
        return n * fact(n-1)    # recursive call 

print(fact(5))

# 5*4*3*2*1 = 120 
# important to have base case otherwise infinite loop