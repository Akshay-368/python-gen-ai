# problem 1 level 1 
# unique department list 
# alex has duplicate dept names 
# need to remove duplicates using set

# set automatically removes duplicates 
# in c# we use HashSet 
# in js / typescript we use new Set() 
# python set is very easy and fast for this 

depts = ["IT", "Finance", "HR", "Finance", "IT"]

unique_depts = list(set(depts))   # convert to set then back to list
unique_depts.sort()               # sort so it looks neat

print(unique_depts)

# important - set does not keep order so we sorted after 
# in js set also doesnt guarantee order