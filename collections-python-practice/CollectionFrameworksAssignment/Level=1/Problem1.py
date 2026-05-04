# problem 1 level 1 
# customer region tracker 
# alex has list with duplicate regions 
# need to give unique regions and sorted 

# in python we can use set to remove duplicates 
# sets are like unique collections 
# in c# we use HashSet<string> 
# in js we use new Set() 
# big difference - python set is easy to make from list just set(list)

regs = ["APAC", "EMEA", "AMER", "APAC"]

unique = []
for r in regs:
    if r not in unique:     # check if already there
        unique.append(r)

unique.sort()               # sort the list 
print(unique)

# i didnt use set() because some beginners might not know it yet 
# manual way is more basic and easy to understand