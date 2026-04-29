# problem 5  levle 2
# error report formatter 
# clean messy error logs and make them readable

# python string methods are very easy compared to c# where we need StringBuilder sometimes
# in js we also split and map but arrow functions make it shorter

def fixerror(logs):
    lines = logs.split("\n")      # split into separate lines
    
    for line in lines:
        line = line.strip()       # remove extra spaces
        line = line.replace("ERROR", "Error:")
        line = line.replace("WARNING", "Warning:")
        line = line.replace("at line", "line")
        print(line)

fixerror("ERROR at line12: missing ; \nWARNING at line15: unused variable")