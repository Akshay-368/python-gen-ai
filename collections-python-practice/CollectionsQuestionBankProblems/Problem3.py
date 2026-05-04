# problem 3 
# unique visitor tracker 
# use set to remove duplicate visitor ids

# set only keeps unique values 
# in c# HashSet 
# in js new Set() 
# super useful for counting unique things

vis = ["A123", "B234", "A123", "C345"]

unique_vis = set()

for v in vis:
    unique_vis.add(v)

print("Unique Visitors :", len(unique_vis))