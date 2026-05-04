# problem 7 level 3 
# duplicate record cleaner 
# remove duplicate records based on id 

# using set to track seen ids 

def remove_dups(records):
    seen = set()
    clean = []
    
    for r in records:
        id_val = r["id"]
        if id_val not in seen:
            seen.add(id_val)
            clean.append(r)
    
    print(clean)
    return clean

data = [{"id": 1}, {"id": 2}, {"id": 1}]
remove_dups(data)