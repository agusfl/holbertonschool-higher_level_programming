# Python - Test driven development:

Learning objectives:

* Why Python programming is awesome
* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

## Environment

* Language: Python
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/) - [Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* Interpreter: python3 (version 3.9)

## Test

Use of: [doctest](https://docs.python.org/3.9/library/doctest.html) and [unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest).

All your tests should be executed by using this command: 
```
python3 -m doctest ./tests/*
```

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|test |Folder for all the test files (.txt) using doctest and unittest.
|0-add_integer.py |Function that adds 2 integers.
|2-matrix_divided.py |Function that divides all elements of a matrix.
|3-say_my_name.py |Function that prints ``My name is <first name> <last name>``.
|4-print_square.py |Function that prints a ``square`` with the character ``#``.
|5-text_indentation.py |Function that prints a text with 2 new lines after each of the following characters: ``. : ?``.
|100-matrix_mul.py |Function that multiplies 2 matrices.
|101-lazy_matrix_mul.py |Function that multiplies 2 matrices by using the module ``NumPy``.

## Authors

* [Agustin Flom](https://github.com/agusfl)
