-- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- Lo que se va a haciendo es ir "joinenando" entre las distintas tablas que se relacionan para poder llegar a la
-- info que se nos pide. En este caso la tabla "tv_show_genres" nos sirve como "pivot" para unir "tv_shows" y
-- "tv_genres".
-- Muy similar a los ejercicios anteriores salvo que en este caso se usa el LEFT JOIN para que nos aparezcan los
-- valores que estan en NULL en la columna name de "tv_genres".

SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
ORDER BY title, name;
