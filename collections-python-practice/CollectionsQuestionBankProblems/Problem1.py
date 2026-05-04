# problem 1 
# log retention analyzer using deque 
# alex wants to keep only latest 1000 logs 
# old ones should auto remove when new come

# in python we have collections.deque with maxlen 
# in c# we use Queue or LinkedList with manual check 
# in js we use array and shift() but its slow for big data 
# deque is efficient like circular buffer

from collections import deque

logs = deque(maxlen=1000)   # this will auto remove old when full

for i in range(1005):       # adding 1005 logs to test
    logs.append("Log" + str(i+1))

print("Stored Logs count now :", len(logs))
# it should keep only last 1000 logs 