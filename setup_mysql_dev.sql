-- Create database if it doesn't exit
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnh_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev to hbnb_dev_user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnh_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnh_dev user
GRANT SELECT ON performance_schema.* TO 'hbnh_dev'@'localhost';
