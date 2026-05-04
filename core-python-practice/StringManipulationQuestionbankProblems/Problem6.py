# problem 6 
# email domain normalizer 
# make everything lowercase and clean spaces 

emails = ["Alex@Corp.COM ", "sam@corp.com", "neha@Corp.com"]
clean_emails = []

for e in emails:
    clean = e.strip().lower()      # remove spaces and lowercase
    clean_emails.append(clean)

print(clean_emails)

# strip removes extra spaces from start and end 
# lower makes all small letters