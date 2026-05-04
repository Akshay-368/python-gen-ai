# problem 4 level 2 
# dynamic report title generator 

def format_title(title, dept="Analytics"):
    final = dept + " Report: " + title
    print(final)
    return final

format_title("Sales Summary")

# default parameter dept="Analytics" 
# if user doesnt give department it uses default 
# in c# we use optional parameters 
# in js we use || or default in function params