# problem 7 level 3 
# transaction validator 
# filter only valid transactions 

# valid means amount > 0 and status Approved 

def val_trans(trans):
    clean = []
    for t in trans:
        if ( t["amount"] > 0 ) and ( t["status"] == "Approved" ) :
            clean.append(t)
    
    print(clean)
    return clean

data = [
    {"id": 1, "amount": 100, "status": "Approved"},
    {"id": 2, "amount": -50, "status": "Pending"}
]

val_trans(data)

# used normal for loop instead of list comprehension 
# because its easier to understand for beginners at 3am