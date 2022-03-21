CREATE DATABASE IF NOT EXISTS CVDCalculator;
USE CVDCalculator;
CREATE TABLE IF NOT EXISTS accounts (
    id int NOT NULL AUTO_INCREMENT,
    first_name varchar(255) NOT NULL,
	second_name varchar(255) NOT NULL,
	email varchar(255),
    role varchar(255) NOT NULL,
	password CHAR(60) BINARY NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS records (
    id int NOT NULL AUTO_INCREMENT,
    nhs_id int(10) NOT NULL,
	first_name varchar(255) NOT NULL,
	second_name varchar(255) NOT NULL,
	smoker BOOLEAN,
	age varchar(10),
	birth_date DATE,
    sex varchar(255),
	systolic varchar(255),
	cholesterol varchar(255),
	hdl varchar(255),
	chd_risk varchar(255),
	PRIMARY KEY (id)
);

INSERT INTO accounts (first_name, second_name, email, role, password)
VALUES ("Sev", "Hayrapet", "sev@an.com", "admin", "$2b$12$gpRwkPTXziQTCQzJLJiOcuJ0ONGAYCnrW2lxzQOvHLeVJt68gj7zO");
INSERT INTO accounts (first_name, second_name, email, role, password)
VALUES ("Terry", "Davis", "terry@gmail.com", "gp", "$2b$12$EhU9ol5oInHWNPfPV8WTbeCYFzYhGKdxa7z2nvs3DTbfU73lypj.C"); 

INSERT INTO records (nhs_id, first_name, second_name, smoker, age, birth_date, sex, systolic, cholesterol, hdl, chd_risk)
VALUES (69, "Jeffrey", "Bozo", True, 45, "1982-01-25", "male", 100, 100, 100, 25); 

CREATE USER 'cvd_account'@'localhost' IDENTIFIED BY 'james_charles00';
GRANT ALL PRIVILEGES ON CVDCalculator . * TO 'cvd_account'@'localhost';
FLUSH PRIVILEGES;