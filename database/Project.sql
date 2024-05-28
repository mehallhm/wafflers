DROP DATABASE IF EXISTS CarbonConnect;
CREATE DATABASE IF NOT EXISTS CarbonConnect;
USE CarbonConnect;
CREATE TABLE IF NOT EXISTS NGO (
	id integer UNIQUE NOT NULL,
    PRIMARY KEY(id),
    website varchar(255) UNIQUE NOT NULL,
	name varchar(50) ,
    mission_tags varchar(50),
    contact varchar(50));

CREATE TABLE IF NOT EXISTS Enterprises(
    name varchar(50),
    id integer UNIQUE NOT NULL,
    type varchar(255),
    emission_result varchar(255),
    misc_emissions varchar(255)
);
CREATE TABLE IF NOT EXISTS Users(
    id integer UNIQUE NOT NULL,
    tags varchar(255));
CREATE TABLE IF NOT EXISTS SupplyChain(
    vehicle_type varchar(50),
    distance integer,
    fuel_type varchar(50),
    emission_tags varchar(50),
    entity_id integer);
CREATE TABLE IF NOT EXISTS Country(
    id integer,
    emissions varchar(255),
    name varchar(50)
);
CREATE TABLE IF NOT EXISTS PublicTransport(
    distance int,
    trainCount int,
    busCount int,
    emission_tags varchar(50) UNIQUE NOT NULL,

)