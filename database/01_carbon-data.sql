USE CarbonConnect;

INSERT INTO Country (id, emissions, name) VALUES (1, 108871.68, 'Belgium');
INSERT INTO Country (id, emissions, name) VALUES (2, 59082.72, 'Bulgaria');
INSERT INTO Country (id, emissions, name) VALUES (3, 118500.35, 'Czechia');
INSERT INTO Country (id, emissions, name) VALUES (4, 44243.3, 'Denmark');
INSERT INTO Country (id, emissions, name) VALUES (5, 777380.09, 'Germany');
INSERT INTO Country (id, emissions, name) VALUES (6, 14125.06, 'Estonia');
INSERT INTO Country (id, emissions, name) VALUES (7, 63650.14, 'Ireland');
INSERT INTO Country (id, emissions, name) VALUES (8, 82242.9, 'Greece');
INSERT INTO Country (id, emissions, name) VALUES (9, 309286.15, 'Spain');
INSERT INTO Country (id, emissions, name) VALUES (10, 409732.55, 'France');
INSERT INTO Country (id, emissions, name) VALUES (11, 26258.1, 'Croatia');
INSERT INTO Country (id, emissions, name) VALUES (12, 419467.07, 'Italy');
INSERT INTO Country (id, emissions, name) VALUES (13, 9572.78, 'Cyprus');
INSERT INTO Country (id, emissions, name) VALUES (14, 10568.91, 'Latvia');
INSERT INTO Country (id, emissions, name) VALUES (15, 19249.2, 'Lithuania');
INSERT INTO Country (id, emissions, name) VALUES (16, 10145.27, 'Luxembourg');
INSERT INTO Country (id, emissions, name) VALUES (17, 60331.72, 'Hungary');
INSERT INTO Country (id, emissions, name) VALUES (18, 2647.72, 'Malta');
INSERT INTO Country (id, emissions, name) VALUES (19, 162999.6, 'Netherlands');
INSERT INTO Country (id, emissions, name) VALUES (20, 74825.78, 'Austria');
INSERT INTO Country (id, emissions, name) VALUES (21, 383434.04, 'Poland');
INSERT INTO Country (id, emissions, name) VALUES (22, 60581.36, 'Portugal');
INSERT INTO Country (id, emissions, name) VALUES (23, 109992.76, 'Romania');
INSERT INTO Country (id, emissions, name) VALUES (24, 15676.64, 'Slovenia');
INSERT INTO Country (id, emissions, name) VALUES (25, 37183,78, 'Slovakia');
INSERT INTO Country (id, emissions, name) VALUES (26, 47341.71, 'Finland');
INSERT INTO Country (id, emissions, name) VALUES (27, 47074.61, 'Sweden');
INSERT INTO Country (id, emissions, name) VALUES (28, 5402.55, 'Iceland');
INSERT INTO Country (id, emissions, name) VALUES (29, 50255.43, 'Norway');
INSERT INTO Country (id, emissions, name) VALUES (30, 45847.17, 'Switzerland');




INSERT INTO EmissionTags (id, description) VALUES
(1, 'Transport'),
(2, 'Flights'),
(3, 'Energy'),
(4, 'Heat');

INSERT INTO Enterprises (id, name, type, emission_result, misc_emissions, country_id) VALUES
(1, 'Enterprise One', 'Type A', 10, 'Misc A', 1),
(2, 'Enterprise Two', 'Type B', 20, 'Misc B', 2),
(3, 'Enterprise Three', 'Type C', 30, 'Misc C', 3),
(4, 'Enterprise Four', 'Type D', 40, 'Misc D', 3);

INSERT INTO EntTags (enterprise_id, tag_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 3),
(4, 2),
(4, 1);

INSERT INTO NGO (id, website, name, contact) VALUES
(1, 'logo1.png', 'NGO One', 'contact1@ngo1.org'),
(2, 'logo2.png', 'NGO Two', 'contact2@ngo2.org'),
(3, 'logo3.png', 'NGO Three', 'contact3@ngo3.org');

INSERT INTO NGOTags (ngo_id, tag_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 3);

INSERT INTO User (id, emission_result, country_id) VALUES
(1, 100, 1),
(2, 200, 2),
(3, 300, 3);

INSERT INTO ResData (id, user_id, elec_usage, emission_tags, heating, water_heating, cooking_gas) VALUES
(200, 1, 1000.0, 'res', 2000.0, 1.0, 11.0)

INSERT INTO UserTags (user_id, tag_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 1),
(3, 3);

INSERT INTO Cars (id, user_id, fuel_type, emission_tags, fuel_used) VALUES
(1, 1, 'Gasoline/Hybrid', 'car', 100.0),
(2, 2, 'Diesel', 'car', 200.0),
(3, 3, 'Electric', 'car', 304.0);