# problem 4 
# higher order function for validation 

def is_num(val):
    return val.isdigit()

def validate_all(rule, items):
    for i in items:
        if not rule(i):
            print(False)
            return False
    print(True)
    return True

validate_all(is_num, ["123", "456", "78A"])