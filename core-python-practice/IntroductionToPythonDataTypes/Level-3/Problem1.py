# problem 7 - Level 3
# we have mixed list with strings and numbers
# i need to convert all to integers and find sum

mixed_list = [ "10", 20, "30", 40 ]

sum_total = 0     # starting sum with 0

# using for loop to go through each item
for item in mixed_list:
    integer_value = int(item)     # converting everything to int
    sum_total = sum_total + integer_value

print( "Sum of all numbers after conversion is :" , sum_total )