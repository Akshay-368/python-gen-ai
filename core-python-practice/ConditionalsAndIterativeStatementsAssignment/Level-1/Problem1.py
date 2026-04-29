# problem 1 level 1 
# even or odd checker 
# alex is making a tool to check if number is even or odd

num = int(input("Enter a number : "))

if ( num % 2 ) == 0 :
    print(num , "is Even")
else :
    print(num , "is Odd")

# i used % operator to check reminder when divided by 2 
# if reminder is 0 then its even