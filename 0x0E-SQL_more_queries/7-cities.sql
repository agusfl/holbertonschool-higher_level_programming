-- Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on my MySQL server.
-- Description of the table: id (INT unique, auto generated and can not be NULL), state_id (INT can not be NULL
-- and must be a FOREGIN KEY that refers to id of the states table), name (VARCHAR(256) and can not be NULL).
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail
-- Info FOREIGN KEY: https://zetcode.com/mysql/constraints/

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES cities(id),
	name VARCHAR(256) NOT NULL);
