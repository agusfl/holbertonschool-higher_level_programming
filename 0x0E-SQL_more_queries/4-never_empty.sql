-- Script that creates the table id_not_null on my MySQL server.
-- Description of the table: id (INT with default value of 1) - name(VARCHAR(256))
-- The database name will be passed as an argument of the mysql command
-- If the table id_not_null already exists, your script should not fail
-- Setting a default value: https://dev.mysql.com/doc/refman/8.0/en/data-type-defaults.html

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256));
