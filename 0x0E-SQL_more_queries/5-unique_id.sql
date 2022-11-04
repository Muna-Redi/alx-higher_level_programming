-- create a table unique_id, deafault column value and uniqueness
-- creating table unique_id with deafult column value
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256) NOT NULL
);
