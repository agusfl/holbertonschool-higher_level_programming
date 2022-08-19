#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status:

- You must use the package requests
- You are not allow to import packages other than requests
- The body of the response must be display like the following example
(tabulation before -)
Info atributes for package requests:
https://www.geeksforgeeks.org/python-requests-tutorial/
"""
if __name__ == "__main__":
    import requests

    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    # .text - atributo de requests para imprimir en formato texto
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
