USE CarbonConnect;

INSERT INTO Country (id, emissions, name) VALUES (1, '5.8 million metric tons', 'CountryA');
INSERT INTO Country (id, emissions, name) VALUES (2, '15.2 million metric tons', 'CountryB');
INSERT INTO Country (id, emissions, name) VALUES (3, '20.7 million metric tons', 'CountryC');

INSERT INTO EmissionTags (id, description) VALUES
(1, 'Tag Description One'),
(2, 'Tag Description Two'),
(3, 'Tag Description Three');

INSERT INTO Enterprises (id, name, type, emission_result, misc_emissions, country_id) VALUES
(1, 'Enterprise One', 'Type A', 'Result A', 'Misc A', 1),
(2, 'Enterprise Two', 'Type B', 'Result B', 'Misc B', 2),
(3, 'Enterprise Three', 'Type C', 'Result C', 'Misc C', 3);

INSERT INTO EntTags (enterprise_id, tag_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 3);

INSERT INTO NGO (id, logo, website, name, contact) VALUES
(1, 'logo1.png', 'https://www.ngo1.org', 'NGO One', 'contact1@ngo1.org'),
(2, 'logo2.png', 'https://www.ngo2.org', 'NGO Two', 'contact2@ngo2.org'),
(3, 'logo3.png', 'https://www.ngo3.org', 'NGO Three', 'contact3@ngo3.org');

INSERT INTO NGOTags (ngo_id, tag_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 2),
(3, 3);