# problem 8 
# dynamic function router 
# call function based on command name 

def invoke(cmd, cmds):
    if cmd in cmds:
        result = cmds[cmd]()      # calling the function 
        print(result)
    else:
        print("Command not found")

invoke("start", {"start": lambda: "System started"})