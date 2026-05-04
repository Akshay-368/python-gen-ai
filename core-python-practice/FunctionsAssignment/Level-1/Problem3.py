# problem 3 
# word reverser 
# reverse each word in sentence 

def rev_words(sent):
    words = sent.split()       # split into words
    newwords = []
    
    for w in words:
        newwords.append(w[::-1])     # reverse each word using slicing
    
    final = " ".join(newwords)
    print(final)

rev_words("Hello Python Developer")

# [::-1] is python trick to reverse string 
# in c# we use Array.Reverse or manual loop