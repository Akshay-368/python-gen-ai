# problem 7 level 3 
# category wise sales aggregator 
# add up sales for same category 

sales = [("Electronics", 1000), ("Furniture", 2000), ("Electronics", 1500)]

totals = {}

for s in sales:
    cat = s[0]
    amt = s[1]
    
    if cat not in totals:
        totals[cat] = 0
    
    totals[cat] = totals[cat] + amt     # add to existing total

print(totals)