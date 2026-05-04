# problem 3 Level-1
# tuple based coordinates 
# storing fixed x y z values in tuple 

# tuple is immutable like const array in js 
# in c# we can use Tuple or ValueTuple 
# in python once made we cannot change values inside 

cord = (10, 20, 30)     # this is tuple

x, y, z = cord          # unpacking tuple into variables 

print("Coordinates: X=" + str(x) + ", Y=" + str(y) + ", Z=" + str(z))

# unpacking is cool feature in python 
# in js we can do const [x,y,z] = cord also similar