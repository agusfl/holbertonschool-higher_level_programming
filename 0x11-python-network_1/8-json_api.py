#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter:

- The letter must be sent in the variable q
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty, display the id
and name like this: [<id>] <name>
Otherwise:
- Display Not a valid JSON if the JSON is invalid
- Display No result if the JSON is empty
- You must use the package requests and sys
- You are not allowed to import packages other than requests and sys

Info json: https://www.geeksforgeeks.org/response-json-python-requests/
"""
if __name__ == "__main__":
    import requests
    from sys import argv  # for command line arguments

    url = "http://0.0.0.0:5000/search_user"
    # Setear letter como el comando de linea si pasaron uno y sino como ""
    if len(argv) > 1:
        letter = argv[1]  # letter to be sent as a command line argument
    else:
        letter = ""

    # Set value to send
    values = {'q': letter}
    # Post method with requests
    response = requests.post(url, values)
    # Igual json a la respuesta si existe
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json["id"], json["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
