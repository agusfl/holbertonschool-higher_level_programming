-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- Tener en cuenta que para poder usar la funcion COUNT hay que usar GROUP BY
-- Hacemos el join por "genre_id" y "id" de tv_genres ya que nos piden que listemos todos los generos de la base
-- de datos.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY genre
ORDER BY number_of_shows DESC;
