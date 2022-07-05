-- Script that creates a table calles "first_table" in the current database in my MySQL server.
-- The database name will be passed as an argument of the mysql command
-- If the table first_table already exists, your script should not fail
-- Info: https://phoenixnap.com/kb/how-to-create-a-table-in-mysql 

CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256));
