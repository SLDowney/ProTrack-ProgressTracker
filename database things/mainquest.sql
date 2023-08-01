CREATE TABLE "mainqu" (
	"mainqu_id"	INTEGER NOT NULL UNIQUE,
	"mainqu_done"	INTEGER NOT NULL DEFAULT 0,
	"mainqu_name"	TEXT,
	"mainqu_giver"	TEXT,
	"mainqu_location"	TEXT,
	"mainqu_region"	TEXT,
	"mainqu_coord"	TEXT,
	PRIMARY KEY("mainqu_id" AUTOINCREMENT)
);

BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "mainqu" (
	"mainqu_id"	INTEGER,
	"mainqu_done"	INTEGER,
	"mainqu_name"	TEXT,
	"mainqu_giver"	TEXT,
	"mainqu_location"	TEXT,
	"mainqu_region"	TEXT,
	"mainqu_coord"	TEXT
);
INSERT INTO "mainqu" ("mainqu_id","mainqu_done","mainqu_name","mainqu_giver","mainqu_location","mainqu_region","mainqu_coord") VALUES (1,0,'Prologue','-','Beneath Hyrule Castle','Central Hyrule','N/A'),
 (2,0,'Find Princess Zelda','Steward Construct','Garden of Time','Great Sky Island','0448, -1313, 1535'),
 (3,0,'The Closed Door','Rauru','Temple of Time','Great Sky Island','0452, -0859, 1450'),
 (4,0,'To the Kingdom of Hyrule','Zelda''s Voice','Temple of Time','Great Sky Island','0444, -0631, 1472'),
 (5,0,'Crisis at Hyrule Castle','Purah','Lookout Landing','Central Hyrule','-0254, 0153, 0026'),
 (6,0,'Regional Phenomena','Purah','Lookout Landing','Hyrule Field','-0252, 0153, 0026'),
 (7,0,'Camera Work in the Depths','Josha','Lookout Landing','Hyrule Field','-0252, 0146, 0020'),
 (8,0,'Impa and the Geoglyphs','Cado','New Serenne Stable','Hyrule Ridge','-1615, 0558, 0032'),
 (9,0,'Tulin of Rito Village','Teba','Rito Village','Tabantha Frontier','-3596, 1802, 0212'),
 (10,0,'A Mystery in the Depths','Josha','Lookout Landing','Hyrule Field','-0255, 0138, 0019'),
 (11,0,'Riju of Gerudo Town','Riju','Gerudo Town','Gerudo Desert','-3889, -2969, 0043'),
 (12,0,'Yunobo of Goron City','Yunobo','Goron City','Eldin Canyon','1649, 2447, 0381'),
 (13,0,'The Sludge-Covered Statue','???','Zora''s Domain','Lanayru Great Spring','3302, 0463, 0139'),
 (14,0,'Sidon of the Zora','Yona','Zora''s Domain','Lanayru Great Spring','3306, 0464, 0139'),
 (15,0,'The Broken Slate','Jiahto','Toto Lake','Lanayru Great Spring','3405, 0884, 0400'),
 (16,0,'Clues to the Sky','Jiahto','Toto Lake','Lanayru Great Spring','3404, 0877, 0399'),
 (17,0,'Restoring the Zora Armor','Yona','Zora''s Domain','Lanayru Great Spring','3845, 0568, 0485'),
 (18,0,'The Dragon''s Tears','Impa','New Serenne Stable','Hyrule Ridge','-1615, 0558, 0032'),
 (19,0,'Find the Fifth Sage','Purah','Lookout Landing','Hyrule Field','-0253, 0153, 0026'),
 (20,0,'Secret of the Ring Ruins','Tauro','Kakariko Village','West Necluda','1814, -0951, 0113'),
 (21,0,'Guidance from Ages Past','Zonai Relic','Dragonhead Island','Faron Grasslands','1363, -3263, 0431'),
 (22,0,'Trail of the Master Sword','Mineru','Spirit Temple','Faron Grasslands Depths','1367, -3309, -0737'),
 (23,0,'Recovering the Hero''s Sword','Great Deku Tree','Korok Forest','Great Hyrule Forest','0429, 2146, 0162'),
 (24,0,'Destroy Ganondorf','Purah','Lookout Landing','Central Hyrule','-0252, 0155, 0026');
COMMIT;
