# problem 5 level 2
# making a dictionary to store employee data
# then getting data by employee id

emp = {
    "e1" : {"nam":"Rahul", "sal":75000},
    "e2" : {"nam":"Priya", "sal":82000},
    "e3" : {"nam":"Aman", "sal":45000}
}

id = input("Enter employee ID (e1 or e2 or e3) : ")

if id in emp:
    print("Name :" , emp[id]["nam"])
    print("Salary :" , emp[id]["sal"])
else:
    print("Sorry employee ID not found")