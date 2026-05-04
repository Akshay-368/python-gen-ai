# problem 7 
# financial report token parser 
# extract currency and amounts 

report = "Q1 Revenue: $1200, Q2 Revenue: €1500, Q3: ₹95000"

parts = report.split(",")
result = []

for p in parts:
    p = p.strip()
    for char in p:
        if ( char in "$€₹" ) :
            # very basic way 
            num_part = p.replace(char, "").strip()
            try:
                num = int(num_part)
                result.append( (char, num) )
            except:
                pass

print(result)