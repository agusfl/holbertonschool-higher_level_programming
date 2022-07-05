-- Script that updates the score of Bob to 10 in the table second_table.
-- You are not allowed to use Bob’s id value, only the name field
-- The database name will be passed as an argument of the mysql command
-- Info about UPDATE command: https://www.mysqltutorial.org/mysql-update-data.aspx

UPDATE second_table
SET score = 10
WHERE name = "Bob";
