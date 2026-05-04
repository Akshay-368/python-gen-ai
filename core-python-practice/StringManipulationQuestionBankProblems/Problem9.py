# problem 9 
# audit log signature verifier 

logs = ["Event A --signed", "Event B", "Event C --signed"]

unsigned = 0

for l in logs:
    if ( not l.endswith("--signed") ) :
        unsigned = unsigned + 1

print("Unsigned Entries :", unsigned)

# endswith is very useful method 
# same in js and c# also exists