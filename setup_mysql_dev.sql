-- Create database if it doesn't exit
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnh_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev to hbnb_dev_user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnh_dev'@'localhost';
FLUSH PRIVILEGES;
-- Grant SELECT privilege on performance_schema to hbnh_dev user
GRANT SELECT ON performance_schema.* TO 'hbnh_dev'@'localhost';
FLUSH PRIVILEGES;

/*
-- this script prepares a MySQL server for the project
-- create project developement database with the name : hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating new user named : hbnb_dev with all privileges on the db hbnb_dev_db
-- with the password : hbnb_dev_pwd if it dosen't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- granting the SELECT privilege for the user hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
*/
