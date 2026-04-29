# problem 6  levle 2
# odd number printer with skip 
# print odd numbers from 1 to 30 but skip multiples of 5

for i in range(1 , 31) :
    if ( i % 2 ) == 0 :
        continue          # skip even numbers
    
    if ( i % 5 ) == 0 :
        continue          # skip multiples of 5
    
    print(i)

# continue statement skips the current iteration and moves to next
# range(1,31) gives numbers from 1 to 30