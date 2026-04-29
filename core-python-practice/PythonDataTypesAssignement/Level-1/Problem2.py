# problem 2  level 1
# taking temperature from user as string then converting to float
# then showing both celsius and fahrenheit

temp = input("Enter temperature in Celsius : ")   # user gives input as string

c = float(temp)      # converting string to float and storing in c

f = (c * 9/5) + 32   # formula to convert celsius to fahrenheit

print ( "Temperature in Celsius : " , c )
print ( "Temperature in Fahrenheit : " , f )

# i used short names c and f to keep it simple