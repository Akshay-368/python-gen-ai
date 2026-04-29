# problem 7 level 3 
# resume keyword extractor 
# find specific skills like Python Django from resume text

# in python we can loop and check if word is in our list
# in c# we use List<string> and Contains()
# in js we use array includes() 
# python is simpler for beginners in this case

def getskills(text):
    skills = ["python", "django", "react"]   # skills we are looking for
    found = []
    
    words = text.lower().split()     # make small case and split into words
    
    for w in words:
        cleanword = w.replace(",", "").replace(".", "")   # remove punctuation
        if cleanword in skills:
            found.append(cleanword.capitalize())
    
    print(found)

getskills("John has experience in Python, Django, and React.")