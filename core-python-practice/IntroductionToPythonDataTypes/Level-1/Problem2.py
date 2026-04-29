# problem number 2 
# hr system gave number of employees as string "250"
# i have to convert it into integer and then add 10 new hires

number_of_employees = "250"     # this is string right now

# converting string to integer using int()
total_employees = int(number_of_employees)

total_employees = total_employees + 10   # adding 10 new hires

print("After adding 10 new hires , total employees are :" , total_employees)