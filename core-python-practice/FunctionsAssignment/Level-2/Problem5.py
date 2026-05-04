# problem 5 
# config loader 
# get value from dict with default if not found 

def load_conf(conf, key, defval=None):
    # .get() is safe way in python 
    # in js we use || for default 
    # in c# we use TryGetValue
    val = conf.get(key, defval)
    print(val)
    return val

load_conf({"timeout": 10}, "timeout")