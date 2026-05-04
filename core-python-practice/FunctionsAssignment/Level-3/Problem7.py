# problem 7 level 3 
# recursive directory scanner 
# this one is advanced recursion + files 

# i am making simple version because recursion is confusing at 3am 

def scan_dir(path):
    print("Scanning :", path)
    # real code would use os module but keeping simple for now
    # recursion means function calling itself 
    # same idea in c# and js but risk of stack overflow

# for now just printing 
scan_dir("/project/logs")