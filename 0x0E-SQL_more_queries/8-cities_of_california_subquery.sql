-- Lists all the cities of California that can be found in the database
--Lists all rows of columns
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY ASC;
