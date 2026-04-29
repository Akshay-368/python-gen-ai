# problem 8  level 3
# template driven email generator 
# replace placeholders in template with real data

# python has .format() which is nice 
# in c# we have string interpolation with $"" 
# in js we have template literals with ` ${} ` - very clean
# but here im using .format() because its basic

def makeemail(template, data):
    msg = template.format(name = data["name"], order_id = data["order_id"])
    print(msg)

temp = "Hello {name}, your order {order_id} is confirmed."
info = {"name": "Alice", "order_id": "12345"}

makeemail(temp, info)