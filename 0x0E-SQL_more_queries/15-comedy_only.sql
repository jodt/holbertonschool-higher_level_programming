-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = 5
GROUP BY 1
ORDER BY 1;

