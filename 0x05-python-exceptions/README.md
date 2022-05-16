# Python - Exceptions:

Learning objectives:

* Why Python programming is awesome
* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception

## Environment

* Language: Python
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/)
* Interpreter: python3 (version 3.8.5)

## Description of each file:

 | Files          |Desription
 |:----------------|:-------------------------------:|
 |0-safe_print_list.py |Function that prints ``x`` elements of a list --> ``IndexError``.
 |1-safe_print_integer.py |Function that prints an integer with ``"{:d}.format()"`` --> ``TypeError and ValueError``.
 |2-safe_print_list_integers.py |Function that prints the first ``x`` elements of a list and only integers --> ``TypeError and ValueError``.
 |3-safe_print_division.py |Function that divides 2 integers and prints the result --> ``ZeroDivisionError``.
 |4-list_division.py |Function that divides element by element of 2 lists --> ``TypeError, ZeroDivisionError and IndexError``.
 |5-raise_exception.py |Function that **raises** a ``type`` exception --> ``TypeError``.
 |6-raise_exception_msg.py |Function that **raises** a ``name`` exception --> ``NameError``.
 |100-safe_print_integer_err.py |Function that prints an integer --> ``Exception``.
 |101-safe_function.py | Function that executes a function safely --> ``Exception``.
 |102-magic_calculation.py | Python bytecode

## Authors :pen:

 * [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
