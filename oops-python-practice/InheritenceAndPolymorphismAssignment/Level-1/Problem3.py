# problem 3 
# class variable inheritance 

class Company:
    name = "TechCorp"      # class variable shared by all 

class HR(Company):
    pass

class IT(Company):
    pass

print(HR.name)
print(IT.name)

# class variables are shared 
# same in c# static variables and js static properties