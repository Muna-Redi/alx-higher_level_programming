-- creating a table and adding values (rows)
-- creating second_table with values for decription id, name and score
CREATE TABLE IF NOT EXISTS second_table (
	id integer,
	name varchar(256),
	score integer
);
-- adding multipler rows
INSERT INTO second_table
VALUES (1, "John", 10);
INSERT INTO second_table
VALUES(2, "ALEX", 3);
INSERT INTO second_table
VALUES(3, "Bob", 14);
VALUES (4, "George", 8);
