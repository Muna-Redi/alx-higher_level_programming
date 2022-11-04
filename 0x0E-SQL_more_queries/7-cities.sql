-- Adding Primary and FOREING KEY to a table column
-- creating state_id with a FOREING KEY 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- creating new table
CREATE TABLE IF NOT EXISTS cities (
       id INT NOT NULL AUTO_INCREMENT UNIQUE,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states(id)
);
