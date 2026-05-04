# problem 4 
# top 3 most used commands 
# using Counter to find most common 

# Counter is like smart dictionary for counting 
# in c# we make our own with Dictionary 
# in js people use reduce or loop 

from collections import Counter

cmds = ["init", "push", "push", "commit", "push", "init"]

count_cmd = Counter(cmds)

top3 = count_cmd.most_common(3)
print(top3)