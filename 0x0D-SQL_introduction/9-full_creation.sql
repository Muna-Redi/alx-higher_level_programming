r- creating a table and adding values (rows)
-- creating second_table with values for decription id, name and score
CREATE TABLE IF NOT EXISTS second_table (
	id integer,
	name varchar(256),
	score integer
);
-- adding multipler rows
INSERT INTO second_table (id, name, score)
	VALUES
	(1, "John", 10),
	(2, "ALEX", 3),
	(3, "Bob", 14),
	(4, "George", 8);
