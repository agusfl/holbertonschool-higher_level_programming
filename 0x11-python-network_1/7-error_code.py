#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
body of the response:

- If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)
"""
if __name__ == "__main__":
    import requests
    from sys import argv  # for command line arguments

    url = argv[1]  # get url from the command line
    req = requests.get(url)  # request the url with GET method
    # Si se pudo hacer un GET se devuelve e imprime
    if req:
        print(req.text)
    # sino se imprime le mensaje de error
    else:
        print("Error code:", req.status_code)
