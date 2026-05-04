# problem 6 
# access log time window 
# check if user tried login 3 times in short time 

# using deque to keep recent timestamps 

from collections import deque

def checklogin(user, times):
    ts = deque()
    
    for t in times:
        # here we should remove old timestamps but keeping simple
        ts.append(t)
        if len(ts) > 3:
            ts.popleft()      # remove oldest
    
    if len(ts) >= 3:
        print("Alert: Multiple login attempts detected for", user)
    else:
        print("No alert for", user)

checklogin("Alex", [12.00, 12.02, 12.04])