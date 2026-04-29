# problem 6 levle 2
# list of sales amounts 
# finding average and rounding to 2 decimal places

sales = [1200, 4500, 3200, 6700, 2300]

total = 0
count = 0

for s in sales:
    total = total + s     # adding each sale to total
    count = count + 1     # counting how many sales

avg = total / count       # calculating average

print("Average sales amount is :" , round(avg, 2))