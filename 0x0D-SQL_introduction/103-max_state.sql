-- displays the max temperature of each state
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY 1
ORDER BY 1;