#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8):

- The email must be sent in the email variable
- You must use the packages urllib and sys
- You are not allowed to import packages other than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement
"""
if __name__ == "__main__":
    from sys import argv  # for command line arguments
    import urllib.request
    import urllib.parse

    URL = argv[1]
    email = argv[2]

    # Set value to send
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(URL, data)
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
