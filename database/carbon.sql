DROP DATABASE IF EXISTS CarbonConnect;
CREATE DATABASE IF NOT EXISTS CarbonConnect;
USE CarbonConnect;


DROP TABLE IF EXISTS Country;
CREATE TABLE IF NOT EXISTS Country (
   id INT PRIMARY KEY,
   emissions varchar(255),
   name varchar(50)
);


DROP TABLE IF EXISTS NGO;
CREATE TABLE IF NOT EXISTS NGO (
   id INT PRIMARY KEY,
   logo varchar(255) UNIQUE NOT NULL,
   website varchar(255) UNIQUE NOT NULL,
   name varchar(50),
   mission_tags varchar(50),
   contact varchar(50)
);


DROP TABLE IF EXISTS User;
CREATE TABLE IF NOT EXISTS User (
   id INT PRIMARY KEY,
   tags varchar(255),
   emission_result INT,
   country_id INT,
   FOREIGN KEY (country_id) REFERENCES Country(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS Enterprises;
CREATE TABLE IF NOT EXISTS Enterprises (
   id INT PRIMARY KEY,
   name varchar(50),
   type varchar(255),
   emission_result varchar(255),
   emission_tags varchar(255),
   misc_emissions varchar(255),
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
   heat_and_gas varchar(50),
   ElectricityUsage varchar(50)
);


DROP TABLE IF EXISTS SupplyChain;
CREATE TABLE IF NOT EXISTS SupplyChain (
   id INT PRIMARY KEY,
   enterprise_id INT,
   vehicle_type varchar(50),
   distance INT,
   fuel_type varchar(50),
   emission_tags varchar(50),
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
   emission_tags varchar(50),
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
   origin varchar(250),
   destination varchar(250),
   emission_tags varchar(50),
   aircraft_type varchar(250),
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
   elec_usage varchar(250),
   emission_tags varchar(250),
   heat_gas varchar(50),
   FOREIGN KEY (user_id) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS Ent_NGO;
CREATE TABLE IF NOT EXISTS Ent_NGO (
   Enterprise_ID INT,
   NGO_ID INT,
   PRIMARY KEY(Enterprise_ID, NGO_ID),
   FOREIGN KEY (Enterprise_ID) REFERENCES Enterprises(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   FOREIGN KEY (NGO_ID) REFERENCES NGO(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS User_NGO;
CREATE TABLE IF NOT EXISTS User_NGO (
   User_ID INT,
   NGO_ID INT,
   PRIMARY KEY(User_ID, NGO_ID),
   FOREIGN KEY (User_ID) REFERENCES User(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   FOREIGN KEY (NGO_ID) REFERENCES NGO(id)
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


DROP TABLE IF EXISTS ResTags;
CREATE TABLE IF NOT EXISTS ResTags (
   Res_ID INT,
   Emission_Tag INT,
   PRIMARY KEY(Res_ID, Emission_Tag),
   FOREIGN KEY (Res_ID) REFERENCES ResData(id)
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


DROP TABLE IF EXISTS MissionTags;
CREATE TABLE IF NOT EXISTS MissionTags (
   NGO_ID INT,
   Emission_Tag INT,
   PRIMARY KEY(NGO_ID, Emission_Tag),
   FOREIGN KEY (NGO_ID) REFERENCES NGO(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


DROP TABLE IF EXISTS EntTags;
CREATE TABLE IF NOT EXISTS EntTags (
   Enterprises_ID INT,
   Emission_Tag INT,
   PRIMARY KEY(Enterprises_ID, Emission_Tag),
   FOREIGN KEY (Enterprises_ID) REFERENCES Enterprises(id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);



