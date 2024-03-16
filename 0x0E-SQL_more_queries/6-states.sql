-- Creates database named hbtn_0d_usa and table named states
-- Creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use a database for the table
USE hbtn_0d_usa;
-- Creates table
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);

