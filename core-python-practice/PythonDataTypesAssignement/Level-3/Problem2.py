# problem 8
# reading csv like string "23,45,67,12"
# converting to integers then finding mean and max

data = "23,45,67,12"

nums = data.split(",")     # splitting by comma

total = 0
count = 0
maxi = 0

for n in nums:
    val = int(n)           # converting string to int
    total = total + val
    count = count + 1
    
    if val > maxi:
        maxi = val

mean = total / count

print("Mean value is :" , round(mean, 2))
print("Maximum value is :" , maxi)