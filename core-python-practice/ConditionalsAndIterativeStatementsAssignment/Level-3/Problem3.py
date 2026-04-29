# problem 9  levle 3
# compound interest calculator 
# using while loop to show amount each year

prin = float(input("Enter principal amount : "))
rate = float(input("Enter rate (%) : "))
yrs = int(input("Enter number of years : "))

yr = 1

while ( yr <= yrs ) :
    prin = prin * (1 + rate/100)     # compound interest formula
    print("Year" , yr , ":" , round(prin , 2))
    yr = yr + 1

# while loop runs for given number of years 
# each time we update principal with new amount