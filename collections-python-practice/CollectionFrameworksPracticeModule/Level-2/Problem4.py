# problem 4 level 2 
# sales frequency tracker 
# count how many times each product sold 

# using Counter because its perfect for counting 
# in c# we make dictionary and increment manually 
# in js people use reduce function 

from collections import Counter

items = ["TV", "TV", "Laptop", "Phone", "Laptop"]

count_items = Counter(items)
print(dict(count_items))