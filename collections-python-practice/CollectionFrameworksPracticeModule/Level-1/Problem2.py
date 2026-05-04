# problem 2 
# employee lookup 
# get role by name from dictionary 

# in python .get() is safe if key not found 
# in c# we use TryGetValue 
# in js we use obj["key"] or optional chaining 

def getrole(empdict, nam):
    role = empdict.get(nam)      # safe way 
    print(role)

data = {"Alex": "Engineer", "Priya": "Manager"}
getrole(data, "Priya")