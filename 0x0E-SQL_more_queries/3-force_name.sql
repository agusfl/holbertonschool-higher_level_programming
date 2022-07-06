-- Script that creates the table force_name on my MySQL server.
-- Description of the table: id (INT) - name (VARCHAR(256) can’t be null)
-- The database name will be passed as an argument of the mysql command
-- If the table force_name already exists, your script should not fail
-- Info: ejs que hicimos en el 1er proyecto de SQL.
-- Info NOT NULL: https://zetcode.com/mysql/constraints/

CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL);

