# problem 3 
# immutable configuration data 
# using tuple because we dont want anyone to change it 

# tuple is immutable like const in js 
# in c# we can use readonly tuple or record 
# once created we cannot modify values 

config = ("v1.0", "Production")

ver, env = config      # unpacking 

print("Version :", ver)
print("Environment :", env)

# tuples are good for fixed data like this 
# list would allow changes which we dont want