-- displays the max temperature of each state from the database
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
