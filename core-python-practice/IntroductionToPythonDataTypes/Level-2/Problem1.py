# problem 1 - Level 2
# project dashboard has a tuple of project codes
# tuple is immutable means we cannot change it

project_codes = ( "P001", "P002", "P003", "P004" )

print ( "All project codes are : " )
print(project_codes)

# now lets try to change one element to see if its really immutable
# project_codes[0] = "P999"     # if i remove the # it will give error

try :
	project_codes[0] = "P999"
except Exception as e:
	print ( f"\nTuple is immutable so we cannot change values inside it \nhere is the message of the exception as well : \n{e}" )