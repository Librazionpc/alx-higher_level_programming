-- List all citis using JOIN
USE hbtn_0d_usa;
SELECT cites.id, cities.name, states.name AS state_name 
FROM cities
INNER JOIN states ON cities.state_id = state.id 
ORDER BY cities.id ASC;
