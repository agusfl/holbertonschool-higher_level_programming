-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on my MySQL server.
-- Description of the table: id (INT UNIQUE, auto generated, cant be NULL and is a Primary key), name (VARCHAR(256)
-- can not be NULL)
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail
-- Para usar la base de datos (hbtn_0d_usa) se puede hacer como lo hice en este caso poniendo: hbtn_0d_usa.states - con
-- el punto se le indica que queremos crear la tabla "states" en la base de datos: hbtn_0d_usa. 
-- Otra forma que tenemos de crear la tabla dentro de la base de datos es poner antes de la query: CREATE TABLE
-- poner: USE hbtn_0d_usa y despues para crear la tabla ponemos nomas: "states" sin la base de datos y el punto.
-- Info AUTO_INCREMENT: https://www.w3schools.com/sql/sql_autoincrement.asp

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
