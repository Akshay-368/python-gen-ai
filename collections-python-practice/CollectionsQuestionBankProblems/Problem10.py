# problem 10 
# product inventory comparator 
# find difference between two warehouses using Counter

# Counter can do subtraction directly 

from collections import Counter

w1 = Counter({"A": 10, "B": 5})
w2 = Counter({"A": 8, "B": 7})

diff = w1 - w2
print(diff)

# positive means w1 has extra 
# negative means w2 has extra