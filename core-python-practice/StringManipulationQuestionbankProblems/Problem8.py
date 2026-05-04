# problem 8 
# multi language accent cleaner 

text = "Crème brûlée à la carte"

clean = text.replace("é", "e")
clean = clean.replace("è", "e")
clean = clean.replace("ê", "e")
clean = clean.replace("à", "a")
clean = clean.replace("ü", "u")

print(clean)

# this is manual way 
# in real code unicodedata is used but keeping basic