# problem 3 Level 3
# list of tuples with department and employee count
# need to find total employees

departments = [("IT", 10), ("HR", 5), ("Finance", 8)]

total_count = 0

for dept in departments:
    total_count = total_count + dept[1]   # dept[1] means second value in tuple

print("Total number of employees across all departments :" , total_count)