-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS `codyx_test`;
GRANT ALL PRIVILEGES ON `codyx_test`.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
