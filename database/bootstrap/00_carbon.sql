DROP DATABASE IF EXISTS CarbonConnect;
CREATE DATABASE IF NOT EXISTS CarbonConnect;
Use CarbonConnect;

DROP TABLE IF EXISTS TFIDF_Encoding;
CREATE TABLE IF NOT EXISTS TFIDF_Encoding (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vector MEDIUMTEXT,
    vocabulary MEDIUMTEXT,
    idf MEDIUMTEXT
);

DROP TABLE IF EXISTS Beta_User;
CREATE TABLE IF NOT EXISTS Beta_User (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_values VARCHAR(100)
);

DROP TABLE IF EXISTS Beta_Enterprise;
CREATE TABLE IF NOT EXISTS Beta_Enterprise (
    id INT PRIMARY KEY AUTO_INCREMENT,
    enterprise_values VARCHAR(100)
);

DROP TABLE IF EXISTS Country;
CREATE TABLE IF NOT EXISTS Country (
   id INT PRIMARY KEY AUTO_INCREMENT,
   emissions FLOAT(5),
   name VARCHAR(50)
);


DROP TABLE IF EXISTS NGO;
CREATE TABLE IF NOT EXISTS NGO (
   id INT PRIMARY KEY AUTO_INCREMENT,
   website VARCHAR(255) NOT NULL,
   name VARCHAR(50),
   contact VARCHAR(50),
   bio MEDIUMTEXT,
   vectorized_bio MEDIUMTEXT
);


DROP TABLE IF EXISTS User;
CREATE TABLE IF NOT EXISTS User (
   id INT PRIMARY KEY,
   emission_result FLOAT(5),
   country_id INT,
   email VARCHAR(255),
   match_consent BOOLEAN,
   name VARCHAR(255),
   bio MEDIUMTEXT,
   vectorized_bio MEDIUMTEXT,
   FOREIGN KEY (country_id) REFERENCES Country(id)
       ON UPDATE RESTRICT
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS Enterprises;
CREATE TABLE IF NOT EXISTS Enterprises (
   survey_id INT PRIMARY KEY AUTO_INCREMENT,
   id INT,
   name VARCHAR(50),
   type VARCHAR(255),
   emission_result FLOAT(5),
   country_id INT,
   FOREIGN KEY (country_id) REFERENCES Country(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS PublicTransport;
CREATE TABLE IF NOT EXISTS PublicTransport (
   id INT PRIMARY KEY,
   user_id INT,
   distance INT,
   trainCount INT,
   busCount INT,
   emission_tags VARCHAR(50),
   FOREIGN KEY (user_id) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS Flight;
CREATE TABLE IF NOT EXISTS Flight (
   id INT PRIMARY KEY,
   user_id INT,
   date_taken DATETIME,
   distance INT,
   emission_tags VARCHAR(50),
   aircraft_type VARCHAR(250),
   FOREIGN KEY (user_id) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS Cars;
CREATE TABLE IF NOT EXISTS Cars (
   id INT PRIMARY KEY AUTO_INCREMENT,
   user_id INT,
   fuel_type VARCHAR(50),
   emission_tags VARCHAR(50),
   fuel_used FLOAT(20),
   FOREIGN KEY (user_id) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS ResData;
CREATE TABLE IF NOT EXISTS ResData (
   id INT PRIMARY KEY AUTO_INCREMENT,
   user_id INT,
   elec_usage FLOAT(5),
   emission_tags VARCHAR(250),
   heating FLOAT(5),
   water_heating FLOAT(5),
   cooking_gas FLOAT(5),
   FOREIGN KEY (user_id) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS CarTags;
CREATE TABLE IF NOT EXISTS CarTags (
   Car_ID INT,
   Emission_Tag INT,
   PRIMARY KEY(Car_ID, Emission_Tag),
   FOREIGN KEY (Car_ID) REFERENCES Cars(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS FlightTags;
CREATE TABLE IF NOT EXISTS FlightTags (
   Flight_ID INT,
   Emission_Tag INT,
   PRIMARY KEY(Flight_ID, Emission_Tag),
   FOREIGN KEY (Flight_ID) REFERENCES Flight(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS TransportTags;
CREATE TABLE IF NOT EXISTS TransportTags (
   PublicTransport_ID INT,
   Emission_Tag INT,
   PRIMARY KEY(PublicTransport_ID, Emission_Tag),
   FOREIGN KEY (PublicTransport_ID) REFERENCES PublicTransport(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);

DROP TABLE IF EXISTS EmissionTags;
CREATE TABLE IF NOT EXISTS EmissionTags (
    id INT PRIMARY KEY,
    description VARCHAR(250)
);

DROP TABLE IF EXISTS EntTags;
CREATE TABLE IF NOT EXISTS EntTags (
   enterprise_survey_id INT,
   tag_id INT,
   PRIMARY KEY(enterprise_survey_id, tag_id),
   FOREIGN KEY (enterprise_survey_id) REFERENCES Enterprises(survey_id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   FOREIGN KEY (tag_id) REFERENCES EmissionTags(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);

DROP TABLE IF EXISTS UserTags;
CREATE TABLE IF NOT EXISTS UserTags (
   user_id INT,
   tag_id INT,
   PRIMARY KEY(user_id, tag_id),
   FOREIGN KEY (user_id) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   FOREIGN KEY (tag_id) REFERENCES EmissionTags(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);

DROP TABLE IF EXISTS NGOTags;
CREATE TABLE IF NOT EXISTS NGOTags (
   ngo_id INT,
   tag_id INT,
   PRIMARY KEY(ngo_id, tag_id),
   FOREIGN KEY (ngo_id) REFERENCES NGO(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   FOREIGN KEY (tag_id) REFERENCES EmissionTags(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);

DROP TABLE IF EXISTS NGOEnterprise;
CREATE TABLE IF NOT EXISTS NGOEnterprise (
   ngo_id INT,
   enterprise_survey_id INT,
   PRIMARY KEY(ngo_id, enterprise_survey_id),
   FOREIGN KEY (ngo_id) REFERENCES NGO(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   FOREIGN KEY (enterprise_survey_id) REFERENCES Enterprises(survey_id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);
DROP TABLE IF EXISTS NGOUser;
CREATE TABLE IF NOT EXISTS NGOUser (
   ngo_id INT,
   user_id INT,
   PRIMARY KEY(ngo_id, user_id),
   FOREIGN KEY (ngo_id) REFERENCES NGO(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   FOREIGN KEY (user_id) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


