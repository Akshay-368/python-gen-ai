# problem 2 
# department wise salary aggregation 
# using defaultdict to sum salaries easily

# defaultdict is nice because it gives default value 0 for int 
# in c# we use Dictionary and check if key exists 
# in js we use object and || 0 

from collections import defaultdict

sal = [("IT", 5000), ("HR", 3000), ("IT", 4000)]

dept_sal = defaultdict(int)

for d in sal:
    dept = d[0]
    amt = d[1]
    dept_sal[dept] = dept_sal[dept] + amt     # auto adds 0 if new

print(dict(dept_sal))     # converting back to normal dict for print