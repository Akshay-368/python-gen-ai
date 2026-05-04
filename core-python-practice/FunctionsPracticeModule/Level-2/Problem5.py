# problem 5 level 2 
# bulk addition utility 
# alex wants a function that can add any number of numbers 

# *numbers means we can give as many arguments as we want 
# in python this is called *args 
# in c# its params int[] numbers 
# in js we use ...numbers rest parameter 

def sum_all(*nums):
    total = 0
    for n in nums:
        total = total + n     # adding one by one 
    print(total)
    return total

sum_all(10, 20, 30, 40)

# could also use sum(nums) but doing loop to keep it basic and clear