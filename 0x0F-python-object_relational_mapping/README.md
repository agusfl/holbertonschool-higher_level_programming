# Python | SQLAlchemy (ORM) - Object-relational mapping:

**Learning objectives:**

* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

## Environment

* Language: Python
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/) - [Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* Interpreter: python3 (version 3.8.5)
* Databases and ORM: ``MySQLdb`` version 2.0.x | ORM --> ``SQLAlchemy`` version 1.4.x

### How to install ``MySQLdb`` module version 2.0.x:

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### How to install ``SQLAlchemy`` module version 1.4.x:

```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|tests |Folder that holds tests suite cases.
| |
| |
| |
| |
| |
| |
| |

## Authors

* [Agustin Flom](https://github.com/agusfl)
