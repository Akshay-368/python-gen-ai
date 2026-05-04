# problem 3 
# discount price calculator 

def disc_price(prc, disc):
    final = prc - (prc * disc / 100)
    print(final)
    return final

disc_price(1000, 10)

# basic math again 
# always good to return value from function