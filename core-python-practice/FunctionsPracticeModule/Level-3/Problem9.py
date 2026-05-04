# problem 9 
# function based menu system 
# show menu and call functions dynamically 

def startproc():
    print("Process Started...")

def stopproc():
    print("Process Stopped...")

def disp_menu(opts):
    for k in opts:
        print(k + ". " + opts[k])
    
    choice = input("Select an option: ")
    
    # simple mapping 
    if ( choice == "1" ) :
        startproc()
    elif ( choice == "2" ) :
        stopproc()
    else:
        print("Invalid option")

menu = {
    "1": "Start Process",
    "2": "Stop Process"
}

disp_menu(menu)

# in real code we can use dict of functions like before 
# but kept it simple with if elif