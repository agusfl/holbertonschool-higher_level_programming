-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
-- Importante: en esta task hay que crear una base de datos nueva "hbtn_0d_tvshows_rate" que no es la que veniamos
-- usando en los ejercicios pasados. Para crear esta base de datos nueva e importar la info que nos pasan en el
-- link que esta en el "download" uso los comandos que estan mas arriba en la parte de: How to import a SQL dump
-- Uso los mismos comandos, simplemente que cambio en el "curl" pongo el link que nos pasan en el "download" y despues
-- en lugar de poner la bases de datos "hbtn_0d_tvshows" pongo: "hbtn_0d_tvshows_rate".

SELECT tv_shows.title AS title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id=tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;
