-- Script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in my MySQL server.
-- The database name will be passed as an argument of the mysql command
-- Info: https://www.tutorialspoint.com/how-to-count-the-number-of-tables-in-a-mysql-database#:~:text=To%20check%20the%20count%20of,count%20of%20all%20the%20tables. 

SELECT COUNT(*) FROM first_table WHERE id=89;
