#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.

- You must use the packages urllib and sys
- You are not allow to import packages other than urllib and sys
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use a with statement
How to get header info using get:
https://stackoverflow.com/questions/43344819/reading-response-headers-with-
fetch-api
"""
if __name__ == "__main__":
    from sys import argv  # for command line arguments
    import urllib.request

    URL = argv[1]
    with urllib.request.urlopen(URL) as response:
        # Obtenemos el dato especifico del header que nos piden "X-Request-Id"
        content = response.headers.get('X-Request-Id')
        print(content)
