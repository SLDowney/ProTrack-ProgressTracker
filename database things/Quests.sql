BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Quests" (
	"quest_id"	INTEGER UNIQUE,
	"quest_done"	INTEGER NOT NULL DEFAULT 0,
	"quest_type"	TEXT,
	"quest_name"	TEXT,
	"quest_contact"	TEXT,
	"quest_description"	TEXT,
	"quest_coord"	INTEGER,
	"quest_location"	TEXT,
	"quest_region"	TEXT,
	"quest_reward"	TEXT,
	"quest_level"	INTEGER NOT NULL DEFAULT 1,
	"quest_alternateLocation"	TEXT,
	"quest_prereq"	TEXT,
	"quest_prestart"	TEXT,
	PRIMARY KEY("quest_id" AUTOINCREMENT)
);
INSERT INTO "Quests" ("quest_id","quest_done","quest_type","quest_name","quest_contact","quest_description","quest_coord","quest_location","quest_region","quest_reward","quest_level","quest_alternateLocation","quest_prereq","quest_prestart") VALUES (1,1,'Main','Find Princess Zelda','Steward Construct','','0448, -1313, 1535','Garden of Time','Great Sky Island','',1,NULL,NULL,NULL),
 (2,2,'Main','The Closed Door','Rauru','','0452, -0859, 1450','Temple of Time','Great Sky Island','',1,NULL,NULL,NULL),
 (3,2,'Main','To the Kingdom of Hyrule','Zelda''s Voice','','0444, -0631, 1472','Temple of Time','Great Sky Island','',1,NULL,NULL,NULL),
 (4,1,'Main','Crisis at Hyrule Castle','Purah','','-0254, 0153, 0026','Lookout Landing','Central Hyrule','',1,'First Gatehouse
',NULL,NULL),
 (5,2,'Main','Regional Phenomena','Purah','','-0252, 0153, 0026','Lookout Landing','Hyrule Field','',1,NULL,NULL,NULL),
 (6,2,'Main','Camera Work in the Depths','Josha','','-0252, 0146, 0020','Lookout Landing','Hyrule Field','',1,NULL,NULL,NULL),
 (7,1,'Main','Impa and the Geoglyphs','Cado','','-1615, 0558, 0032','New Serenne Stable','Hyrule Ridge','',1,NULL,NULL,NULL),
 (8,2,'Main','Tulin of Rito Village','Teba','','-3596, 1802, 0212','Rito Village','Tabantha Frontier','',1,NULL,NULL,NULL),
 (9,2,'Main','A Mystery in the Depths','Josha','','-0255, 0138, 0019','Lookout Landing','Hyrule Field','Huge Crystaline Charge, Hot-Air Balloon Schema Stone, Large Zonaite',1,NULL,NULL,NULL),
 (10,2,'Main','Riju of Gerudo Town','Riju','','-3889, -2969, 0043','Gerudo Town','Gerudo Desert','',1,NULL,NULL,NULL),
 (11,2,'Main','Yunobo of Goron City','Yunobo','','1649, 2447, 0381','Goron City','Eldin Canyon','',1,NULL,NULL,NULL),
 (12,2,'Main','The Sludge-Covered Statue','Yona','','3302, 0463, 0139','Zora''s Domain','Lanayru Great Spring','',1,NULL,NULL,NULL),
 (13,2,'Main','Sidon of the Zora','Yona','','3306, 0464, 0139','Zora''s Domain','Lanayru Great Spring','',1,NULL,NULL,NULL),
 (14,2,'Main','The Broken Slate','Jiahto','','3405, 0884, 0400','Toto Lake','Lanayru Great Spring','',2,NULL,NULL,'Sidon of the Zora'),
 (15,2,'Main','Clues to the Sky','Jiahto','','3404, 0877, 0399','Toto Lake','Lanayru Great Spring','',2,NULL,NULL,'Sidon of the Zora'),
 (16,2,'Main','Restoring the Zora Armor','Yona','','3845, 0568, 0485','Zora''s Domain','Lanayru Great Spring','',2,NULL,NULL,'Sidon of the Zora'),
 (17,0,'Main','The Dragon''s Tears','Impa','','-1615, 0558, 0032','New Serenne Stable','Hyrule Ridge','',1,NULL,NULL,NULL),
 (18,2,'Main','Find the Fifth Sage','Purah','','-0253, 0153, 0026','Lookout Landing','Hyrule Field','',1,NULL,NULL,NULL),
 (19,0,'Main','Secret of the Ring Ruins','Tauro','','1814, -0951, 0113','Kakariko Village','West Necluda','',1,NULL,NULL,NULL),
 (20,0,'Main','Guidance from Ages Past','Zonai Relic','','1363, -3263, 0431','Dragonhead Island','Faron Grasslands','',1,NULL,NULL,NULL),
 (21,0,'Main','Trail of the Master Sword','Mineru','','1367, -3309, -0737','Spirit Temple','Faron Grasslands Depths','',1,NULL,NULL,NULL),
 (22,0,'Main','Recovering the Hero''s Sword','Great Deku Tree','','0429, 2146, 0162','Korok Forest','Great Hyrule Forest','',1,NULL,NULL,NULL),
 (23,0,'Main','Destroy Ganondorf','Purah','','-0252, 0155, 0026','Lookout Landing','Central Hyrule','',1,NULL,NULL,NULL),
 (120,2,'Adventure','A Call from the Depths','Goddess Statue','Speak to the Goddess Statue in the Temple of Time Ruins',NULL,'Temple of Time Ruins','Great Plateau','1 Heart Container or Stamina Essence',1,'Great Plateau West Chasm
Great Plateau South Chasm
Great Plateau East Chasm
Great Plateau North Chasm
Great Abandoned Central Mine
Temple of Time Ruins',NULL,NULL),
 (121,0,'Adventure','A Deal With the Statue','Horned Statue','Explore the Royal Hidden Passage in search of the mysterious voice.','-0234, 0157, 0004','Royal Hidden Passage','Central Hyrule','Ability to swap Stamina and Heart containers',1,'Royal Hidden Passage',NULL,'Who Goes There?'),
 (122,2,'Adventure','A Letter to Koyin','Koyin','Rescue the Message Bottle from the pond and return it to Koyin.','3631, -2048, 0175','Hateno Village','Necluda','Hateno Cheese',1,'Lake Sumac',NULL,NULL),
 (123,0,'Adventure','A Monstrous Collection I','Kilton',NULL,'3960, 1642, 0128','Tarrey Town','Akkala','Monster Extract',1,NULL,'Mattison''s Independence
The Hunt for Bubbul Gems!
Camera Work in the Depths',NULL),
 (124,0,'Adventure','A Monstrous Collection II','Kilton',NULL,'3960, 1642, 0128','Tarrey Town','Akkala','Sneaky Monster Soup, Monster Extract',1,NULL,'A Monstrous Collection I',NULL),
 (125,0,'Adventure','A Monstrous Collection III','Kilton',NULL,'3960, 1642, 0128','Tarrey Town','Akkala','Monster Bridle, Monster Extract',1,NULL,'A Monstrous Collection II',NULL),
 (126,0,'Adventure','A Monstrous Collection IV','Kilton',NULL,'3960, 1642, 0128','Tarrey Town','Akkala','Monster Saddle, Monster Extract',1,NULL,'A Monstrous Collection III',NULL),
 (127,0,'Adventure','A Monstrous Collection V','Kilton',NULL,'3960, 1642, 0128','Tarrey Town','Akkala','Diamond, Monster Extract',1,NULL,'A Monstrous Collection IV',NULL),
 (128,0,'Adventure','A New Signature Food','Reede',NULL,'3429, -2082, 0131','Hateno Village','Necluda','100 Rupees',2,NULL,NULL,'Team Cece or Team Reede?'),
 (129,0,'Adventure','An Eerie Voice','Penn',NULL,'0504, -3444, 0047','Highland Stable','Faron','Rupees',2,'Haran Lakefront Well',NULL,'Potential Princess Sightings!'),
 (130,0,'Adventure','Bring Peace to Akkala!','Toren',NULL,'3005, 1126, 0281','Akkala Span','Akkala','100 Rupees',1,NULL,'Bring Peace to Eldin!',NULL),
 (131,0,'Adventure','Bring Peace to Eldin!','Toren',NULL,'2369, 3059, 0448','Lake Darman Monster Den','Eldin','100 Rupees',1,NULL,'1 Tower Complete',NULL),
 (132,0,'Adventure','Bring Peace to Faron!','Flaxel',NULL,'-0021, -3424, 0007','Menoat River Bridge','Faron','100 Rupees',1,NULL,'1 Tower Complete',NULL),
 (133,0,'Adventure','Bring Peace to Hebra!','Flaxel',NULL,'-1791, 2301, 0238','South Tabantha Snowfield','Tabantha Tundra','100 Rupees',1,NULL,'Bring Peace to Faron!',NULL),
 (134,0,'Adventure','Bring Peace to Hyrule Field!','Captain Hoz',NULL,'-0433, -0490, 0025','Southwest of Lookout Landing','Central Hyrule','100 Rupees',1,NULL,'1 Tower Complete',NULL),
 (135,0,'Adventure','Bring Peace to Necluda!','Captain Hoz',NULL,'2261, -1838, 0011','Fort Hateno','West Necluda','100 Rupees',1,NULL,'Bring Peace to Hyrule Field!',NULL),
 (136,0,'Adventure','Cece''s Secret','Sophie',NULL,'3357, -2139, 0120','Hateno Village','Mount Lanayru','10 x Ironshrooms',2,NULL,NULL,'Team Cece or Team Reede?'),
 (137,0,'Adventure','Filling Out the Compendium','Robbie',NULL,'3781, -2123, 0251','Hateno Ancient Tech Lab','Hateno Village, Mount Lanayru','Purchase pictures from Robbie to fill out Compendium',1,NULL,'Presenting: Sensor+ !',NULL),
 (138,0,'Adventure','For Our Princess!','Penn',NULL,'2583, 1154, 0148','Foothill Stable','Eldin','Rupees',2,'Foothill Monster Den',NULL,'Potential Princess Sightings!'),
 (139,1,'Adventure','Gourmets Gone Missing','Penn','The cook Gotter is worried about some regular guests who are overdue to arrive at the stable.','0377, -1043, 0016','Riverside Stable','Central Hyrule','Rupees',2,'Owlan Bridge
Batrea Lake',NULL,'Potential Princess Sightings!'),
 (140,2,'Adventure','Hateno Village Research Lab','Robbie',NULL,'-0249, 0136, 0019','Lookout Landing','Central Hyrule','Shrine Sensor',1,'Hateno Ancient Tech Lab','Camera Work in the Depths
A Mystery in the Depths',NULL),
 (141,2,'Adventure','Hestu''s Concerns','Hestu',NULL,NULL,NULL,'Hyrule Ridge','Inventory Expansion',1,NULL,NULL,NULL),
 (142,0,'Adventure','Honey, Bee Mine','Beetz',NULL,'2167, -1380, 0109','Southeast of Kakariko Village','West Necluda','100 Rupees',1,NULL,NULL,NULL),
 (143,0,'Adventure','Infiltrating the Yiga Clan','Mimos',NULL,'-3687, -1365, 0331','Yiga Clan Hideout','Gerudo Highland','Access to the Yiga Clan Hideout
Earthwake Technique
Thunder Helm
Yiga Armor
Yiga Mask
Yiga Tights',1,'Akkala Ancient Tech Lab
Yiga Clan Maritta Branch',NULL,NULL),
 (144,2,'Adventure','Investigate the Thyphlo Ruins','Kazul',NULL,'0373, 3095, 0174','Thyphlo Ruins','Great Hyrule Forest','Diamond
Large Zonai Charge
Big Battery
Dusk Claymore',1,NULL,'1 Temple Complete',NULL),
 (145,0,'Adventure','Lurelin Village Restoration Project','Bolson',NULL,'2875, -3443, 0000','Lurelin Village','East Necluda','Free Village Services',1,NULL,'Ruffian-Infested Village',NULL),
 (146,1,'Adventure','Master Kohga of the Yiga Clan','Kohga',NULL,'-0803, -1928, -0520','Great Abandoned Central Mine','Hyrule Field Depths','Autobuild Ability
Huge Crystal Charge
Fanplane
Huge Crystal Charge
Hovercraft
Huge Crystal Charge
Bolt Boat
Huge Crystal Charge
Diamond
Rocket Platform',1,'Great Abandoned Central Mine
Abandoned Gerudo Mine
Abandoned Lanayru Mine
Rito Village Chasm
Abandoned Hebra Mine',NULL,NULL),
 (147,2,'Adventure','Mattison''s Independence','Hudson','Speak to Hudson and Rhondson in Tarrey Town.','3938, 1590, 0129','Tarrey Town','Akkala','200 Rupees',1,'Tarrey Town Tunnel
Hudson Construction Site',NULL,NULL),
 (148,1,'Adventure','Messages from an Ancient Era','Wotsworth','Take pictures of the tablets on the Flower-Shaped Islands and return them to Wotsworth.','-0269, 0067, 0018','Lookout Landing','Central Hyrule','100 Rupees for each picture you show Wotsworth (1200 total).',1,'Kakariko Village','1 Temple Complete',NULL),
 (149,2,'Adventure','Potential Princess Sightings!','Traysi',NULL,'-3258, 1763, 0119','Lucky Clover Gazette','Tabantha Frontier','50 Rupees
50 Rupees, Lucky Clover Gazette Fabric
50 Rupees + 20 Rupees
50 Rupees + Froggy Sleeve
100 Rupees
100 Rupees
100 Rupees + 20 Rupees
100 Rupees + 20 Rupees
100 Rupees + Froggy Leggings
100 Rupees + 50 Rupees
200 Rupees
300 Rupees
Froggy Hood (on return to Traysi)',1,'South Akkala Stable
Foothill Stable
Woodland Stable
Highland Stable
Gerudo Canyon Stable
Snowfield Stable
New Serenne Stable
Outskirt Stable
Riverside Stable
Wetland Stable
Tabantha Bridge Stable
Dueling Peaks Stable
Lakeside Stable',NULL,NULL),
 (150,0,'Adventure','Presenting: Hero''s Path Mode!','Robbie','Speak to Robbie about getting Hero''s Path Mode.','3780, -2122, 0251','Hateno Village','Mount Lanayru','Hero''s Path Mode Unlocked',1,'Akkala Ancient Tech Lab','Hateno Village Research Lab',NULL),
 (151,1,'Adventure','Presenting: Sensor+ !','Robbie','Speak to Robbie about getting the Sensor+.','3780, -2122, 0251','Hateno Village','Mount Lanayru','Sensor+ Unlocked',1,'Akkala Ancient Tech Lab','Hateno Village Research Lab',NULL),
 (152,1,'Adventure','Presenting: The Travel Medallion!','Robbie','Speak to Robbie about gettin the Travel Medallion. After acquiring the prototype, Robbie will give you one Travel Medallion for 5 locations found, a second for 10 locations found, and a third for 15 locations found.','3780, -2122, 0251','Hateno Village','Mount Lanayru','Travel Medallions Unlocked',1,'Akkala Ancient Tech Lab','Hateno Village Research Lab',NULL),
 (153,0,'Adventure','Princess Zelda Kidnapped?!','Penn',NULL,'1758, -1925, 0040','Dueling Peaks Stable','West Necluda','Rupees',2,NULL,NULL,'Potential Princess Sightings!'),
 (154,0,'Adventure','Reede''s Secret','Clavia',NULL,'3422, -2092, 0130','Hateno Village','Mount Lanayru','10 x Hylian Tomatoes',2,NULL,NULL,'Team Cece or Team Reede?'),
 (155,0,'Adventure','Ruffian-Infested Village','Rozel',NULL,'2782, -3272, 0083','Cliff Overlooking Lurelin Village','East Necluda','Lurelin Village Restored',1,'Lurelin Village
Lurelin Village Well',NULL,NULL),
 (156,2,'Adventure','Serenade to a Great Fairy','Penn',NULL,'1047, 1149, 0022','Woodland Stable','Eldin Canyon','100 Rupees',2,NULL,NULL,'Potential Princess Sightings!'),
 (157,0,'Adventure','Serenade to Cotera','Mastro',NULL,'-1755, -1958, 0010','Dueling Peaks Stable','West Necluda','100 Rupees',1,NULL,'Serenade to a Great Fairy',NULL),
 (158,0,'Adventure','Serenade to Kaysa','Mastro',NULL,'-1406, -1264, 0032','Outskirt Stable','Central Hyrule','100 Rupees',1,NULL,'Serenade to a Great Fairy
The Flute Player''s Plan',NULL),
 (159,0,'Adventure','Serenade to Mija','Mastro',NULL,'-1630, 2589, 0234','Snowfield Stable','Tabantha Tundra','100 Rupees',1,NULL,'Serenade to a Great Fairy
The Hornist''s Dramatic Escape',NULL),
 (160,0,'Adventure','Team Cece or Team Reede?','Cece',NULL,'3354, -2125, 0121','Hateno Village','Mount Lanayru','Use of Clothing Shop',1,NULL,NULL,NULL),
 (161,1,'Adventure','The All-Clucking Cucco','Penn',NULL,'3163, 1716, 0201','South Akkala Stable','Akkala','Rupees',2,NULL,NULL,'Potential Princess Sightings!'),
 (162,0,'Adventure','The Beast and the Princess','Penn','Penn has heard rumors of Princess Zelda riding a beast in the subtropical region to the south.','-1348, 0734, 0085','New Serenne Stable','Hyrule Ridge','Rupees',2,'Lakeside Stable',NULL,'Potential Princess Sightings!'),
 (163,0,'Adventure','The Beckoning Woman','Penn',NULL,'-1413, -1295, 0031','Outskirt Stable','Central Hyrule','Rupees',2,NULL,NULL,'Potential Princess Sightings!'),
 (164,0,'Adventure','The Blocked Well','Penn',NULL,'-2817, -2235, 0029','Gerudo Canyon Stable','Gerudo','Rupees',2,'Gerudo Canyon Well',NULL,'Potential Princess Sightings!'),
 (165,2,'Adventure','The Corridor between Two Dragons','Kazul',NULL,'0373, 3095, 0174','Thyphlo Ruins','Great Hyrule Forest','3 Rubies',2,NULL,'Fire Temple','Investigate the Thyphlo Ruins'),
 (166,0,'Adventure','The Flute Player''s Plan','Pyper',NULL,'0528, -3395, 0056','Highland Stable','Faron','Big Hearty Truffle',1,NULL,NULL,NULL),
 (167,2,'Adventure','The Hornist''s Dramatic Escape','Eustus',NULL,'-3648, 0756, 0118','Tabantha Bridge Stable','Tabantha Frontier','3 Courser Bee Honey',1,NULL,NULL,NULL),
 (168,0,'Adventure','The Hunt for Bubbul Gems','Kilton',NULL,'1222, 1207, 0020','Woodland Stable','Woodland Stable, Eldin Canyon','Bokoblin Mask',1,NULL,NULL,NULL),
 (169,1,'Adventure','The Long Dragon','Kazul',NULL,'0373, 3095, 0174','Thyphlo Ruins','Great Hyrule Forest','3 Topaz',2,NULL,'Lightning Temple','Investigate the Thyphlo Ruins'),
 (170,0,'Adventure','The Mayoral Election','Sophie',NULL,'3357, -2139, 0120','Hateno Village','Mount Lanayru','Cece hat',1,NULL,'Team Cece or Team Reede?
A New Signature Food
Reede''s Secret
Cece''s Secret',NULL),
 (171,0,'Adventure','The Missing Farm Tools','Penn',NULL,'0876, -0159, 0025','Wetlands Stable','West Necluda','Rupees',2,'Floret Sandbar',NULL,'Potential Princess Sightings!'),
 (172,1,'Adventure','The Owl Protected by Dragons','Kazul',NULL,'0373, 3095, 0174','Thyphlo Ruins','Great Hyrule Forest','3 Sapphires',2,NULL,'Wind Temple','Investigate the Thyphlo Ruins'),
 (173,0,'Adventure','The Search for Koltin','Kilton',NULL,NULL,NULL,'Tarrey Town, Akkala','Koltin''s Shop',1,NULL,'The Hunt for Bubbul Gems!',NULL),
 (174,2,'Adventure','The Six Dragons','Kazul',NULL,'0373, 3095, 0174','Thyphlo Ruins','Great Hyrule Forest','5 Opals',2,NULL,'Water Temple','Investigate the Thyphlo Ruins'),
 (175,0,'Adventure','The Yiga Clan Exam','Yiga Blademaster',NULL,'-2479, -1794, 0137','Yiga Blademaster Station','Gerudo Highland','Ruby, Eightfold Longblade (Untarnished)',1,'Mount Nabooru Cave
Spectacle Rock
Gerudo Canyon Mine','Infiltrating the Yiga Clan',NULL),
 (176,0,'Adventure','White Goats Gone Missing','Penn',NULL,'-2910, 0524, 0169','Tabantha Bridge Stable','Hyrule Ridge','Rupees',2,NULL,NULL,'Potential Princess Sightings!'),
 (177,0,'Adventure','Who Goes There?','Jerrin',NULL,'-0256, 0107, 0008','Lookout Landing Emergency Shelter','Central Hyrule','20 Rupees',1,'Royal Hidden Passage','1 Temple Complete',NULL),
 (178,0,'Adventure','Zelda''s Golden Horse','Harlow',NULL,'-1641, 2582, 0233','Snowfield Stable','Tabantha Tundra','Zelda''s Golden Horse, Royal Bridle, Royal Saddle',2,NULL,NULL,'Potential Princess Sightings!'),
 (179,0,'Adventure','Legend of the Great Sky Island','Steward Construct',NULL,'0453, -0802, 1540','Great Sky Island','Hyrule Field','Zonai Fabric',1,NULL,'2 Temples Completed
Restoring the Zora Armor',NULL),
 (180,0,'Side','A Bottled Cry for Help','Message in a Bottle',NULL,'3945, -2509, 0000','Hateno Beach','East Necluda','100 Rupees',1,'Mapla Point Cave',NULL,NULL),
 (181,0,'Side','A Crabulous Deal','Cleff',NULL,'3323, 0492, 0139','Zora''s Domain','Lanayru','Sapphire',1,NULL,'Water Temple',NULL),
 (182,2,'Side','A New Champion''s Tunic','Zelda''s Diary','Examine Zelda''s Diary','3306, -2297, 0112','Hateno Village','East Necluda','Champion''s Leathers',1,'Zelda''s Secret Well
Hyrule Castle
Sanctum',NULL,NULL),
 (183,0,'Side','A Picture for Dueling Peaks Stable','Tasseren',NULL,'1757, -1924, 0010','Dueling Peaks Stable','West Necluda','Pony Point, Hasty Apple Pie',1,NULL,NULL,NULL),
 (184,0,'Side','A Picture for East Akkala Stable','Rudi',NULL,'4230, 2746, 0126','East Akkala Stable','Akkala','Pony Point, Meat and Rice Bowl',1,NULL,NULL,NULL),
 (185,1,'Side','A Picture for Foothill Stable','Ozunda',NULL,'2610, 1141, 0148','Foothill Stable','Eldin Canyon','Pony Point, Fireproof Elixir',1,NULL,NULL,NULL),
 (186,0,'Side','A Picture for Highland Stable','Padok',NULL,'0526, -3448, 0047','Highland Stable','Faron','Pony Point, Energizing Honey Crepe',1,NULL,NULL,NULL),
 (187,0,'Side','A Picture for Lakeside Stable','Anly',NULL,'1552, -3534, 0061','Lakeside Stable','Faron','Pony Point, Tough Tomato Seafood Soup',1,NULL,NULL,NULL),
 (188,0,'Side','A Picture for New Serenne Stable','Sprinn',NULL,'-1358, 0727, 0086','New Serenne Stable','Hyrule Ridge','Pony Point, Bright Tomato Mushroom Stew',1,NULL,NULL,NULL),
 (189,0,'Side','A Picture for Outskirt Stable','Embry',NULL,'-1445, -1268, 0032','Outskirt Stable','Central Hyrule','Pony Point, Egg Tart',1,NULL,NULL,NULL),
 (190,0,'Side','A Picture for Riverside Stable','Ember',NULL,'0336, -1092, 0010','Riverside Stable','Central Hyrule','Pony Point, Energizing Crab Stir-Fry',1,NULL,NULL,NULL),
 (191,0,'Side','A Picture for Snowfield Stable','Varke',NULL,'-1651, 2570, 0234','Snowfield Stable','Hebra Tabantha Tundra','Pony Point, Spicy Meat Stew',1,NULL,NULL,NULL),
 (192,0,'Side','A Picture for South Akkala Stable','Dmitri',NULL,'3146, 1690, 0201','South Akkala Stable','Akkala','Pony Point, Prime Meat Stew',1,NULL,NULL,NULL),
 (193,0,'Side','A Picture for Tabantha Bridge Stable','Dabi',NULL,'-2927, 0547, 0169','Tabantha Bridge Stable','Hyrule Ridge','Pony Point, Hasty Elixir',1,NULL,NULL,NULL),
 (194,0,'Side','A Picture for the Closed Stable I','Piaffe','Talk to Piaffe inside the Gerudo Canyon Stable.','-2809, -2219, 0029','Gerudo Canyon Stable','Gerudo Canyon','Pony Point, Chilly Mushroom Risotto',1,NULL,'Piaffe, Packed Away',NULL),
 (195,0,'Side','A Picture for the Closed Stable II','Piaffe','Talk to Piaffe inside the Gerudo Canyon Stable.','-2809, -2219, 0029','Gerudo Canyon Stable','Gerudo Canyon','Pony Point, Spicy Mushroom Risotto',1,NULL,'Piaffe, Packed Away',NULL),
 (196,0,'Side','A Picture for Wetland Stable','Lawdon',NULL,'0888, -0169, 0026','Wetland Stable','West Necluda','Pony Point, Electro Elixir',1,NULL,NULL,NULL),
 (197,0,'Side','A Picture for Woodland Stable','Kish',NULL,'1064, 1138, 0022','Woodland Stable','Great Hyrule Forest','Pony Point, Hasty Vegetable Curry',1,NULL,NULL,NULL),
 (198,2,'Side','A Token of Friendship','Yona','Talk to Yona in Zora''s Domain','3307, 0488, 0150','Zora''s Domain','Lanayru','Zora greaves',1,'Ancient Zora Waterworks
East Reservoir Lake','Water Temple',NULL),
 (199,2,'Side','A Trip through History','Bugut','Talk to Bugut in Kakariko Village','1843, -0970, 0115','Kakariko Village','West Necluda','3 Thunderwing Butterflies',1,NULL,NULL,NULL),
 (200,0,'Side','A Way to Trade, Washed Away','Garini',NULL,'2955, -3492, 0001','Lurelin Village','East Necluda','Star Fragment, General Store items free for Link',1,NULL,'Lurelin Village Restoration Project
Village Attacked by Pirates',NULL),
 (201,0,'Side','A Wife Wafted Away','Fronk',NULL,'3290, 0441, 0139','Zora''s Domain','Lanayru','Hearty Fish Skewer',1,'Great Zora Bridge
Wellspring Island','Water Temple',NULL),
 (202,2,'Side','Amber Dealer','Ramella','Talk to Ramella in Goron City, she will ask you to sell her 10 Amber for 200 Rupees - higher than market price. After selling 10 Amber, she will ask for 10 Topaz for 1,000 Rupees.','1661, 2466, 0385','Goron City','Eldin Canyon','10 Amber -> 200 Rupees
10 Topaz -> 1000 Rupees
10 Rubies -> 1300 Rupees
10 Sapphires -> 1700 Rupees
10 Diamonds -> 5500 Rupees',1,NULL,'Fire Temple Complete',NULL),
 (203,0,'Side','An Uninvited Guest','Ami','Speak with Ami in Wetland Stable','0865, -0171, 0025','Wetland Stable','West Necluda','2 Pony Points',1,'Wetland Stable South Well',NULL,NULL),
 (204,0,'Side','Ancient Blades Below','Mining Construct',NULL,'1334, -3366, -0737','Spirit Temple','Faron Depths','Ancient Blade',1,NULL,'The Fifth Sage',NULL),
 (205,0,'Side','Cash In on Ripened Flint','Gomo',NULL,'1750, 1536, 0278','Bedrock Bistro','Eldin','1,000 Rupees',1,NULL,'Meat for Meat',NULL),
 (206,2,'Side','Cave Mushrooms That Glow','Nat','Nat and Mehgan stand outside Brightcap Cave, give them 10 Brightcaps.','-2990, 1654, 0199','Brightcap Cave','Tabantha Frontier','Spicy Tomato Mushroom Stew',1,NULL,NULL,NULL),
 (207,2,'Side','Codgers'' Quarrel','Trissa','Defeat the monsters at the Southern Ring Ruin','1791, -1030, 0115','Kakariko Village','West Necluda','Endura Carrot, Other groceries restocked at High Spirits Produce',1,NULL,NULL,NULL),
 (208,0,'Side','Cold-Endurance Contest!','Rahdo','Talk to Rahdo on top of Mount Granajh, he will charge you 50 Ruppees, and challenge you to stand from sunset to sunrise on a pillar without cold clothes without dying.','-1380, -3363, 0469','Mount Granajh','Gerudo Canyon','100 Rupees',1,NULL,NULL,NULL),
 (209,0,'Side','Crossing the Cold Pool','Verla','Speak With Verla Outside of Talonto Peak Cave','-3217, 2456, 0347','Talonto Peak Cave','Hebra Mountains','50 Rupees',1,NULL,NULL,NULL),
 (210,0,'Side','Dad''s Blue Shirt','Zuta',NULL,'2892, -3435, 0000','Lurelin Village','East Necluda','Island Lobster Shirt',1,NULL,'Lurelin Village Restoration Project',NULL),
 (211,0,'Side','Dalia''s Game','Dalia',NULL,'-3815, -2873, 0043','Gerudo Town','Gerudo Desert','Orb',1,NULL,'Lightning Temple',NULL),
 (212,2,'Side','Dantz''s Prize Cows','Dantz','Speak With Dantz','3626, -2075, 0178','Hateno Village''s Lake Sumac','East Necluda','Fresh Milk',1,NULL,NULL,NULL),
 (213,0,'Side','Decorate with Passion','Boraa',NULL,'3226, -2518, 0023','Kara Kara Bazaar','Gerudo Desert','Electric Keese Eye',1,NULL,NULL,'Riju of Gerudo Town'),
 (214,0,'Side','Disaster in Gerudo Canyon','Qunice',NULL,'-1661, -2014, -0015','Gerudo Canyon Pass','Gerudo Canyon','Bomb Flower x10',1,'Stalry Plateau Cave
Koukot Plateau',NULL,NULL),
 (215,0,'Side','Eldin''s Colossal Fossil','Loone','Place the fossil''s eye into the eye socket','4339, 2816, 0142','Northeast of East Akkala Stable','Akkala','50 Rupees',1,'Eldin Great Skeleton',NULL,NULL),
 (216,0,'Side','Feathered Fugitives','Teli',NULL,'0368, -1103, 0009','Riverside Stable','Central Hyrule','100 Rupees',1,NULL,'Gourmets Gone Missing',NULL),
 (217,0,'Side','Fell into a Well!','Dillie',NULL,'0782, 0004, 0031','Rebonae Bridge Well','Central Hyrule','50 Rupees',1,'Rebonae Bridge',NULL,NULL),
 (218,2,'Side','Fish for Fletching','Bedoli','Give Bedoli 3 Glowing Cave fish.','-3656, 1762, 0214','Rito Village','Tabantha Frontier','Arrows x10',1,NULL,'Wind Temple Complete',NULL),
 (219,2,'Side','Follow the Cuccos','Trissa','Talk to Trissa After They Restock','1790, -1030, 0115','Kakariko Village','West Necluda','Eggs Restocked at High Spirits Produce',1,NULL,'Codgers'' Quarrel',NULL),
 (220,0,'Side','Genli''s Home Cooking','Genli','Speak to Genli in the General Store in Rito Village','-3642, 1820, 0184','Rito Village','Tabantha Frontier','Biting Simmered Meat',1,NULL,'Wind Temple Complete',NULL),
 (221,0,'Side','Gerudo''s Colossal Fossil','Loone','Speak with Loone, attach the body and tail to the small skull','-4876, -3770, -0057','Gerudo Great Skeleton','Gerudo Desert','50 Rupees',1,NULL,'Hebra''s Colossal Fossil
Eldin''s Colossal Fossil',NULL),
 (222,0,'Side','Gleeok Guts','Malena',NULL,'-2727, -2336, 0062','South of Gerudo Canyon Stable','Gerudo Canyon','300 Rupees',1,NULL,NULL,NULL),
 (223,2,'Side','Gloom-Borne Illness','Lasli','Speak with Lasli in Kakariko Village','1908, -0999, 0127','Kakariko Village','West Necluda','Reduced Prices at clothing store Enchanted',1,NULL,NULL,NULL),
 (224,0,'Side','Glory of the Zora','Dento',NULL,'3336, 0490, 0140','Zora''s Domain','Lanayru','Lightscale Trident',1,NULL,'Water Temple',NULL),
 (225,0,'Side','Goddess Statue of Courage','Goddess Statue',NULL,'0875, -2362, 0017','Spring of Courage','Faron','Topaz',1,'The Forgotten Temple',NULL,NULL),
 (226,0,'Side','Goddess Statue of Power','Goddess Statue',NULL,'3758, 2676, 0003','Spring of Power','Akkala','Ruby',1,'The Forgotten Temple',NULL,NULL),
 (227,0,'Side','Goddess Statue of Wisdom','Goddess Statue',NULL,'3914, -1329, 0467','Spring of Wisdom','Mount Lanayru','Sapphire',1,'The Forgotten Temple',NULL,NULL),
 (228,0,'Side','Heat-Endurance Contest!','Rahdo','Talk to Rahdo on top of Mount Granajh, he will charge you 150 Ruppees, and challenge you to stand from sunrise to sunset on a pillar without heat clothes without dying.','-1380, -3363, 0469','Mount Granajh','Gerudo Canyon','300 Rupees',1,NULL,'Cold-Endurance Contest!',NULL),
 (229,0,'Side','Hebra''s Colossal Fossil','Loone','Place the fin and spine piece back into place','-3882, 3691, 0223','Hebra North Summit','Hebra Mountains','50 Rupees',1,'Hebra Great Skeleton','Eldin''s Colossal Fossil',NULL),
 (230,2,'Side','Home on Arrange','Rhondson','Speak with Rhondson in Tarrey Town to build your dream home.','3933, 1586, 0129','Tarrey Town','Akkala','Hudson Construction Fabric
Ability to Build Link''s Home',1,NULL,'Mattison''s Independence',NULL),
 (231,0,'Side','Homegrown in Hateno','Mayor Reede','Talk to Reede After Completing The Mayoral Election','3298, -2123, 0109','Hateno Village','East Necluda','Sun Pumpkin x10',1,NULL,'The Mayoral Election',NULL),
 (232,0,'Side','Horse-Drawn Dreams','Zumi','Speak With Zumi in New Serenne Stable','-1333, 0723, 0085','New Serenne Stable','Hyrule Ridge','100 Rupees',1,NULL,NULL,NULL),
 (233,0,'Side','Kaneli''s Flight Training','Kaneli','Speak with Kaneli at the flight range','-3794, 2317, 0161','Flight Range','Herba Mountains','50 Rupees, Flight Training time trials',1,NULL,'Wind Temple Complete',NULL),
 (234,0,'Side','Legacy of the Rito','Teba',NULL,'-3609, 1824, 0218','Rito Village','Tabantha Frontier','Great Eagle Bow',1,NULL,'Wind Temple Complete',NULL),
 (235,0,'Side','Lost in the Dunes','Benja',NULL,'-3272, -2582, 0023','Kara Kara Bazaar','Gerudo Desert','Orb',1,'Oasis Source
Kara Kara Bazaar Well',NULL,'Riju of Gerudo Town'),
 (236,0,'Side','Lurelin Resort Project','Rozel',NULL,'2859, -3518, 0000','Lurelin Village','East Necluda','Lurelin Water Rally',1,NULL,'Lurelin Village Restoration Project',NULL),
 (237,0,'Side','Manny''s Beloved','Manny',NULL,'3373, -2131, 0120','Hateno Village','East Necluda','10 x Rushrooms',1,NULL,NULL,NULL),
 (238,2,'Side','Master the Vehicle Prototype','Fernison','Speak to Fernison, Shabonne and Tali at the Tarrey Town Construction Site.','3752, 1678, 0092','Hudson Construction Site','Akkala','100 Rupees, Stable Sleepover Ticket',1,NULL,NULL,NULL),
 (240,2,'Side','Meat for Meat','Mezer',NULL,'1754, 1548, 0278','Bedrock Bistro','Eldin','Large Zonai Charge',1,'Bedrock Bistro
West Restaurant Cave',NULL,NULL),
 (241,1,'Side','Mine-Cart Land: Death Mountain','Kabetta','Ride the minecart and hit the targets with arrows.','2363, 2596, 0827','Death Mountain','Eldin','Goron Fabric',1,'Southern Mine','Fire Temple
Mine-Cart Land: Quickshot Course',NULL),
 (242,2,'Side','Mine-Cart Land: Open for Business!','Bayge','Ride the minecart and hit the targets with arrows.','1832, 2075, 0321','Southern Mine','Eldin','20 Rupees',1,'Southern Mine','Fire Temple Complete',NULL),
 (243,2,'Side','Mine-Cart Land: Quickshot Course','Heehl','Ride the minecart and hit the targets with arrows.','1832, 2075, 0321','Southern Mine','Eldin','50 Rupees',1,'Southern Mine','Fire Temple
Mine-Cart Land: Open for Business!',NULL),
 (244,0,'Side','Mired in Muck','Bazz','Talk to Bazz in Upland Zorana Skyview Tower','2846, 0585, 0375','Zora''s Domain','Lanayru','Zora Spear',1,NULL,NULL,NULL),
 (245,0,'Side','Misko''s Cave of Chests','Domidak','Talk to Domidak and Prissen Outside of Cephla Lake Cave','2606, 1325, 0150','Cephla Lake','Eldin Canyon','Ember Trousers',1,'Cephla Lake Cave',NULL,NULL),
 (246,0,'Side','Misko''s Treasure of Awakening I','Misko''s Letter','Retrieve the Misko''s Treasure in Goronbi Cave, read the revealed pedestal to start the quest.','1381, 2260, 0294','Goronbi River Cave','Eldin','Tunic of Awakening',1,'Ancient Columns Cave',NULL,NULL),
 (247,0,'Side','Misko''s Treasure of Awakening II','Misko''s Letter',NULL,'-3528, 0410, 0241','Ancient Columns Cave','Tabantha Frontier','Trousers of Awakening',1,'Coliseum Ruins Cave','Misko''s Treasure of Awakening I',NULL),
 (248,0,'Side','Misko''s Treasure of Awakening III','Misko''s Letter','Find Misko''s Letter in the Coliseum Ruins Cave.','-1160, -1271, 0034','Coliseum Ruins Cave','Central Hyrule','Mask of Awakening',1,'Thundra Plateau
Thundra Plateau Cave','Misko''s Treasure of Awakening II',NULL),
 (249,0,'Side','Misko''s Treasure: Heroines Manuscript','Domidak','Speak with Domidak and Prissen Outside of Cephla Lake Cave','2603, 1319, 0150','Cephla Lake','Eldin Canyon','Tingle''s Hood',1,'Statue of the Eighth Heroine Cave','Misko''s Cave of Chests',NULL),
 (250,0,'Side','Misko''s Treasure: Pirate Manuscript','Domidak','Speak with Domidak and Prissen Outside of Cephla Lake Cave','2603, 1319, 0150','Cephla Lake','Eldin Canyon','Tingle''s Tights',1,'Cape Cales
Cape Cales Cliffbase Cave','Misko''s Cave of Chests',NULL),
 (251,0,'Side','Misko''s Treasure: The Fierce Deity','Misko''s Letter',NULL,'2582, 1426, 0134','Cephla Lake Cave','Eldin Canyon','Fierce Deity Sword
Fierce Deity Armor
Fierce Deity Mask
Fierce Deity Boots',1,'Akkala Citadel Ruins Summit Cave
Akkala Citadel Ruins
Skull Lake Cave
Skull Lake
Ancient Tree Stump Cave
Ancient Tree Stump','Misko''s Cave of Chests',NULL),
 (252,0,'Side','Misko''s Treasure: Twins Manuscript','Domidak','Speak with Domidak and Prissen Outside of Cephla Lake Cave','2603, 1319, 0150','Cephla Lake','Eldin Canyon','Tingle''s Shirt',1,'Dueling Peaks
Dueling Peaks North Cave
Dueling Peaks South Cave','Misko''s Cave of Chests',NULL),
 (253,0,'Side','Molli the Fletcher''s Quest','Molli','Speak With Molli in Her Home in Rito Village','-3616, 1793, 0214','Rito Village','Tabantha Frontier','Arrows x10',1,NULL,'Wind Temple Complete',NULL),
 (254,2,'Side','Moon-Gazing Gorons','Tray',NULL,'1668, 2433, 0383','Goron City','Eldin','100 Rupees',1,'Lake Ferona Cave','Fire Temple Complete',NULL),
 (255,0,'Side','One-Hit Wonder!','Parcy','Talk to Parcy in South Akkala Stable','3085, 1672, 0201','South Akkala Stable','Akkala','Various Gemstones',1,NULL,NULL,NULL),
 (256,0,'Side','Open the Door','Jogo','defeat the monsters around the cabin','-2684, 1669, 0258','Tabantha Hills','Hebra','Spicy Elixir',1,NULL,NULL,NULL),
 (257,2,'Side','Ousting The Giants','Kampo',NULL,'1563, -3530, 0060','Lakeside Stable','Faron','Mighty Fried Bananas',1,'Corta Lake Cave
Rodai Lakefront Tunnel
Calora Lake Cave',NULL,NULL),
 (258,0,'Side','Out of the Inn','Dai','Wake the inkeeper sleeping in the Ring Ruin by bringing him a Hearty Truffle','1836, -1022, 0116','Kakariko Village','West Necluda','Sticky Elixir, Restores Use of Inn',1,NULL,NULL,NULL),
 (259,0,'Side','Photographing a Chuchu','Sayge','Speak to Sayge in the Dye Shop and bring him a picture of a Chuchu','3409, -2149, 0121','Hateno Village','East Necluda','Paraglider Fabric, Ability to change paraglider fabric',1,NULL,'1 Tower Complete','Camera Work in the Depths'),
 (260,0,'Side','Piaffe, Packed Away','Piaffe','Speak to Piaffe in Gerudo Canyon Stable','-2802, -2226, 0029','Gerudo Canyon Stable','Gerudo Canyon','1 Pony Point',1,NULL,NULL,NULL),
 (261,0,'Side','Pride of the Gerudo','Isha',NULL,'-3827, -2885, 0043','Gerudo Town','Gerudo Desert','Scimitar of the Seven
Daybreaker',1,NULL,'Lightning Temple
The Missing Owner',NULL),
 (262,0,'Side','Rattled Ralera','Ralera',NULL,'2845, -3462, 0004','Lurelin Village','East Necluda','Lurelin Village Fabric',1,'Goron General Store
Goron City','Lurelin Village Restoration Project',NULL),
 (263,0,'Side','Rock Roast or Dust','Cooke',NULL,'1759, 1547, 0279','Bedrock Bistro','Eldin','Seared Gourmet Steak',1,'West Restaurant Cave','Fire Temple Complete
Meat for Meat',NULL),
 (264,2,'Side','Secret Treasure Under the Great Fish','Sidon',NULL,'3340, 0543, 0163','Zora''s Domain','Lanayru','Vah Ruta Divine Helm',1,'Great Zora Bridge
Cave Under Zora''s Domain
Chasm Under Zora''s Domain','Water Temple',NULL),
 (265,0,'Side','Secrets Within','Pulcho','Speak to Pulcho about the Device Despenser','3801, 1569, 0091','Hudson Construction Site','Akkala','Sundelion',1,NULL,NULL,NULL),
 (266,0,'Side','Seeking the Pirate Hideout','Sesami',NULL,'4515, -3500, 0002','Eventide Island','East Necluda','Blue-Maned Lynel Saber Horn',1,'Eventide Island Cave',NULL,NULL),
 (267,0,'Side','Simmerstone Springs','Kima',NULL,'Before Completing the Sage of Fire: 2181, 2085, 0387
After Completing the Sage of Fire: 1705, 2422, 0392','Goron City','Eldin','100 Rupees, Hard-Boiled Egg x3',1,'Goron Hot Springs
Gorko Tunnel',NULL,NULL),
 (268,0,'Side','Soul of the Gorons','Fugo','Bring a Cobble Crusher and diamonds (?) to get a Boulder Breaker','1687, 2494, 0396','Goron City','Eldin','Boulder Breaker',1,NULL,'Fire Temple',NULL),
 (269,0,'Side','Spotting Spot','Lester',NULL,'-0251, 0051, 0019','Lookout Landing','Central Hyrule','50 Rupees, Swift Carrot, Spot the Horse',1,NULL,'2 Temples Complete
The Incomplete Stable',NULL),
 (270,0,'Side','Strongest in the World','Chabi',NULL,'4199, 2766, 0127','East Akkala Stable','Akkala','Lynel Horn -> 50 Rupees
Blue-Maned Lynel Horn -> 100 Rupees
White-Maned or Silver Lynel Horn -> 300 Rupees',1,NULL,NULL,NULL),
 (271,0,'Side','Supply-Eyeing Fliers','Huck',NULL,'-2175, 2028, 0363','Tabantha Hills','Hebra','50 Rupees',1,NULL,'Wind Temple Complete',NULL),
 (272,0,'Side','Teach Me a Lesson I','Symin',NULL,'3363, -1968, 0129','Hateno School','East Necluda','10 x Hylian Rice',1,'Kakariko Village',NULL,'Camera Work in the Depths'),
 (273,0,'Side','Teach Me a Lesson II','Symin',NULL,'3363, -1968, 0129','Hateno School','East Necluda','Access to the school''s field for planting',1,'Goron General Store
Goron City','Teach Me a Lesson I','Camera Work in the Depths'),
 (274,0,'Side','The Abandoned Laborer','Mota','Mota is stranded in a cave. Build a cart with a rocket attached to jump the broken tracks.','2347, 2681, 0514','Death Mountain West Tunnel','Eldin','Large Zonai Charge',1,NULL,NULL,NULL),
 (275,0,'Side','The Ancient City Gorondia?','Dugby',NULL,'1629, 2439, 0384','Goron City','Eldin','Large Zonai Charge',1,NULL,'Fire Temple Complete
The Ancient City Gorondia!',NULL),
 (276,2,'Side','The Blocked Cave','Mazli','Speak with Mazli outside a blocked cave entrance','-3580, 2477, 0228','Rospro Pass Cave','Hebra Mountains','20 Rupees',1,NULL,NULL,NULL),
 (277,0,'Side','The Blue Stone','Ledo',NULL,'3597, 0339, 0211','East Resevoir Lake','Lanayru','Zora Fabric',1,'Reservoir Lakefront Cavern','Water Temple',NULL),
 (278,0,'Side','The Captured Tent','Nat',NULL,'-1662, 2542, 0233','Snowfield Stable','Hebra Tabantha Tundra','Spicy Steamed Mushrooms',1,NULL,'Cave Mushrooms That Glow',NULL),
 (279,0,'Side','The Duchess Who Disappeared','Russ',NULL,'-3517, 3102, 0316','Biron Snowshelf','Hebra Mountains','Strong Zonaite Shield, Shield Surfing time trials',1,'East Biron Snowshelf Cave','Wind Temple Complete',NULL),
 (280,0,'Side','The Fort at Ja''Abu Ridge','Gaddison',NULL,'3449, 0487, 0155','Zora''s Domain','Lanayru','100 Rupees',1,'Fort East of East Reservoir Lake','Water Temple',NULL),
 (281,0,'Side','The Gathering Pirates','Aya','Speak to Aya at the South Akkala Stable','4235, 2737, 0125','East Akkala Stable','Akkala','2 Pony Points
Endura Carrot',1,'North Akkala Beach',NULL,NULL),
 (282,0,'Side','The Great Tumbleweed Purge','Barles',NULL,'-1010, -3581, 0219','Daval Peak','Gerudo Canyon','Royal Shield',1,NULL,NULL,NULL),
 (283,0,'Side','The Heroines'' Secret','Rotana','Talk to Rotana','-3884, -2970, 0033','Gerudo Town','Gerudo Desert','100 Rupees',1,NULL,NULL,NULL),
 (284,0,'Side','The Hidden Treasure at Lizard Lakes','Bludo','Talk to Bludo after completing the Fire Temple.','1646, 2438, 0381','Goron City','Eldin','Vah Rudania Divine Helm',1,'Lizard''s Burrow','Fire Temple Complete',NULL),
 (285,0,'Side','The Horse Guard''s Request','Toffa','Speak with Toffa at Outskirt Stable','-1449, -1251, 0032','Outskirt Stable','Central Hyrule','1 Pony Point, 50 Rupees
1 Pony Point, 100 Rupees',1,NULL,NULL,NULL),
 (286,0,'Side','The Iceless Icehouse','Anche',NULL,'-3754, -2277, 0033','Northern Icehouse','Gerudo Highlands','50 Rupees',1,NULL,NULL,NULL),
 (287,2,'Side','The Incomplete Stable','Karson','Talk to Karson in Lookout Landing after completing a Temple.','-0245, 0060, 0019','Lookout Landing','Central Hyrule','Mini Stable Unlocked',1,NULL,'1 Temple Complete',NULL),
 (288,2,'Side','The Lomei Labyrinth Island Prophecy','Mysterious Voice','Activate the Lomei Labyrinth Island Terminal','4655, 3682, 0129','Lomei Labyrinth Island','Akkala','Evil Spirit Armor',1,'Lomei Sky Labyrinth
Lomei Labyrinth Chasm
Lomei Depths Labyrinth',NULL,NULL),
 (289,0,'Side','The Missing Owner','Cara','Speak With Cara in Gerudo Town','-3871, -2960, 0033','Gerudo Town','Gerudo Desert','Diamond',1,'Toruma Dunes',NULL,NULL),
 (290,0,'Side','The Moonlit Princess','Seggin',NULL,'3274, 0543, 0155','Zora''s Domain','Lanayru','Zora Sword',1,'Mipha Court','Water Temple','Camera Work in the Depths'),
 (291,0,'Side','The Mother Goddess Statue','Goddess Statue',NULL,'-1056, 2689, -0084','Forgotten Temple','Hyrule Ridge','White Sword of the Sky',1,'Spring of Wisdom
Spring of Courage
Spring of Power','Goddess Statue of Wisdom
Goddess Statue of Courage
Goddess Statue of Power',NULL),
 (292,0,'Side','The Mysterious Eighth','Rotana',NULL,'-3828, -2970, 0030','Gerudo Town','Gerudo Desert','Diamond, Hydromelon x6',1,'Kara Kara Bazaar
North Gerudo Ruins
Gerudo Sanctuary
Statue of the Eighth Heroine Room','Lightning Temple
The Heroines Secret
Dalia''s Game
Lost in the Dunes',NULL),
 (293,0,'Side','The Never-Ending Lecture','Chroma','Talk to Chroma in Zora''s Domain','3322, 0548, 0163','Zora''s Domain','Lanayru','Zora helm',1,'Floating Scales Island','Water Temple',NULL),
 (294,0,'Side','The North Lomei Prophecy','Mysterious Voice','Activate the North Lomei Labyrinth Terminal','-0799, 3534, 0235','North Lomei Labyrinth','Hebra','Evil Spirit Greaves',1,'North Lomei Castle Top Floor
North Lomei Chasm
North Lomei Depths Labyrinth',NULL,NULL),
 (295,0,'Side','The Rito Rope Bridge','Gesane','Speak with Gesane in front of the broken Rito Bridge','-3294, 1803, 0121','Lucky Clover Gazette','Tabantha Frontier','100 Rupees',1,NULL,'Wind Temple Complete
The Incomplete Stable',NULL),
 (296,0,'Side','The Secret Room','Oaki',NULL,'0413, 2177, 0179','Korok Forest','Great Hyrule Forest','Korok Fabric',1,NULL,NULL,NULL),
 (297,0,'Side','The Shrine Explorer','Rauru',NULL,NULL,'Shrine of Light',NULL,'Ancient Hero''s Aspect',1,'Temple of Time',NULL,NULL),
 (298,0,'Side','The South Lomei Prophecy','Mysterious Voice','Activate the South Lomei Labyrinth Terminal','-1794, -3440, 0046','South Lomei Labyrinth','Gerudo','Evil Spirit Mask',1,'South Lomei Labyrinth
South Lomei Chasm
South Lomei Depths Labyrinth',NULL,NULL),
 (299,0,'Side','The Tarrey Town Race Is On!','Fernison',NULL,'3754, 1677, 0092','Hudson Construction Site','Akkala','Zonai Charge x3',1,NULL,'Master the Vehicle Prototype',NULL),
 (300,0,'Side','The Treasure Hunters','Domidak',NULL,'0600, 1284, 0047','Rauru Hillside','Great Hyrule Forest','x3 Bomb Flowers',1,NULL,NULL,NULL),
 (301,0,'Side','The Ultimate Dish?','Moza','Talk to Moza in Rikoka Hills Well','1711, -0653, 0013','Rikoka Hills Well','Lanayru','Repair Ruined Meals',1,NULL,NULL,NULL),
 (302,0,'Side','To the Ruins!','Pokki',NULL,'-3768, -2927, 0043','Gerudo Town','Gerudo Desert','100 Rupees',1,'East Gerudo Ruins','Lightning Temple',NULL),
 (303,2,'Side','Today''s Menu','Burmano','Found in the Emergency Shelter, give Burmano an apple.','-0266, 0098, 0008','Emergency Shelter in Lookout Landing','Central Hyrule','Fruit and Mushroom Mix',1,NULL,NULL,NULL),
 (304,0,'Side','Treasure of the Gerudo Desert','Riju',NULL,'-3888, -2967, 0051','Gerudo Town','Gerudo Desert','Vah Naboris Divine Helm',1,'West Gerudo Underground Ruins','Lightning Temple',NULL),
 (305,0,'Side','Treasure of the Secret Springs','Tulin',NULL,'-3610, 1822, 0218','Rito Village','Tabantha Frontier','Vah Medoh Divine Helm',1,'North Biron Snowshelf Cave','Wind Temple Complete',NULL),
 (306,0,'Side','True Treasure','Kodah','Speak with Sasan in Tarm Point cave or Kodah in Zora''s Domain','3295, 0512, 0140','Zora''s Domain','Lanayru','x2 Opal',1,'Tarm Point
Tarm Point Cave','Water Temple',NULL),
 (307,0,'Side','Uma''s Garden','Uma',NULL,'3333, -2035, 0117','Hateno Village','East Necluda','Ability to grow vegetables',1,NULL,'Teach Me a Lesson II',NULL),
 (308,0,'Side','Unknown','Gralens',NULL,'-0252, 0086, 0008','Lookout Landing','Central Hyrule','Diamond',1,'Lake Hylia
Bridge of Hylia','WANTED',NULL),
 (311,0,'Side','Village Attacked by Pirates','Garini',NULL,'-0209, 0081, 0019','Lookout Landing','Central Hyrule','Mighty Salt-Grilled Crab',1,NULL,'2 Temples Complete',NULL),
 (312,0,'Side','Walton''s Treasure Hunt','Walton',NULL,'0418, 2180, 0227','Korok Forest','Great Hyrule Forest','Forest Dweller''s Weapons',1,'The Great Deku Tree',NULL,NULL),
 (313,0,'Side','WANTED','Gralens',NULL,'-0252, 0086, 0008','Lookout Landing','Central Hyrule','300 Rupees',1,NULL,'','Crisis at Hyrule Castle
Bring Peace to'),
 (315,'','','','','','','','','',1,'','',NULL),
 (316,1,'Side','Where Are the Wells?','Fera','Speak to Fera in one of the stable wells.','X','South Akkala Stable Well','Akkala','10 Rupees per Well Location
All''s Well Trophy',1,'Aquame Lake Well
Bottomless Pond Well
Carok Bridge Well
Construction Site Well
Deya Village Ruins East Well
Deya Village Ruins North Well
Deya Village Ruins South Well
Deya Village Ruins Well
Dronoc''s Pass Well
Dueling Peaks Stable Well
East Akkala Stable Well
Elma Knolls Well
Foothill Stable Well
Gerudo Canyon Well
Goponga Village Ruins Well
Haran Lakefront Well
Hateno Village East Well
Hateno Village North Well
Hateno Village South Well
Hateno Village West Well
Highland Stable Well
Hills of Baumer Well
Hyrule Castle Town Ruins Well
Irch Plain Well
Kakariko Village Well
Kara Kara Bazaar Well
Lakeside Stable Well
Lanayru Wetlands Well
Lookout Landing Well
Lurelin Village Well
Mabe Village Ruins Well
Maritta Exchange Ruins Well
Moor Garrison Ruins Well
Mount Daphnes Well
Mount Gustaf Well
Mount Nabooru Well
New Serenne Stable Well
Outskirt Hill Well
Outskirt Stable Well
Popla Foothills North Well
Popla Foothills South Well
Rauru Settlement Ruins Well
Rebonae Bridge Well
Rikoka Hills Well
Riverside Stable Well
Rowan Plain Well
Shadow Hamlet Ruins Well
Snowfield Stable Well
South Akkala Stable Well
South Nabi Lake Well
Tabahl Woods Well
Tabantha Bridge Stable Well
Tabantha Village Ruins Well
Wetland Stable South Well
Wetland Stable Well
Woodland Stable Well
Zauz Island Well
Zelda''s Secret Well',NULL,NULL),
 (317,0,'Side','Whirly Swirly Things','Kula',NULL,'0420, 2132, 0143','Korok Forest','Great Hyrule Forest','5 Endura Carrots',1,'The Great Deku Tree
Lake Hylia',NULL,NULL),
 (318,0,'Side','Who Finds the Haven','Nat',NULL,'-4038, 2668, 0024','Sturnida Springs Cave','Hebra Tabantha Tundra','Mushrooms',1,NULL,'The Captured Tent',NULL),
 (319,0,'Side','A Picture For...',NULL,NULL,NULL,NULL,NULL,'Diamond, Enduring Carrot Cake x5',1,'Dueling Peaks Stable
East Akkala Stable
Foothill Stable
Highland Stable
Lakeside Stable
New Serenne Stable
Outskirt Stable
Riverside Stable
Snowfield Stable
South Akkala Stable
Tabantha Bridge Stable
Gerudo Canyon Stable
Wetland Stable
Woodland Stable',NULL,NULL),
 (320,0,'Side','The Ancient City Gorondia!','Dugby',NULL,'1744, 2576, 0426','North of Goron City','Eldin','Zonai Charge',1,'Goron City',NULL,NULL),
 (321,0,'Side','WANTED: Hinox','Gralens','','1300, 0914, 0027','Lookout Landing','Central Hyrule','100 Rupees',2,NULL,NULL,NULL),
 (322,0,'Side','WANTED: Molduga','Gralens','','-2400, -3281, 0021','Lookout Landing','Central Hyrule','100 Rupees',2,NULL,NULL,NULL),
 (323,0,'Side','WANTED: Stone Talus','Gralens','','4046, 2977, 0149','Lookout Landing','Central Hyrule','100 Rupees',2,NULL,NULL,NULL),
 (324,0,'Side','Unknown Huge Silhouette','Gralens',NULL,'Lookout Landing','Central Hyrule','100 Rupees',NULL,2,NULL,NULL,NULL),
 (325,0,'Side','Unknown Sky Giant','Gralens',NULL,'Lookout Landing','Central Hyrule','100 Rupees',NULL,2,NULL,NULL,NULL),
 (326,0,'Side','Unknown Three-Headed Monster','Gralens',NULL,'Lookout Landing','Central Hyrule','100 Rupees',NULL,2,NULL,NULL,NULL);
COMMIT;
