# Bash | Python -> Network #0:

**Learning objectives:**

* What a ``URL`` is
* What ``HTTP`` is
* How to ``read`` a URL
* The ``scheme`` for a HTTP URL
* What a ``domain name`` is
* What a ``sub-domain`` is
* How to define a ``port number`` in a URL
* What a ``query string`` is
* What an ``HTTP request`` is
* What an ``HTTP response`` is
* What ``HTTP headers`` are
* What the ``HTTP message body`` is
* What an ``HTTP request method`` is
* What an ``HTTP response status code`` is
* What an ``HTTP Cookie`` is
* How to make a request with ``cURL``
* What happens when you type google.com in your browser (Application level)

## Environment

* Languages: Bash, Python
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/) - [Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) | [Shellcheck](https://github.com/koalaman/shellcheck)
* Interpreter: python3 (version 3.9)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-body_size.sh |Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
|1-body.sh |Bash script that takes in a URL, ``sends a GET request`` to the URL, and displays the body of the response
|2-delete.sh |Bash script that sends a ``DELETE`` request to the URL passed as the first argument and displays the body of the response
|3-methods.sh |Bash script that takes in a URL and displays all HTTP methods the server will accept.
|4-header.sh |Bash script that takes in a URL as an argument, sends a ``GET`` request to the URL, and displays the body of the response
|5-post_params.sh |Bash script that takes in a URL, sends a ``POST`` request to the passed URL, and displays the body of the response
|100-status_code.sh |Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
|101-post_json.sh |Bash script that sends a ``JSON POST request`` to a URL passed as the first argument, and displays the body of the response.
|102-catch_me.sh |Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.

## Authors

* [Agustin Flom](https://github.com/agusfl)
