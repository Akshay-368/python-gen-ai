# problem 7 
# case insensitive dictionary 
# headers should ignore case like content-type and Content-Type

# this one is bit hard for beginner 
# we need to make our own class 

class IgnoreCaseDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)     # store in small case
    
    def __getitem__(self, key):
        return super().__getitem__(key.lower())

headers = IgnoreCaseDict()
headers["Content-Type"] = "application/json"
print(headers["content-type"])      # should work same