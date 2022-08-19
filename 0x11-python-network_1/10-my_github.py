#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id:

- You must use Basic Authentication with a personal access token as password to
access to your information (only read:user permission is needed)
- The first argument will be your username
- The second argument will be your password (in your case, a personal access
token as password)
- You must use the package requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)

Info request an API in github using python:
https://blog.devgenius.io/how-to-use-api-request-in-python-6ef370f9f771
"""
if __name__ == "__main__":
    import requests
    from sys import argv  # for command line arguments

    url = "https://api.github.com/user"
    user = argv[1]  # se guarda el usuario pasado como primer comando en linea
    password = argv[2]  # guardamos la contr que se pase como 2 comand en linea

    # Se hace una request usando autentificacion
    response = requests.get(url, auth=(user, password))
    # Se guarda la respuesta en formato JSON
    json = response.json()
    # Se hace un try y un except por si la id no existe
    try:
        # Si el atributo "id" del diccionario "json" existe se imprime la id
        print(json["id"])
    except Exception:
        # Si no existe la "id" se imprime: None
        print("None")
