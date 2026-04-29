# problem 1 level 1 
# department greeting script 
# alex wants to make a function that makes welcome message 
# using name and department

# in python we use def to make function 
# in c# it would be like static string MakeGreeting() with capital letter 
# in js or typescript we use function keyword or arrow function 
# big difference is python doesnt need semicolon at end of lines like js and c#

def greet(nam, dept):
    msg = "Welcome " + nam + " to the " + dept + " department!"
    print(msg)
    # i used + to join strings , could also use f string but keeping it simple

# calling the function
greet("John", "Finance")