# problem 7 level 3 
# order processing simulator 
# stop when we find Failed status using break

orders = ["Pending", "Processing", "Delivered", "Failed", "Pending"]

for o in orders :
    if ( o == "Failed" ) :
        print("Processing stopped due to Failed status.")
        break
    
    print("Processing order :" , o)

# break statement stops the loop immediately when condition is true