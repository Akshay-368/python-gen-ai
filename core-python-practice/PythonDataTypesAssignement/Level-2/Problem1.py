# problem 4 level 2
# taking product name price and discount
# then calculating final price after discount

prod = input("Enter product name : ")
prc = float(input("Enter price : "))        # price as float
disc = float(input("Enter discount rate (like 0.10 for 10%) : "))

final = prc - (prc * disc)     # final price after subtracting discount

print( "Product :" , prod)
print("Original Price : " , prc)
print ( "Final Price after discount  : " , final )