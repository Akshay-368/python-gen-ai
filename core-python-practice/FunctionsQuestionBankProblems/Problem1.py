# problem 1 from question bank 
# dynamic dispatcher for tasks 
# call different functions based on task name without many if else

# using dict of functions - very pythonic way 
# in c# we can use Dictionary with delegates 
# in js we use object with function values

def create(d):
    return "Record created"

def dele(d):
    return "Record with ID " + str(d["id"]) + " deleted."

def upd(d):
    return "Record updated"

def dispatcher(task, data):
    cmds = {
        "create" : create,
        "delete" : dele,
        "update" : upd
    }
    if task in cmds:
        result = cmds[task](data)      # calling the right function
        print(result)
    else:
        print("Unknown task")

dispatcher("delete", {"id": 42})