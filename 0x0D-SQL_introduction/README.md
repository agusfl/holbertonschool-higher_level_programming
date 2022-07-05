# SQL - Introduction to SQL using MySQL:

Learning objectives:

* What’s a **database**
* What’s a **relational database**
* What does ``SQL`` stand for
* What’s ``MySQL``
* How to **create** a database in MySQL
* What does ``DDL`` and ``DML`` stand for
* How to ``CREATE`` or ``ALTER`` a table
* How to ``SELECT`` data from a table
* How to ``INSERT``, ``UPDATE`` or ``DELETE`` data
* What are ``subqueries``
* How to use MySQL ``functions``

## Environment

* Language: **MySQL**
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [MySql](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
* Usage: ``cat [filename] | mysql -hlocalhost -uroot -p [database]``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-list_databases.sql |Script that **lists all databases** of your MySQL server.
|1-create_database_if_missing.sql |Script that **creates** the database ``hbtn_0c_0`` in your MySQL server.
|2-remove_database.sql |Script that **deletes** the database ``hbtn_0c_0`` in your MySQL server.
|3-list_tables.sql |Script that **lists all the tables** of a database in your MySQL server.
|4-first_table.sql |Script that **creates a table** called ``first_table`` in the current database in your MySQL server.
|5-full_table.sql |Script that **prints the full description of the table first_table** from the database ``hbtn_0c_0`` in your MySQL server.
|6-list_values.sql |Script that **lists all rows of the table first_table** from the database ``hbtn_0c_0`` in your MySQL server.
|7-insert_value.sql |Script that **inserts a ``new row`` in the table first_table** (database hbtn_0c_0) in your MySQL server.
|8-count_89.sql |Script that **displays the number of records with ``id = 89`` in the table first_table** of the database ``hbtn_0c_0`` in your MySQL server.
|9-full_creation.sql |Script that **creates a table second_table in the database hbtn_0c_0** in your MySQL server and **add multiples rows**.
|10-top_score.sql |Script that lists all records of the table second_table of the database ``hbtn_0c_0`` in your MySQL server.
|11-best_score.sql |Script that lists all records **with a score >= 10** in the table second_table of the database ``hbtn_0c_0`` in your MySQL server.
|12-no_cheating.sql |Script that ``updates`` the score of Bob to 10 in the table second_table.
|13-change_class.sql |Script that ``removes`` all records with a **score <= 5** in the table second_table of the database ``hbtn_0c_0`` in your MySQL server.
|14-average.sql |Script that computes the score ``average`` of all records in the table second_table of the database ``hbtn_0c_0`` in your MySQL server.
|15-groups.sql |Script that lists the number of records with the **same score in the table second_table** of the database ``hbtn_0c_0`` in your MySQL server.
|16-no_link.sql |Script that lists all records of the table second_table of the database ``hbtn_0c_0`` in your MySQL server.
|100-move_to_utf8.sql |Script that **converts hbtn_0c_0 database to UTF8** ``(utf8mb4, collate utf8mb4_unicode_ci)`` in your MySQL server.
|101-avg_temperatures.sql |Script that displays the **average** ``temperature`` (Fahrenheit) by city ordered by temperature (descending).
|102-top_city.sql |Script that displays the **top 3 of cities temperature during July and August** ordered by temperature (descending)
|103-max_state.sql |Script that displays the ``max`` temperature of each state (ordered by State name).

## Authors

* [Agustin Flom](https://github.com/agusfl)

