# problem 9 levl 3
# nested dictionary for departments and employees
# user enters department and we show all employees in it

depts = {
    "it" : [
        {"nam":"Rahul", "role":"dev"},
        {"nam":"Sneha", "role":"tester"}
    ],
    "hr" : [
        {"nam":"Priya", "role":"manager"}
    ],
    "fin" : [
        {"nam":"Aman", "role":"accountant"},
        {"nam":"Rohit", "role":"analyst"}
    ]
}

dep = input( "Enter department (it / hr / fin) : " ).lower()

if dep in depts:
    print (  "Employees in" , dep , "department : " )
    for e in depts[dep]:
        print (e["nam"] , "-" , e["role"])
else:
    print("Department not found")