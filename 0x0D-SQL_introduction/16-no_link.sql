-- filtered records in Database
-- showing scores with non_empty name fields from second_table
SELECT score, name FROM second_table
WHERE name != ''
ORDER BY score DESC;
