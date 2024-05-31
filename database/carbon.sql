DROP DATABASE IF EXISTS CarbonConnect;
CREATE DATABASE IF NOT EXISTS CarbonConnect;
USE CarbonConnect;


DROP TABLE IF EXISTS Country;
CREATE TABLE IF NOT EXISTS Country (
   id INT PRIMARY KEY,
   emissions VARCHAR(255),
   name VARCHAR(50)
);


DROP TABLE IF EXISTS NGO;
CREATE TABLE IF NOT EXISTS NGO (
   id INT PRIMARY KEY,
   logo VARCHAR(255) UNIQUE NOT NULL,
   website VARCHAR(255) UNIQUE NOT NULL,
   name VARCHAR(50),
   mission_tags VARCHAR(50),
   contact VARCHAR(50)
);


DROP TABLE IF EXISTS User;
CREATE TABLE IF NOT EXISTS User (
   id INT PRIMARY KEY,
   tags VARCHAR(255),
   emission_result INT,
   country_id INT,
   FOREIGN KEY (country_id) REFERENCES Country(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS Enterprises;
CREATE TABLE IF NOT EXISTS Enterprises (
   id INT PRIMARY KEY,
   name VARCHAR(50),
   type VARCHAR(255),
   emission_result VARCHAR(255),
   emission_tags VARCHAR(255),
   misc_emissions VARCHAR(255),
   country_id INT,
   FOREIGN KEY (country_id) REFERENCES Country(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS operatingEmission;
CREATE TABLE IF NOT EXISTS operatingEmission (
   id INT PRIMARY KEY,
   enterprise_id INT,
   FOREIGN KEY (enterprise_id) REFERENCES Enterprises(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   heat_and_gas VARCHAR(50),
   ElectricityUsage VARCHAR(50)
);


DROP TABLE IF EXISTS SupplyChain;
CREATE TABLE IF NOT EXISTS SupplyChain (
   id INT PRIMARY KEY,
   enterprise_id INT,
   vehicle_type VARCHAR(50),
   distance INT,
   fuel_type VARCHAR(50),
   emission_tags VARCHAR(50),
   FOREIGN KEY (enterprise_id) REFERENCES Enterprises(id)
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
   enterprise_id INT,
   Date_taken DATETIME,
   origin VARCHAR(250),
   destination VARCHAR(250),
   emission_tags VARCHAR(50),
   aircraft_type VARCHAR(250),
   FOREIGN KEY (user_id) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   FOREIGN KEY (enterprise_id) REFERENCES Enterprises(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS Cars;
CREATE TABLE IF NOT EXISTS Cars (
   id INT PRIMARY KEY,
   user_id INT,
   fuel_type VARCHAR(50),
   emission_tags VARCHAR(50),
   distance INT,
   FOREIGN KEY (user_id) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS ResData;
CREATE TABLE IF NOT EXISTS ResData (
   id INT PRIMARY KEY,
   user_id INT,
   elec_usage VARCHAR(250),
   emission_tags VARCHAR(250),
   heat_gas VARCHAR(50),
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


DROP TABLE IF EXISTS SupplyTags;
CREATE TABLE IF NOT EXISTS SupplyTags (
   SupplyChain_ID INT,
   Emission_Tag INT,
   PRIMARY KEY(SupplyChain_ID, Emission_Tag),
   FOREIGN KEY (SupplyChain_ID) REFERENCES SupplyChain(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS CostTags;
CREATE TABLE IF NOT EXISTS CostTags (
   operatingEmission_ID INT,
   Emission_Tag INT,
   PRIMARY KEY(operatingEmission_ID, Emission_Tag),
   FOREIGN KEY (operatingEmission_ID) REFERENCES operatingEmission(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);

DROP TABLE IF EXISTS EntTags;
CREATE TABLE IF NOT EXISTS EntTags (
   enterprise_id INT,
   tag_id INT,
   PRIMARY KEY(enterprise_id, tag_id),
   FOREIGN KEY (enterprise_id) REFERENCES Enterprises(id)
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




DROP TABLE IF EXISTS EmissionTags;
CREATE TABLE IF NOT EXISTS EmissionTags (
    id INT PRIMARY KEY,
    description VARCHAR(250)
);

DROP TABLE IF EXISTS NGOEnterprise;
CREATE TABLE IF NOT EXISTS NGOEnterprise (
   ngo_id INT,
   enterprise_id INT,
   PRIMARY KEY(ngo_id, enterprise_id,
   FOREIGN KEY (ngo_id) REFERENCES NGO(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   FOREIGN KEY (enterprise_id) REFERENCES enterprise(id)
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
   FOREIGN KEY (user_id) REFERENCES user(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


