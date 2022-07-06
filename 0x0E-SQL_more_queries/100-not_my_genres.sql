-- Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
-- Esta task es muy similar a la task 14, solo que aca se nos piden que listemos los generos que no estan "linkeados"
-- al show "Dexter" en lugar de los que si estan linkeados.
-- Uso el comando DISTINCT para que no se repitan los nombres de los generos ("name").
-- Info NOT IN con subquery: https://stackoverflow.com/questions/17469943/mysql-query-how-to-show-opposite-results

SELECT DISTINCT tv_genres.name AS name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id
WHERE name NOT IN (SELECT tv_genres.name
			FROM tv_genres
			JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
			JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id
			WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name;
