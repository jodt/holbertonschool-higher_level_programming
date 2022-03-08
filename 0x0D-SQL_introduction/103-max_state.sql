-- displays the max temperature of each state
SELECT state, MAX(value)
FROM temperatures
GROUP BY 1
ORDER BY 1;
