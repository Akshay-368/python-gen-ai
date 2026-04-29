# problem 5 levle 2
# attendance validator 
# check attendance percentage and give feedback

att = float(input("Enter attendance percentage : "))

if ( att >= 90 ) :
    print("Excellent")
elif ( att >= 75 ) and ( att <= 89 ) :
    print("Satisfactory")
else :
    print("Poor")

# used if elif else to check different ranges 
# kept variable att short for attendance