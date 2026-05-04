# problem 5 
# employee skill mapping 
# reverse it - show skill to list of employees 

# using defaultdict(list) 
# this is reverse mapping 

from collections import defaultdict

emp_skill = {"Alex": ["Python", "SQL"], "Neha": ["SQL"], "Sam": ["Python"]}

skill_to_emp = defaultdict(list)

for emp in emp_skill:
    for sk in emp_skill[emp]:
        skill_to_emp[sk].append(emp)

print(dict(skill_to_emp))