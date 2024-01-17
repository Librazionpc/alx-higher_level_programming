-- List all the cities name California in the databasee
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
