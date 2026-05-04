# problem 4 level 2 
# department employee aggregator 
# group employees by their departments 

# i will use normal dict not defaultdict because that might be advanced 
# in c# we use Dictionary<string, List<string>> 
# in js object with arrays 

data = [("IT", "Alex"), ("HR", "Riya"), ("IT", "John")]

groups = {}

for d in data:
    dept = d[0]
    emp = d[1]
    
    if dept not in groups:
        groups[dept] = []         # create empty list if new dept
    
    groups[dept].append(emp)      # add employee to that dept list

print(groups)