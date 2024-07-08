CREATE DATABASE new_database_name;
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON new_database_name.* TO 'new_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
