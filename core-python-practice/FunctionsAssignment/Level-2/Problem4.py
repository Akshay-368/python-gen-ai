# problem 4 level 2 
# data normalizer 
# make all names lowercase and remove extra spaces 

def norm_names(nlist):
    clean = []
    for n in nlist:
        clean.append(n.strip().lower())     # remove spaces and lowercase
    print(clean)
    return clean

norm_names([" John ", "MARY", " Alex "])