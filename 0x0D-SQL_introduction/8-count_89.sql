-- Script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in my MySQL server.
-- The database name will be passed as an argument of the mysql command
-- Info COUNT() function: https://www.javatpoint.com/mysql-count#:~:text=MySQL%20count()%20function%20is,not%20find%20any%20matching%20rows.

SELECT COUNT(*) FROM first_table WHERE id=89;
