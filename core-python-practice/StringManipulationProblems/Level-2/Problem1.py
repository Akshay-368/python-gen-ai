# problem 4 level 2 
# url parser 
# separate base url and path from full url

# in python we can use split() 
# there is also urllib but im not using it because its bit advanced for beginner
# in js we have URL object which is easier 
# in c# we use Uri class - much more strict and object oriented

def parseurl(url):
    parts = url.split("/")     # split by forward slash
    
    base = parts[0] + "//" + parts[2]     # https://example.com
    path = "/" + "/".join(parts[3:])      # /products/item1
    
    print("Base URL :" , base)
    print("Path :" , path)

parseurl("https://example.com/products/item1")