USE CarbonConnect;

INSERT INTO Country (id, emissions, name) VALUES (1, 108871.68 / 11719000, 'Belgium');
INSERT INTO Country (id, emissions, name) VALUES (2, 59082.72 / 6519789, 'Bulgaria');
INSERT INTO Country (id, emissions, name) VALUES (3, 118500.35 / 10693939, 'Czechia');
INSERT INTO Country (id, emissions, name) VALUES (4, 44243.3 / 5932000, 'Denmark');
INSERT INTO Country (id, emissions, name) VALUES (5, 777380.09 / 83166711, 'Germany');
INSERT INTO Country (id, emissions, name) VALUES (6, 14125.06 / 1331796, 'Estonia');
INSERT INTO Country (id, emissions, name) VALUES (7, 63650.14 / 5158000, 'Ireland');
INSERT INTO Country (id, emissions, name) VALUES (8, 82242.9 / 10384971, 'Greece');
INSERT INTO Country (id, emissions, name) VALUES (9, 309286.15 / 47556000, 'Spain');
INSERT INTO Country (id, emissions, name) VALUES (10, 409732.55 / 68075000, 'France');
INSERT INTO Country (id, emissions, name) VALUES (11, 26258.1 / 3850000, 'Croatia');
INSERT INTO Country (id, emissions, name) VALUES (12, 419467.07 / 58982000, 'Italy');
INSERT INTO Country (id, emissions, name) VALUES (13, 9572.78 / 1231000, 'Cyprus');
INSERT INTO Country (id, emissions, name) VALUES (14, 10568.91 / 1848837, 'Latvia');
INSERT INTO Country (id, emissions, name) VALUES (15, 19249.2 / 2857000, 'Lithuania');
INSERT INTO Country (id, emissions, name) VALUES (16, 10145.27 / 645397, 'Luxembourg');
INSERT INTO Country (id, emissions, name) VALUES (17, 60331.72 / 9594214, 'Hungary');
INSERT INTO Country (id, emissions, name) VALUES (18, 2647.72 / 514564, 'Malta');
INSERT INTO Country (id, emissions, name) VALUES (19, 162999.6 / 17556000, 'Netherlands');
INSERT INTO Country (id, emissions, name) VALUES (20, 74825.78 / 9121000, 'Austria');
INSERT INTO Country (id, emissions, name) VALUES (21, 383434.04 / 37623000, 'Poland');
INSERT INTO Country (id, emissions, name) VALUES (22, 60581.36 / 10352042, 'Portugal');
INSERT INTO Country (id, emissions, name) VALUES (23, 109992.76 / 18979000, 'Romania');
INSERT INTO Country (id, emissions, name) VALUES (24, 15676.64 / 2100000, 'Slovenia');
INSERT INTO Country (id, emissions, name) VALUES (25, 37183.78 / 5404322, 'Slovakia');
INSERT INTO Country (id, emissions, name) VALUES (26, 47341.71 / 5548000, 'Finland');
INSERT INTO Country (id, emissions, name) VALUES (27, 47074.61 / 10540725, 'Sweden');
INSERT INTO Country (id, emissions, name) VALUES (28, 5402.55 / 376248, 'Iceland');
INSERT INTO Country (id, emissions, name) VALUES (29, 50255.43 / 5488984, 'Norway');
INSERT INTO Country (id, emissions, name) VALUES (30, 45847.17 / 8803000, 'Switzerland');


INSERT INTO EmissionTags (id, description) VALUES
(1, 'Transport'),
(2, 'Flights'),
(3, 'Energy'),
(4, 'Heat');

insert into NGO (id, website, name, contact, bio, vectorized_bio) values (1, 'EcoUnity.com', 'EcoUnity Europe', 'Joe@EcoUnity.org', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (2, 'seesaa.net', 'Grimes, Fahey and Mertz', 'rattlee1@accuweather.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (3, 'fema.gov', 'Terry-Witting', 'sdand2@angelfire.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (4, 'twitpic.com', 'Kub-Anderson', 'swilson3@pinterest.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (5, 'netvibes.com', 'Bosco, Davis and Feil', 'baspinal4@example.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (6, 'pbs.org', 'Morar LLC', 'lwagg5@answers.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (7, 'bloglovin.com', 'Macejkovic-Ebert', 'rmushett6@pbs.org', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (8, 'fda.gov', 'Cormier, Ratke and Koelpin', 'weakins7@wordpress.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (9, 'ustream.tv', 'Becker-Brakus', 'mchislett8@imdb.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (10, 'elegantthemes.com', 'Miller-O''Conner', 'pchrippes9@auda.org.au', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (11, 'ezinearticles.com', 'Hirthe-Emmerich', 'kmillionsa@tamu.edu', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (12, 'simplemachines.org', 'Jacobson, Torphy and Strosin', 'sgowanlockb@nature.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (13, 'bigcartel.com', 'Waters, Legros and Toy', 'npirdyc@sphinn.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (14, 'apple.com', 'Ortiz, Pollich and Jerde', 'tiversd@wp.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (15, 'slashdot.org', 'Corwin-Shields', 'bbeechcrafte@google.com.br', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (16, 'networksolutions.com', 'Zieme, Bergstrom and Schultz', 'srowswellf@moonfruit.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (17, 'un.org', 'Hand-Schroeder', 'rtimbridgeg@mayoclinic.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (18, 'phoca.cz', 'Feest-Armstrong', 'tionnh@slashdot.org', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (19, 'blogspot.com', 'Rice Inc', 'struelocki@mtv.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (20, 'businessinsider.com', 'Marks Group', 'brothamj@addtoany.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (21, 'hud.gov', 'Barrows Inc', 'elownesk@gizmodo.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (22, 'goodreads.com', 'Deckow-Adams', 'sbrowettl@blogspot.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (23, 'homestead.com', 'Brekke, Hauck and Buckridge', 'cjeevesm@japanpost.jp', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (24, 'blogtalkradio.com', 'Hackett Inc', 'skerrichn@nih.gov', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (25, 'economist.com', 'Veum and Sons', 'jphilbrooko@blogspot.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (26, 'ameblo.jp', 'Gutmann-Lockman', 'gharkessp@bandcamp.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (27, 'dropbox.com', 'Kutch-Hahn', 'eaveyardq@umn.edu', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (28, 'dedecms.com', 'Fay-Murphy', 'kyellowleesr@omniture.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (29, '1und1.de', 'Kohler, Ankunding and Doyle', 'darmells@drupal.org', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (30, 'webnode.com', 'Lueilwitz-McGlynn', 'akeeleyt@cyberchimps.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (31, 'prnewswire.com', 'Baumbach-Kemmer', 'ksucreu@imageshack.us', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (32, 'lycos.com', 'Rodriguez, Kassulke and Moore', 'ldallingv@phpbb.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (33, 't-online.de', 'Grimes Group', 'fjanotaw@odnoklassniki.ru', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (34, 'drupal.org', 'Schmitt Group', 'jhimsworthx@icio.us', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (35, 'mlb.com', 'Mohr-Huel', 'tcunliffey@geocities.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (36, 'uol.com.br', 'Mante, Simonis and Gusikowski', 'mgoodwinz@pcworld.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (37, 'utexas.edu', 'Upton LLC', 'hjoska10@theglobeandmail.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (38, 'infoseek.co.jp', 'Steuber-Pfannerstill', 'aalsina11@cpanel.net', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (39, 'imgur.com', 'Lockman, Baumbach and Cassin', 'cnassie12@diigo.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (40, 'list-manage.com', 'Kreiger-Bednar', 'rfretwell13@cnet.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (41, 'netscape.com', 'Lindgren, McLaughlin and Wisoky', 'xhealings14@pinterest.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (42, 'wikia.com', 'Ernser LLC', 'tdurrad15@dyndns.org', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (43, 'wordpress.org', 'Becker, Quigley and Grimes', 'awaulker16@360.cn', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (44, 'opensource.org', 'Hudson, Shields and Buckridge', 'cgussie17@blinklist.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (45, 'businessinsider.com', 'Schaden-Stanton', 'gmangon18@google.com.au', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (46, 'unicef.org', 'Wunsch and Sons', 'pbullock19@amazonaws.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (47, 'salon.com', 'Glover-Herzog', 'gvenney1a@dell.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (48, 'mac.com', 'Smitham-Konopelski', 'kpugsley1b@dailymail.co.uk', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (49, 'washingtonpost.com', 'Dickens-Rohan', 'nbartoloma1c@yellowpages.com', 'empty bio', 'empty vector');
insert into NGO (id, website, name, contact, bio, vectorized_bio) values (50, 'istockphoto.com', 'Nader Group', 'jletts1d@bbb.org', 'empty bio', 'empty vector');

insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (1, 1, 'EcoForward Enterprises', 'Lighting', .08932, 20);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (2, 1, 'EcoForward Enterprises', 'Lighting', .09332, 20);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (3, 3, 'Reinger-Tremblay', 'Telecommunications Equipment', 0.09559, 6);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (4, 4, 'Rau Inc', 'Specialty Chemicals', 0.10831, 23);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (5, 5, 'Dicki, Koch and Nolan', 'Restaurants', 0.03259, 9);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (6, 6, 'Goyette-Harris', 'Metal Fabrications', 0.0386, 22);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (7, 7, 'Feil-Krajcik', 'Metal Fabrications', 0.09158, 9);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (8, 8, 'Stamm-Kemmer', 'n/a', 0.08782, 13);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (9, 9, 'O''Reilly-Schumm', 'Major Banks', 0.07504, 29);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (10, 10, 'Willms, Cummerata and Abshire', 'Major Pharmaceuticals', 0.10664, 25);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (11, 11, 'Rolfson Group', 'Steel/Iron Ore', 0.0503, 7);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (12, 12, 'Bergnaum-Osinski', 'Industrial Machinery/Components', 0.04369, 12);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (13, 13, 'Sanford-Wuckert', 'Construction/Ag Equipment/Trucks', 0.0297, 1);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (14, 14, 'Kirlin and Sons', 'Medical Specialities', 0.10009, 16);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (15, 15, 'Hessel-Rowe', 'Biotechnology: Biological Products (No Diagnostic Substances)', 0.04416, 17);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (16, 16, 'Spinka, Ziemann and Cronin', 'n/a', 0.04827, 16);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (17, 17, 'Jenkins, Pagac and Gibson', 'n/a', 0.02494, 7);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (18, 18, 'Boyer-Heller', 'Package Goods/Cosmetics', 0.08924, 30);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (19, 19, 'Morissette Group', 'Major Banks', 0.03168, 18);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (20, 20, 'Little, Hintz and Blanda', 'n/a', 0.07561, 25);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (21, 21, 'Kuhlman-Vandervort', 'Telecommunications Equipment', 0.05408, 22);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (22, 22, 'Harvey, Mann and Carter', 'Major Pharmaceuticals', 0.05748, 2);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (23, 23, 'Bruen, Beier and Bins', 'Apparel', 0.04154, 17);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (24, 24, 'Keebler and Sons', 'Specialty Chemicals', 0.07983, 30);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (25, 25, 'Turcotte, Baumbach and Cruickshank', 'Oil & Gas Production', 0.07671, 26);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (26, 26, 'Kozey Inc', 'Major Pharmaceuticals', 0.04877, 14);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (27, 27, 'Pagac, Stiedemann and Cormier', 'Major Pharmaceuticals', 0.08622, 16);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (28, 28, 'Effertz Group', 'Real Estate Investment Trusts', 0.05617, 20);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (29, 29, 'O''Reilly-Kulas', 'Real Estate Investment Trusts', 0.10163, 10);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (30, 30, 'Schoen and Sons', 'n/a', 0.02089, 28);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (31, 31, 'Schoen Group', 'Medical/Nursing Services', 0.06484, 9);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (32, 32, 'Kris-Kreiger', 'n/a', 0.04461, 4);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (33, 33, 'D''Amore Inc', 'n/a', 0.05681, 19);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (34, 34, 'Bernhard and Sons', 'n/a', 0.07331, 9);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (35, 35, 'Tillman-Kerluke', 'Television Services', 0.10595, 22);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (36, 36, 'Kuphal and Sons', 'n/a', 0.04639, 14);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (37, 37, 'Nitzsche, Keebler and Mitchell', 'Major Pharmaceuticals', 0.03214, 11);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (38, 38, 'Kuvalis, Witting and Lockman', 'Biotechnology: Biological Products (No Diagnostic Substances)', 0.08446, 21);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (39, 39, 'Legros LLC', 'Packaged Foods', 0.08871, 29);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (40, 40, 'Willms Inc', 'Real Estate Investment Trusts', 0.05577, 29);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (41, 41, 'Bode-Fadel', 'Precious Metals', 0.04988, 12);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (42, 42, 'Frami LLC', 'Electric Utilities: Central', 0.1043, 7);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (43, 43, 'Nader, Green and Gibson', 'n/a', 0.02407, 9);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (44, 44, 'Mohr Inc', 'Coal Mining', 0.07562, 29);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (45, 45, 'Robel, Mohr and Gulgowski', 'Department/Specialty Retail Stores', 0.08512, 12);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (46, 46, 'Daugherty, Jenkins and Zieme', 'Major Pharmaceuticals', 0.09563, 3);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (47, 47, 'Goodwin and Sons', 'Computer Software: Prepackaged Software', 0.07401, 3);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (48, 48, 'Zboncak, Rolfson and Rippin', 'Telecommunications Equipment', 0.07957, 20);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (49, 49, 'Larson Inc', 'Semiconductors', 0.05738, 28);
insert into Enterprises (survey_id, id, name, type, emission_result, country_id) values (50, 50, 'Kris-O''Conner', 'Metal Fabrications', 0.04614, 14);

INSERT INTO User (id, emission_result, country_id, email, match_consent, name, bio, vectorized_bio)
VALUES
(1, 0.00583, 1, 'NatAllard@360.cn', true, 'Natalie', 'empty bio', 'empty vector'),
(2, 0.00528, 22, 'iworham1@rakuten.co.jp', true, 'Innis', 'empty bio', 'empty vector'),
(3, 0.00399, 2, 'lhowselee2@newyorker.com', false, 'Leoline', 'empty bio', 'empty vector'),
(4, 0.00373, 2, 'emintrim3@usatoday.com', false, 'Erl', 'empty bio', 'empty vector'),
(5, 0.01438, 29, 'fbulford4@barnesandnoble.com', false, 'Fidela', 'empty bio', 'empty vector'),
(6, 0.01259, 23, 'pstiegar5@godaddy.com', true, 'Philippa', 'empty bio', 'empty vector'),
(7, 0.01405, 27, 'wbowden6@meetup.com', true, 'Wandie', 'empty bio', 'empty vector'),
(8, 0.00719, 26, 'jhardage7@cafepress.com', true, 'Jeff', 'empty bio', 'empty vector'),
(9, 0.01142, 29, 'jmanston8@bizjournals.com', false, 'Jose', 'empty bio', 'empty vector'),
(10, 0.00432, 24, 'lsmeeton9@hp.com', true, 'Lutero', 'empty bio', 'empty vector'),
(11, 0.00828, 12, 'epentina@economist.com', false, 'Edwin', 'empty bio', 'empty vector'),
(12, 0.00714, 14, 'asivilb@typepad.com', true, 'Alfy', 'empty bio', 'empty vector'),
(13, 0.00384, 8, 'hkinsleyc@cbsnews.com', true, 'Horst', 'empty bio', 'empty vector'),
(14, 0.0107, 5, 'scuestad@smh.com.au', true, 'Sarge', 'empty bio', 'empty vector'),
(15, 0.00623, 13, 'vmaffullie@marriott.com', false, 'Verla', 'empty bio', 'empty vector'),
(16, 0.0078, 30, 'bprewf@intel.com', false, 'Braden', 'empty bio', 'empty vector'),
(17, 0.01114, 5, 'sshimukg@dedecms.com', true, 'Sharla', 'empty bio', 'empty vector'),
(18, 0.00447, 25, 'frothamh@archive.org', false, 'Fanechka', 'empty bio', 'empty vector'),
(19, 0.0112, 1, 'gsteersi@alibaba.com', false, 'Gregory', 'empty bio', 'empty vector'),
(20, 0.01011, 6, 'lstephensj@wunderground.com', false, 'Lester', 'empty bio', 'empty vector'),
(21, 0.00678, 14, 'tbloyk@blogs.com', false, 'Trenton', 'empty bio', 'empty vector'),
(22, 0.00678, 29, 'aleaheyl@barnesandnoble.com', true, 'Anne-marie', 'empty bio', 'empty vector'),
(23, 0.0045, 3, 'jbeckmannm@lulu.com', false, 'Justis', 'empty bio', 'empty vector'),
(24, 0.00828, 29, 'acroftn@mlb.com', false, 'Analiese', 'empty bio', 'empty vector'),
(25, 0.01013, 26, 'qlowatero@google.ca', false, 'Quintin', 'empty bio', 'empty vector'),
(26, 0.00526, 21, 'mendlep@twitter.com', false, 'Moselle', 'empty bio', 'empty vector'),
(27, 0.01406, 7, 'hdyteq@purevolume.com', true, 'Helen-elizabeth', 'empty bio', 'empty vector'),
(28, 0.00851, 24, 'jimortsr@tripod.com', false, 'Jessamine', 'empty bio', 'empty vector'),
(29, 0.00417, 22, 'kmanbys@bravesites.com', false, 'Kev', 'empty bio', 'empty vector'),
(30, 0.00655, 15, 'saldgatet@mediafire.com', true, 'Stavro', 'empty bio', 'empty vector'),
(31, 0.0039, 5, 'tpietrusiaku@soup.io', true, 'Tonye', 'empty bio', 'empty vector'),
(32, 0.01409, 16, 'gcheesmanv@qq.com', false, 'Giorgia', 'empty bio', 'empty vector'),
(33, 0.00453, 28, 'cbrimblecombew@cbsnews.com', false, 'Camellia', 'empty bio', 'empty vector'),
(34, 0.00965, 24, 'hboulex@utexas.edu', false, 'Hillel', 'empty bio', 'empty vector'),
(35, 0.00447, 24, 'lmcilherrany@meetup.com', true, 'Laurice', 'empty bio', 'empty vector'),
(36, 0.0138, 19, 'apfertnerz@intel.com', false, 'Angelita', 'empty bio', 'empty vector'),
(37, 0.01118, 9, 'kseydlitz10@photobucket.com', false, 'Kain', 'empty bio', 'empty vector'),
(38, 0.00957, 23, 'rcicero11@sphinn.com', true, 'Raychel', 'empty bio', 'empty vector'),
(39, 0.01052, 5, 'lhasling12@yelp.com', true, 'Livvie', 'empty bio', 'empty vector'),
(40, 0.01241, 25, 'gdabbs13@taobao.com', false, 'Garvin', 'empty bio', 'empty vector'),
(41, 0.00756, 27, 'jthackray14@naver.com', false, 'Jeffry', 'empty bio', 'empty vector'),
(42, 0.0051, 9, 'psaxon15@uiuc.edu', false, 'Paula', 'empty bio', 'empty vector'),
(43, 0.01175, 20, 'asharplin16@businessweek.com', true, 'Addison', 'empty bio', 'empty vector'),
(44, 0.00704, 11, 'mfrain17@g.co', false, 'Mavis', 'empty bio', 'empty vector'),
(45, 0.00482, 17, 'kkibbye18@friendfeed.com', true, 'Karalee', 'empty bio', 'empty vector'),
(46, 0.01096, 13, 'escurrell19@nasa.gov', false, 'Erwin', 'empty bio', 'empty vector'),
(47, 0.00738, 10, 'mstolli1a@youku.com', false, 'Melany', 'empty bio', 'empty vector'),
(48, 0.01385, 25, 'nstepney1b@e-recht24.de', true, 'Nickey', 'empty bio', 'empty vector'),
(49, 0.00729, 26, 'rsaynor1c@google.com.br', false, 'Randene', 'empty bio', 'empty vector'),
(50, 0.00844, 10, 'rfeake1d@nationalgeographic.com', true, 'Rivalee', 'empty bio', 'empty vector');


insert into EntTags (enterprise_survey_id, tag_id) values (1, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (1, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (2, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (2, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (3, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (3, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (4, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (4, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (14, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (44, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (17, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (16, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (47, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (19, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (35, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (28, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (1, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (14, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (22, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (31, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (29, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (50, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (36, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (31, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (10, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (3, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (37, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (49, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (16, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (32, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (8, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (34, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (14, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (20, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (44, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (41, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (27, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (28, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (39, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (48, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (36, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (33, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (50, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (32, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (23, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (31, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (38, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (1, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (40, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (9, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (29, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (7, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (24, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (45, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (21, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (6, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (5, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (49, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (36, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (10, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (36, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (11, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (13, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (20, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (46, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (2, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (30, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (17, 3);
insert into EntTags (enterprise_survey_id, tag_id) values (26, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (2, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (30, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (16, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (49, 2);
insert into EntTags (enterprise_survey_id, tag_id) values (45, 4);
insert into EntTags (enterprise_survey_id, tag_id) values (23, 1);
insert into EntTags (enterprise_survey_id, tag_id) values (15, 4);


insert into NGOTags (ngo_id, tag_id) values (32, 3);
insert into NGOTags (ngo_id, tag_id) values (29, 1);
insert into NGOTags (ngo_id, tag_id) values (9, 1);
insert into NGOTags (ngo_id, tag_id) values (34, 3);
insert into NGOTags (ngo_id, tag_id) values (22, 4);
insert into NGOTags (ngo_id, tag_id) values (17, 3);
insert into NGOTags (ngo_id, tag_id) values (6, 3);
insert into NGOTags (ngo_id, tag_id) values (2, 1);
insert into NGOTags (ngo_id, tag_id) values (17, 2);
insert into NGOTags (ngo_id, tag_id) values (41, 4);
insert into NGOTags (ngo_id, tag_id) values (21, 4);
insert into NGOTags (ngo_id, tag_id) values (40, 4);
insert into NGOTags (ngo_id, tag_id) values (30, 3);
insert into NGOTags (ngo_id, tag_id) values (15, 2);
insert into NGOTags (ngo_id, tag_id) values (25, 4);
insert into NGOTags (ngo_id, tag_id) values (44, 1);
insert into NGOTags (ngo_id, tag_id) values (33, 4);
insert into NGOTags (ngo_id, tag_id) values (37, 4);
insert into NGOTags (ngo_id, tag_id) values (22, 2);
insert into NGOTags (ngo_id, tag_id) values (22, 3);
insert into NGOTags (ngo_id, tag_id) values (9, 2);
insert into NGOTags (ngo_id, tag_id) values (46, 1);
insert into NGOTags (ngo_id, tag_id) values (12, 1);
insert into NGOTags (ngo_id, tag_id) values (43, 3);
insert into NGOTags (ngo_id, tag_id) values (27, 4);
insert into NGOTags (ngo_id, tag_id) values (24, 2);
insert into NGOTags (ngo_id, tag_id) values (44, 3);
insert into NGOTags (ngo_id, tag_id) values (11, 4);
insert into NGOTags (ngo_id, tag_id) values (1, 4);
insert into NGOTags (ngo_id, tag_id) values (18, 1);
insert into NGOTags (ngo_id, tag_id) values (39, 2);
insert into NGOTags (ngo_id, tag_id) values (10, 2);
insert into NGOTags (ngo_id, tag_id) values (38, 2);
insert into NGOTags (ngo_id, tag_id) values (31, 3);
insert into NGOTags (ngo_id, tag_id) values (50, 2);
insert into NGOTags (ngo_id, tag_id) values (30, 4);
insert into NGOTags (ngo_id, tag_id) values (37, 2);
insert into NGOTags (ngo_id, tag_id) values (42, 3);
insert into NGOTags (ngo_id, tag_id) values (35, 3);
insert into NGOTags (ngo_id, tag_id) values (8, 3);
insert into NGOTags (ngo_id, tag_id) values (20, 4);
insert into NGOTags (ngo_id, tag_id) values (45, 3);
insert into NGOTags (ngo_id, tag_id) values (23, 3);
insert into NGOTags (ngo_id, tag_id) values (5, 1);
insert into NGOTags (ngo_id, tag_id) values (38, 1);
insert into NGOTags (ngo_id, tag_id) values (15, 4);
insert into NGOTags (ngo_id, tag_id) values (38, 4);
insert into NGOTags (ngo_id, tag_id) values (49, 2);
insert into NGOTags (ngo_id, tag_id) values (36, 1);
insert into NGOTags (ngo_id, tag_id) values (13, 1);
insert into NGOTags (ngo_id, tag_id) values (28, 1);
insert into NGOTags (ngo_id, tag_id) values (43, 4);
insert into NGOTags (ngo_id, tag_id) values (36, 2);
insert into NGOTags (ngo_id, tag_id) values (33, 3);
insert into NGOTags (ngo_id, tag_id) values (14, 2);
insert into NGOTags (ngo_id, tag_id) values (4, 2);
insert into NGOTags (ngo_id, tag_id) values (50, 4);
insert into NGOTags (ngo_id, tag_id) values (16, 4);
insert into NGOTags (ngo_id, tag_id) values (47, 1);
insert into NGOTags (ngo_id, tag_id) values (48, 3);
insert into NGOTags (ngo_id, tag_id) values (1, 3);
insert into NGOTags (ngo_id, tag_id) values (26, 3);
insert into NGOTags (ngo_id, tag_id) values (42, 1);
insert into NGOTags (ngo_id, tag_id) values (19, 1);
insert into NGOTags (ngo_id, tag_id) values (20, 3);
insert into NGOTags (ngo_id, tag_id) values (7, 4);
insert into NGOTags (ngo_id, tag_id) values (18, 4);
insert into NGOTags (ngo_id, tag_id) values (3, 2);
insert into NGOTags (ngo_id, tag_id) values (14, 4);
insert into NGOTags (ngo_id, tag_id) values (47, 4);
insert into NGOTags (ngo_id, tag_id) values (12, 2);
insert into NGOTags (ngo_id, tag_id) values (31, 1);
insert into NGOTags (ngo_id, tag_id) values (7, 2);
insert into NGOTags (ngo_id, tag_id) values (34, 1);
insert into NGOTags (ngo_id, tag_id) values (8, 1);
insert into NGOTags (ngo_id, tag_id) values (50, 1);
insert into NGOTags (ngo_id, tag_id) values (37, 3);
insert into NGOTags (ngo_id, tag_id) values (13, 3);
insert into NGOTags (ngo_id, tag_id) values (35, 4);
insert into NGOTags (ngo_id, tag_id) values (41, 2);
insert into NGOTags (ngo_id, tag_id) values (10, 4);
insert into NGOTags (ngo_id, tag_id) values (25, 1);
insert into NGOTags (ngo_id, tag_id) values (48, 4);
insert into NGOTags (ngo_id, tag_id) values (24, 4);
insert into NGOTags (ngo_id, tag_id) values (2, 4);
insert into NGOTags (ngo_id, tag_id) values (19, 4);
insert into NGOTags (ngo_id, tag_id) values (5, 4);
insert into NGOTags (ngo_id, tag_id) values (28, 4);
insert into NGOTags (ngo_id, tag_id) values (12, 4);
insert into NGOTags (ngo_id, tag_id) values (3, 1);
insert into NGOTags (ngo_id, tag_id) values (6, 4);
insert into NGOTags (ngo_id, tag_id) values (43, 1);
insert into NGOTags (ngo_id, tag_id) values (39, 4);
insert into NGOTags (ngo_id, tag_id) values (23, 4);
insert into NGOTags (ngo_id, tag_id) values (26, 1);
insert into NGOTags (ngo_id, tag_id) values (4, 3);

insert into UserTags (user_id, tag_id) values (5, 1);
insert into UserTags (user_id, tag_id) values (33, 3);
insert into UserTags (user_id, tag_id) values (1, 2);
insert into UserTags (user_id, tag_id) values (33, 4);
insert into UserTags (user_id, tag_id) values (24, 4);
insert into UserTags (user_id, tag_id) values (38, 1);
insert into UserTags (user_id, tag_id) values (33, 2);
insert into UserTags (user_id, tag_id) values (11, 4);
insert into UserTags (user_id, tag_id) values (44, 1);
insert into UserTags (user_id, tag_id) values (36, 2);
insert into UserTags (user_id, tag_id) values (29, 4);
insert into UserTags (user_id, tag_id) values (16, 2);
insert into UserTags (user_id, tag_id) values (14, 4);
insert into UserTags (user_id, tag_id) values (35, 3);
insert into UserTags (user_id, tag_id) values (40, 4);
insert into UserTags (user_id, tag_id) values (24, 1);
insert into UserTags (user_id, tag_id) values (50, 1);
insert into UserTags (user_id, tag_id) values (19, 4);
insert into UserTags (user_id, tag_id) values (22, 2);
insert into UserTags (user_id, tag_id) values (38, 3);
insert into UserTags (user_id, tag_id) values (2, 1);
insert into UserTags (user_id, tag_id) values (2, 3);
insert into UserTags (user_id, tag_id) values (48, 2);
insert into UserTags (user_id, tag_id) values (17, 3);
insert into UserTags (user_id, tag_id) values (31, 4);
insert into UserTags (user_id, tag_id) values (15, 4);
insert into UserTags (user_id, tag_id) values (29, 2);
insert into UserTags (user_id, tag_id) values (13, 2);
insert into UserTags (user_id, tag_id) values (15, 1);
insert into UserTags (user_id, tag_id) values (44, 3);
insert into UserTags (user_id, tag_id) values (35, 1);
insert into UserTags (user_id, tag_id) values (48, 4);
insert into UserTags (user_id, tag_id) values (34, 4);
insert into UserTags (user_id, tag_id) values (8, 3);
insert into UserTags (user_id, tag_id) values (5, 4);
insert into UserTags (user_id, tag_id) values (23, 4);
insert into UserTags (user_id, tag_id) values (13, 3);
insert into UserTags (user_id, tag_id) values (36, 1);
insert into UserTags (user_id, tag_id) values (28, 2);
insert into UserTags (user_id, tag_id) values (50, 4);
insert into UserTags (user_id, tag_id) values (14, 3);
insert into UserTags (user_id, tag_id) values (38, 4);
insert into UserTags (user_id, tag_id) values (20, 2);
insert into UserTags (user_id, tag_id) values (22, 4);
insert into UserTags (user_id, tag_id) values (49, 2);
insert into UserTags (user_id, tag_id) values (43, 1);


INSERT INTO ResData (id, user_id, elec_usage, emission_tags, heating, water_heating, cooking_gas) VALUES
(200, 1, 7, 'res', .09, .0864, .0864);

INSERT INTO Cars (id, user_id, fuel_type, emission_tags, fuel_used) VALUES
(1, 1, 'Gasoline/Hybrid', 'car', .003334),
(2, 2, 'Diesel', 'car', 200.0 * .0000334),
(3, 3, 'Electric', 'car', 304.0 * .0000334);

INSERT INTO Beta_User (id, user_values) VALUES (1, '-3.58516566E-17, .163886704, .821830787');
