-- Create a database and a user
-- creating dtabase hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creating user_0d_2 with specific privileges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Granting USAGE privilege to user_0d_2
GRANT USAGE ON * . * TO 'user_0d_2'@'localhost';
-- Granting SELECT privilege to user_0d_2
GRANT SELECT ON `hbtn_0d_2` . * TO 'user_0d_2'@'localhost';
