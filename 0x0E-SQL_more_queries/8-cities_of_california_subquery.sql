-- query for rows in a table
-- Selecting all cities in California with (state_id = 1)
SELECT id, name
       FROM cities
       WHERE state_id = (SELECT id FROM states WHERE name = 'California')
       ORDER BY cities.id ASC;
