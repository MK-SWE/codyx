-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS `codyx_dev`;
GRANT ALL PRIVILEGES ON `codyx_dev`.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
