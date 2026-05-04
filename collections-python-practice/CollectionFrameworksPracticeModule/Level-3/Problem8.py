# problem 8 
# inventory availability checker 
# find which items are in orders but not in inventory 

orders = {101, 102, 103}
inventory = {101, 103}

missing = orders - inventory     # set difference 
print("Missing items :", missing)

# set difference is super useful 
# in c# we use Except() 
# in js we need manual filter