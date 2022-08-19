# Python -> Network #1:

**Resources:**

* [Quickstart with Requests package](https://docs.python.org/3.4/library/stdtypes.html#dict.get)
* [Requests package](https://docs.python-requests.org/en/master/)

**Learning objectives:**

* How to **fetch** internet resources with the ``Python package urllib``
* How to ``decode urllib body response``
* How to use the ``Python package requests`` #requestsiswaysimplerthanurllib
* How to make ``HTTP GET request``
* How to make ``HTTP POST/PUT/etc. request``
* How to **fetch** ``JSON resources``
* How to **manipulate** data from an ``external service``

## Environment

* Languages: Python
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/) - [Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-hbtn_status.py |Python script that fetches https://intranet.hbtn.io/status
|1-hbtn_header.py |Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
|2-post_email.py |Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
|3-error_code.py |Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
|4-hbtn_status.py |Python script that fetches https://intranet.hbtn.io/status
|5-hbtn_header.py |Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
|6-post_email.py |Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
|7-error_code.py |Python script that takes in a URL, sends a request to the URL and displays the body of the response.
|8-json_api.py |Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
|10-my_github.py |Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
|100-github_commits.py |Python script that takes 2 arguments in order to solve this challenge.

## Authors

* [Agustin Flom](https://github.com/agusfl)
