#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8):

- You have to manage urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
- You must use the packages urllib and sys
- You are not allowed to import other packages than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement
"""
if __name__ == "__main__":
    from sys import argv  # for command line arguments
    import urllib.request

    try:
        URL = argv[1]
        with urllib.request.urlopen(URL) as response:
            content = response.read().decode()
            print(content)
    except urllib.error.URLError as e:
        print("Error code:", e.code)
