# problem 4 level 2 
# production target checker 
# find which days production was below target

prod = [120, 95, 110, 80]
target = 100

day = 1

for p in prod :
    if ( p < target ) :
        print("Day" , day , ":" , p , "units (below target)")
    day = day + 1

# i used day variable to show day number 
# for loop goes through each production value