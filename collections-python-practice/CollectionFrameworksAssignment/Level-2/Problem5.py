# problem 5 level-2
# configuration merge tool 
# merge multiple config dicts 
# last one should overwrite if same key 

# in python we can loop and update 
# in c# we have to be careful with reference 
# in js we use spread operator ... which is easier 

def mergeconf(c1, c2):
    result = {}
    
    for k in c1:
        result[k] = c1[k]
    
    for k in c2:
        result[k] = c2[k]      # this will overwrite if key already there
    
    print(result)
    return result

mergeconf({"timeout": 10}, {"timeout": 20, "debug": True})