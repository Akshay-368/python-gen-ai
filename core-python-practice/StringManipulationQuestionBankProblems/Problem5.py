# problem 5 
# palindrome sequence detector 
# check which ids are palindromes 

def is_pal(s):
    if ( s == s[::-1] ) :      # reverse and compare
        return True
    return False

ids = ["ABA12", "1221", "XYZ"]
pals = []

for idd in ids:
    if ( is_pal(idd) ) :
        pals.append(idd)

print(pals)

# s[::-1] is python magic to reverse string 
# in c# we need toArray and reverse