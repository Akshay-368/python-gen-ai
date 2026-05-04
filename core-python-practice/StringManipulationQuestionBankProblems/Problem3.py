# problem 3 
# keyword context extractor 
# show few words before and after keyword 

para = "Python is powerful and widely used in data engineering and automation."
key = "data"

words = para.split()          # split into list of words

for i in range(len(words)):
    if ( words[i] == key ) :
        start = max(0, i-5)
        end = min(len(words), i+6)
        context = " ".join(words[start:end])
        print("Context :", context)