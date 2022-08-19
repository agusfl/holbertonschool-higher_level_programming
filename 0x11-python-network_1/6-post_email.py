#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response:

- The email must be sent in the variable email
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to error check arguments passed to the script (number or type)
Info post method: https://www.geeksforgeeks.org/post-method-python-requests/
"""
if __name__ == "__main__":
    import requests
    from sys import argv  # for command line arguments

    url = argv[1]  # get url from the command line
    email = argv[2]

    # Set value to send
    values = {'email': email}
    # Post method with requests
    pos = requests.post(url, values)
    print(pos.text)
