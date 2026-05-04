# problem 5 
# departmental budget merge 
# add budgets from two different dicts 

# if same dept then add the values 

bud1 = {"IT": 10000, "HR": 8000}
bud2 = {"IT": 5000, "Finance": 7000}

final_bud = {}

for k in bud1:
    final_bud[k] = bud1[k]

for k in bud2:
    if k in final_bud:
        final_bud[k] = final_bud[k] + bud2[k]
    else:
        final_bud[k] = bud2[k]

print(final_bud)

# this is simple way without using update 
# easy to understand at 3am