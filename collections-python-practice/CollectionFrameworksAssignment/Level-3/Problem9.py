# problem 9 Level-3
# employee data serializer 
# convert list of tuples to list of dictionaries 

emps = [("Alex", "IT"), ("Riya", "HR")]

result = []

for e in emps:
    dic = {}
    dic["name"] = e[0]
    dic["department"] = e[1]
    result.append(dic)

print(result)

# this is simple way using loop 
# in real projects people use list comprehension but this is easier to read at 3am lol