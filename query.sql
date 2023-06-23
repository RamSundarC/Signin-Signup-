-- PATH = source ./query.sql;


--CREATE DATABASE BOTBASE;

--SHOW DATABASES;

USE BOTBASE;

-- creating a table to store the user credential details
/*
CREATE TABLE CREDENTIALS(
    User_Id VARCHAR(5) PRIMARY KEY,
    Password VARCHAR(8)
);
*/

-- samples
/*
INSERT INTO CREDENTIALS VALUES
    (2345,"ABC200$"),
    (3456,"ZYX100#");

SELECT * FROM CREDENTIALS;
*/


--creating a profile tabel to store the user details
/*
CREATE TABLE PROFILE(
    User_Id VARCHAR(5) PRIMARY KEY,
    Password VARCHAR(8)UNIQUE,
    Name VARCHAR(10),
    DOB DATE NOT NULL,
    Location VARCHAR(8),
    Name_of_Pet_Animal VARCHAR(5)
);

-- alter table to add security question and drop name of pet animal
ALTER TABLE PROFILE(
    ADD COLUMN security_question VARCHAR9255
    DROP COLUMN Name_of_Pet_Animal
)

*/

--creating a trigger to insert the password in credentials table when the password is inserted in profile table
/*
DELIMITER $$
CREATE TRIGGER writter
AFTER INSERT ON PROFILE
FOR EACH ROW
BEGIN
INSERT INTO CREDENTIALS(User_Id,Password)
VALUES (NEW.User_Id, NEW.Password);
END $$
DELIMITER ;
*/


-- creating a trigger to update the password in credentials table when the password  is updated in profile table
/*
DELIMITER $$
CREATE TRIGGER Updater
AFTER UPDATE ON CREDENTIALS
FOR EACH ROW
BEGIN
    UPDATE PROFILE
    SET Password = NEW.Password
    WHERE User_Id = NEW.User_Id;
END $$
DELIMITER ;
*/









