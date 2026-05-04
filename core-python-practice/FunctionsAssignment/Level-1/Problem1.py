# problem 1 from FunctionsPythonAssignement.pdf level 1 
# tax calculator 
# need to make function that calculates net salary after tax 

# in python we use def to define function 
# in c# its static double CalculateNetSalary() with capital name 
# in js / typescript we use function or const arrow function 
# python no need of semicolon and return type 

def calc_net(gross, taxrate):
    taxamt = gross * (taxrate / 100)      # calculate tax amount
    net = gross - taxamt
    return net

print(calc_net(50000, 10))

# kept variable names short like gross taxrate net 
# simple arithmetic inside function