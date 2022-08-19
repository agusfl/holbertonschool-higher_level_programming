#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header:

- You must use the packages requests and sys
- You are not allow to import other packages than requests and sys
- The value of this variable is different for each request
- You don’t need to check script arguments (number and type)
Attribute "headres": 
https://www.geeksforgeeks.org/response-headers-python-requests/
"""
if __name__ == "__main__":
    import requests
    from sys import argv  # for command line arguments

    url = argv[1]  # get url from the command line
    req = requests.get(url)  # request the url with GET method
    # Request key "X-Request-Id" from the header
    answer = req.headers.get('X-Request-Id')
    print(answer)
