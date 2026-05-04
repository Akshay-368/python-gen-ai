# problem 8 
# ordered transaction processor 
# use OrderedDict to keep insertion order 

# normal dict also keeps order after python 3.7 
# but OrderedDict is more clear for beginners 

from collections import OrderedDict

trans = [("T1", 100), ("T2", 200), ("T3", 150)]

od = OrderedDict()

for t in trans:
    od[t[0]] = t[1]

print(od)