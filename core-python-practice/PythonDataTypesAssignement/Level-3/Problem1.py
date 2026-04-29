# problem 7 level 3
# dictionary of lists for monthly revenue of different branches
# finding the branch with highest total revenue

rev = {
    "del" : [45000, 52000, 48000],   # delhi branch
    "mum" : [67000, 71000, 69000],   # mumbai
    "ban" : [39000, 42000, 41000]    # bangalore
}

high = 0
best = ""

for b in rev:
    sum_rev = 0
    for r in rev[b]:
        sum_rev = sum_rev + r
    
    print("Total revenue of" , b , "is" , sum_rev)
    
    if sum_rev > high:
        high = sum_rev
        best = b

print("Branch with highest revenue is" , best , "with" , high)