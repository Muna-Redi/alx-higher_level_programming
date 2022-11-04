-- Create database and table
-- creating database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- change to new database
USE hbtn_0d_usa;
-- create new table
CREATE TABLE IF NOT EXISTS states (
       id INT NOT NULL AUTO_INCREMENT UNIQUE,
       name VARCHAR(256) NOT NULL, PRIMARY KEY (id)
);
