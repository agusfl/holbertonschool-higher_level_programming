-- Script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in my MySQL server.
-- The result column name should be average
-- The database name will be passed as an argument of the mysql command
-- Info about AVG (average) function: https://www.mysqltutorial.org/mysql-avg/#:~:text=The%20MySQL%20AVG()%20function,average%20value%20of%20a%20set.&text=You%20use%20the%20DISTINCT%20operator,value%20of%20the%20distinct%20values.
-- Info about AS (alias): https://www.mysqltutorial.org/mysql-alias/  

SELECT AVG(score) AS average FROM second_table;
