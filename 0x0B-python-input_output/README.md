# Python - Input/Output:

Learning objectives:

* Why Python programming is awesome
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

## Environment

* Language: Python
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/) - [Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* Interpreter: python3 (version 3.8.5)

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|tests |Folder that holds tests suite cases.
|0-read_file.py |Function that **reads** a text file (with enconding UTF-8) and prints it to stdout.
|1-write_file.py |Function that **writes** a string to a text file (using encoding UTF-8) and returns the number of characters written.
|2-append_write.py |Function that **appends** a string at the end of a text file (using encoding UTF-8) and returns the number of characters added.
|3-to_json_string.py |Function that returns the **JSON representation of an object** (string).
|4-from_json_string.py |Function that returns an **object (Python data structure)** represented by a JSON string.
|5-save_to_json_file.py |Function that writes an Object to a text file, using a JSON representation.
|6-load_from_json_file.py |Function that creates an Object from a “JSON file”.
|7-add_item.py |Script that adds all arguments to a Python list, and then save them to a file.
|8-class_to_json.py |Function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.
|9-student.py |Class ``Student`` that defines a student by the ``attributes``: **first_name**, **last_name** and **age**.
|10-student.py |Add public method ``to_json`` that retrieves a dictionary representation of a ``Student`` instance.
|11-student.py |Add public method ``reload_from_json`` that replaces all attributes of the ``Student`` instance.
|12-pascal_triangle.py |Function that returns a list of lists of integers representing the ``Pascals's`` triangle of ``n``.
|100-append_after.py |Function that inserts a line of text to a file, after each line containing a **specific string**.
|101-stats.py |Still in development, but it is a script that reads stdin line by line and computes metrics.

## Authors

* [Agustin Flom](https://github.com/agusfl)
