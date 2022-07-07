# SQL - More queries:

**Comments for your SQL file:**

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

**Install MySQL 8.0 on Ubuntu 20.04 LTS**

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

**Connect to your MySQL server:**

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

**How to import a SQL dump:**

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

**Learning objectives:**

* How to create a ``new MySQL user``
* How to ``manage privileges`` for a user to a database or table
* What’s a ``PRIMARY KEY``
* What’s a ``FOREIGN KEY``
* How to use ``NOT NULL`` and ``UNIQUE`` **constraints**
* How to ``retrieve datas from multiple tables`` in **one request**
* What are ``subqueries``
* What are ``JOIN`` and ``UNION``

## Environment

* Language: **MySQL**
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [MySql](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
* ```Usage: cat [filename] | mysql -hlocalhost -uroot -p [database]```

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-privileges.sql |Script that lists all privileges of the MySQL users ``user_0d_1`` and ``user_0d_2`` on your server (in localhost).
|1-create_user.sql |Script that creates the MySQL server user ``user_0d_1``.
|2-create_read_user.sql |Script that creates the database ``hbtn_0d_2`` and the **user** ``user_0d_2``.
|3-force_name.sql |Script that creates the **table** ``force_name`` on your MySQL server.
|4-never_empty.sql |Script that creates the **table** ``id_not_null`` on your MySQL server.
|5-unique_id.sql |Script that creates the **table** ``unique_id`` on your MySQL server.
|6-states.sql |Script that creates the **database** ``hbtn_0d_usa`` and the **table** ``states`` (in the database hbtn_0d_usa) on your MySQL server.
|7-cities.sql |Script that creates the **database** ``hbtn_0d_usa`` and the **table** ``cities`` (in the database hbtn_0d_usa) on your MySQL server.
|8-cities_of_california_subquery.sql |Script that **lists** all the **cities** of ``California`` that can be found in the database ``hbtn_0d_usa``.
|9-cities_by_state_join.sql |Script that **lists** all cities contained in the **database** ``hbtn_0d_usa``.
|10-genre_id_by_show.sql |Script that **lists all shows** contained in ``hbtn_0d_tvshows`` that have at least one **genre linked**.
|11-genre_id_all_shows.sql |Script that **lists all shows** contained in the database ``hbtn_0d_tvshows``.
|12-no_genre.sql |Script that **lists all shows** contained in ``hbtn_0d_tvshows`` **without** a genre linked.
|13-count_shows_by_genre.sql |Script that **lists all genres** from ``hbtn_0d_tvshows`` and displays the number of shows **linked** to each.
|14-my_genres.sql |Script that uses the ``hbtn_0d_tvshows`` database to **lists all genres** of the show ``Dexter``.
|15-comedy_only.sql |Script that **lists all Comedy shows** in the database ``hbtn_0d_tvshows``.
|16-shows_by_genre.sql |Script that **lists all shows, and all genres linked to that show**, from the database ``hbtn_0d_tvshows``.
|100-not_my_genres.sql |Script that uses the ``hbtn_0d_tvshows`` database to **list all genres not linked** to the show ``Dexter``.
|101-not_a_comedy.sql |Script that **lists all shows without the genre** ``Comedy`` in the database ``hbtn_0d_tvshows``.
|102-rating_shows.sql |Script that **lists all ``shows``** from ``hbtn_0d_tvshows_rate`` by their ``rating``.
|103-rating_genres.sql |Script that **lists all ``genres``** in the database ``hbtn_0d_tvshows_rate`` by their **rating**.

## Authors

* [Agustin Flom](https://github.com/agusfl)
