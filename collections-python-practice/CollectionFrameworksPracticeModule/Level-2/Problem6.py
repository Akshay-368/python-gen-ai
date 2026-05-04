# problem 6 
# student grade mapping 
# combine names and grades using zip 

# zip is used to pair two lists 
# in c# we use Zip() method 
# in js we need manual loop or libraries 

names = ["Alex", "John", "Riya"]
grades = ["A", "B", "A+"]

result = {}

i = 0
for n in names:
    result[n] = grades[i]
    i = i + 1

print(result)

# i used loop instead of dict(zip) to keep it basic