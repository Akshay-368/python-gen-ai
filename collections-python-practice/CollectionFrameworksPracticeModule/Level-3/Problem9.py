# problem 9 
# word frequency analyzer 
# count how many times each word appears 

text = "great service and great experience"

words = text.lower().split()     # make small case and split

countw = {}

for w in words:
    if w in countw:
        countw[w] = countw[w] + 1
    else:
        countw[w] = 1

print(countw)

# simple dictionary counting 
# in real life people use Counter but this is more basic