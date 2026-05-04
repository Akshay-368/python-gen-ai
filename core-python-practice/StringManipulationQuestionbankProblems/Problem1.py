# problem 1 
# log anonymization engine 
# alex needs to hide emails and ips in logs 

# in python we can use replace for simple cases 
# in c# we would use Regex.Replace 
# in js also regex is common 
# keeping it super basic with string replace 

log = "Error reported by user john.doe@corp.com from 192.168.0.21"

cleanlog = log.replace("john.doe@corp.com", "[EMAIL_MASKED]")
cleanlog = cleanlog.replace("192.168.0.21", "[IP_MASKED]")

print(cleanlog)

# in real project we need proper pattern matching but this is beginner way