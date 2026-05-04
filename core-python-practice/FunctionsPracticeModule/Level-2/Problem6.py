# problem 6 
# conditional logger 
# only print message when debug is true 

# default parameter debug=False 
# in c# we use optional bool debug = false 
# in js we do debug = debug || false 

def log_msg(msg, debug=False):
    if ( debug == True ) :
        print(msg)          # only print when debug is on
    # else do nothing 

log_msg("Debug mode active", True)
log_msg("This should not show")