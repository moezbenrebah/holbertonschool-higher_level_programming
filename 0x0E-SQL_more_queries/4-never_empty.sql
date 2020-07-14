-- a script that creates the table id_not_null on your MySQL server.

CREATE TABLE 
IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL);
