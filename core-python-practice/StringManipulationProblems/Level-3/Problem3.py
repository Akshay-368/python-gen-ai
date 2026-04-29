# problem 9  level 3
# text compression simulation 
# replace repeating characters with char + count like aaabb -> a3b2

# this is simple version of run length encoding
# in python we use loop and counter 
# in c# or js we would do almost same logic but syntax is different
# important thing - python doesnt have ++ like c# and js , we do = var + 1

def compress(txt):
    if not txt:           # if text is empty
        print("")
        return
    
    result = ""
    cnt = 1
    
    for i in range(1, len(txt)):
        if ( txt[i] == txt[i-1] ) :
            cnt = cnt + 1
        else :
            result = result + txt[i-1] + str(cnt)
            cnt = 1
    
    result = result + txt[-1] + str(cnt)   # add last group
    print(result)

compress("aaabbcdddd")