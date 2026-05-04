# problem 4 
# html tag sanitizer 
# remove dangerous tags keep only b i p 

html = "<p>Bold <script>alert</script> <b>text</b></p>"

clean = html.replace("<script>", "")
clean = clean.replace("</script>", "")

print(clean)

# this is very basic version 
# real sanitizer is complicated so keeping simple for now