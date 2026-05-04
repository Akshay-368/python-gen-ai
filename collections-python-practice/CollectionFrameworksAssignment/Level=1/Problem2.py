# problem 2 Level-1
# product price dictionary 
# making dict from two lists - products and prices 

# in python zip() can pair them 
# but im doing it with loop so its more beginner friendly 
# in c# we use Dictionary and loop with index 
# in js we use object and for loop with i 

prods = ["Laptop", "Phone", "Tablet"]
prcs = [70000, 30000, 25000]

price_dict = {}

i = 0
for p in prods:
    price_dict[p] = prcs[i]     # key is product name value is price
    i = i + 1

print(price_dict)

# this way we connect both lists using index 
# simple and clear