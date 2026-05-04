# problem 2 
# recursive directory size calculator 

# recursion = function calling itself 
# same idea in c# and js but can crash if too deep

def calc_size(tree):
    total = 0
    for k in tree:
        if isinstance(tree[k], dict):      # if its folder
            total = total + calc_size(tree[k])
        else:
            total = total + tree[k]        # its a file size
    return total

data = {"dir1": {"file1": 2, "file2": 3}, "dir2": {"file3": 5}}
print(calc_size(data), "MB")