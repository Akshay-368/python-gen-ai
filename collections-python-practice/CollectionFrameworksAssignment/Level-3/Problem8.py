# problem 8 Level-3
# top n frequent words 
# count words and show top n most used 

# i will not use Counter because it might be advanced for beginners 
# doing it with normal dictionary 

def topwords(text, n):
    words = text.split()          # split into words
    countd = {}
    
    for w in words:
        if w in countd:
            countd[w] = countd[w] + 1
        else:
            countd[w] = 1
    
    # simple sort by count (beginner way)
    items = []
    for k in countd:
        items.append((k, countd[k]))
    
    items.sort(key=lambda x: x[1], reverse=True)   # sort by count big to small
    
    print(items[:n])     # first n items

topwords("great service great product", 2)