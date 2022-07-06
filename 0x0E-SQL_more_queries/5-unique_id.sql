-- Script that creates the table unique_id on your MySQL server.
-- Description of the table: id (INT with default value of 1 and must be UNIQUE), name (VARCHAR(256))
-- The database name will be passed as an argument of the mysql command
-- If the table unique_id already exists, your script should not fail
-- Info UNIQUE contraint: https://zetcode.com/mysql/constraints/

CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
