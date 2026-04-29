# problem 6  levle 2
# csv text cleaner 
# remove extra commas , symbols and fix spacing

# this is very common task 
# python makes string cleaning super easy with replace and join
# in c# you might need to use regex which is more complicated for beginners
# in js also people use regex a lot

def cleancsv(text):
    text = text.replace( "!!", "")     # remove unwanted symbols
    text = text.replace(",,", "," )    # fix double commas
    text = text.replace("  ", " ")    # remove extra spaces
    
    parts = text.split( ",")           # split by comma
    cleanparts = []
    
    for p in parts:
        cleanparts.append(p.strip())  # remove spaces from each part
    
    final = ",".join(cleanparts)
    print(final)

cleancsv("John,, Doe!!, New York ")