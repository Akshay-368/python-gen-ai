# problem 2  level 1
# filename formatter 
# need to clean file names - remove spaces and make lowercase

# in python we have .replace() and .lower() 
# in c# we use Replace() and ToLower() - note the capital letters 
# in javascript its also replace() and toLowerCase() but syntax is bit different

def cleanfile(fname):
    clean = fname.replace(" ", "_")   # replace space with underscore
    clean = clean.lower()             # make everything small letters
    print(clean)

cleanfile("My Report FINAL .txt")