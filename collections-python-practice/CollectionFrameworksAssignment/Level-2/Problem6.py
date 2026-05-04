# problem 6 Level-2
# list comprehension cleaner 
# remove empty strings and None from list 

# i will use normal for loop instead of list comprehension 
# because user said keep code simple and beginner level 
# comprehension is bit advanced for some new students 

data = ["Alex", "", "John", None, "Riya"]

cleanlist = []

for item in data:
    if item is not None and item != "":     # check not empty and not None
        cleanlist.append(item)

print(cleanlist)

# this way its very clear what is happening step by step