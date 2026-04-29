# problem 2 Level 3
# creating nested dictionary for employees
# then print names of employees who earn more than 50000

employees = {
    "emp1" : {"name": "Rahul", "role": "Developer", "salary": 65000},
    "emp2" : {"name": "Priya", "role": "Manager", "salary": 82000},
    "emp3" : {"name": "Aman", "role": "Tester", "salary": 45000}
}

print("Employees earning above 50000 :")

for emp in employees:
    if employees[emp]["salary"] > 50000:
        print(employees[emp]["name"])