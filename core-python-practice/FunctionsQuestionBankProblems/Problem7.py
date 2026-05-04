# problem 7 
# api request simulator with default params 

def api_call(url, method="GET", timeout=30, headers=None):
    if headers is None:
        headers = {}
    print("Request:", method, url, "| Timeout:", timeout, "s")

api_call("https://corp.com/api")