# problem 9 
# recursive nested dictionary flattener 
# turn nested dict into single level with dot keys 

# recursion is when function calls itself 
# in c# and js also recursion works same but stack limit is there

def flatten(d, prefix=""):
    flat = {}
    
    for k in d:
        newkey = prefix + k if prefix == "" else prefix + "." + k
        
        if isinstance(d[k], dict):      # if value is another dict
            temp = flatten(d[k], newkey)
            flat.update(temp)
        else:
            flat[newkey] = d[k]
    
    return flat

data = {"a": {"b": {"c": 1}}}
print(flatten(data))