# problem 2 
# dynamic template formatter 
# replace {name} and {city} with real values 

# .format() is easy in python 
# in c# we use string interpolation $"" 
# in js we use template literals `${}` 

def format_temp(temp, data):
    msg = temp.format(name = data["name"], city = data["city"])
    print(msg)
    return msg

template = "Hello {name}, welcome to {city}!"
info = {"name": "Alex", "city": "Bengaluru"}

format_temp(template, info)