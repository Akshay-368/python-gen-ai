# problem 8 
# nested function pipeline 

def process(data):
    def clean(txt):
        return txt.strip().upper()
    
    def load(txt):
        return txt + "_PROCESSED"
    
    step1 = clean(data)
    step2 = load(step1)
    print(step2)
    return step2

process(" raw data ")