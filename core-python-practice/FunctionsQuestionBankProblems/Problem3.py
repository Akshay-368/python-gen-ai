# problem 3 
# parameterized email generator 

def gen_email(nam, dept, jdate):
    msg = "Dear " + nam + ", welcome to " + dept + ". Your joining date is " + jdate + "."
    print(msg)
    return msg

gen_email("Neha", "Engineering", "2025-11-10")

# many parameters - good to use keyword args sometimes