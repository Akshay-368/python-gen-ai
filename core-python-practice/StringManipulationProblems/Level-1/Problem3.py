# problem 3  levle 1
# product id normalizer 
# make all product ids in same format - uppercase and with hyphen

# in python we use .upper() and .replace()
# in c# it would be .ToUpper() and .Replace()
# in typescript/js its .toUpperCase() 
# important difference - python is case sensitive in method names while c# uses PascalCase

def fixid(ids):
    newlist = []
    for i in ids:
        temp = i.upper()           # make capital
        temp = temp.replace("_", "-")   # change underscore to hyphen
        newlist.append(temp)
    
    print(newlist)

fixid(["prod-001", "PROD_002", "prod-003"])