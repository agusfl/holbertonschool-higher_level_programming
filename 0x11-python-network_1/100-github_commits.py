#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge:

- The first argument will be the repository name
- The second argument will be the owner name
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)

Commits API github --> https://docs.github.com/en/rest/commits/commits
"""
if __name__ == "__main__":
    import requests
    from sys import argv  # for command line arguments

    repo = argv[1]  # se guarda el usuario pasado como primer comando en linea
    owner = argv[2]  # guardamos la contr que se pase como 2 comand en linea

    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)

    res = requests.get(url)
    json = res.json()

    cont = 0
    for data in json:
        if cont < 10:
            print("{}: {}".format(data.get('sha'), data.get('commit')
                                  .get('author').get('name')))
        cont = cont + 1
