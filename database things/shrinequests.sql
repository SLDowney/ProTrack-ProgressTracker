BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "shrinequests" (
	"shrinequ_done"	INTEGER DEFAULT 0,
	"shrinequ_name"	TEXT,
	"shrinequ_shrine"	TEXT,
	"shrinequ_location"	TEXT,
	"shrinequ_contact"	TEXT,
	PRIMARY KEY("shrinequ_name")
);
INSERT INTO "shrinequests" ("shrinequ_done","shrinequ_name","shrinequ_shrine","shrinequ_location","shrinequ_contact") VALUES (0,'A Pretty Stone and Five Golden Apples','Pupunke','Great Hyrule Forest','Damia'),
 (0,'Dyeing to Find It','Kurakat','Lanayru Great Spring','Steward Construct'),
 (0,'Keys Born of Water','Jochisiu','West Necluda','Steward Construct'),
 (0,'Legend of the Soaring Spear','Utojis','East Necluda','Tattered Notebook'),
 (0,'Maca’s Special Place','Ninjis','Great Hyrule Forest','Maca'),
 (0,'None Shall Pass?','Sakunbomar','Great Hyrule Forest','Zooki'),
 (0,'Ride the Giant Horse','Ishokin','Faron','Baddek'),
 (0,'Rock for Sale','Jochi-ihiga','Akkala - Tarrey Town','Hagie'),
 (0,'The Death Caldera Crystal','Momosik','Death Mountain','Mysterious Voice'),
 (0,'The East Hebra Sky Crystal','Tauninoud','East Hebra Sky Archipelago','Mysterious Voice'),
 (0,'The Gerudo Canyon Crystal','Rakakudaj','Gerudo Canyon','Mysterious Voice'),
 (0,'The Gisa Crater Crystal','Ikatak','Tabantha Frontier','Mysterious Voice'),
 (0,'The High Spring and the Light Rings','Zakusu','Mount Lanayru','Nazbi'),
 (0,'The Lake Hylia Crystal','En-oma','Lake Hylia','Mysterious Voice'),
 (0,'The Lake Intenoch Cave Crystal','Moshapin','Eldin Canyon','Mysterious Voice'),
 (0,'The Lanayru Road Crystal','O-ogim','East Necluda - Lanayru Promenade','Mysterious Voice'),
 (0,'The Necluda Sky Crystal','Kumamayn','Necluda Sky Archipelago','Mysterious Voice'),
 (0,'The North Hebra Mountains Crystal','Sisuran','Hebra','Mysterious Voice'),
 (0,'The North Hyrule Sky Crystal','Mayam','North Hyrule Sky Archipelago','Mysterious Voice'),
 (2,'The North Necluda Sky Crystal','Josiu','North Necluda Sky Archipelago','Mysterious Voice'),
 (0,'The Northwest Hebra Cave Crystal','Rutafu-um','Hebra','Mysterious Voice'),
 (0,'The Oakle’s Navel Cave Crystal','Tokiy','East Necluda','Mysterious Voice'),
 (0,'The Ralis Channel Crystal','Joniu','Lanayru Great Spring','Mysterious Voice'),
 (0,'The Satori Mountain Crystal','Usazum','Hyrule Ridge','Mysterious Voice'),
 (0,'The Sky Mine Crystal','Gikaku','Akkala Sky','Mysterious Voice'),
 (0,'The Sokkala Sky Crystal','Natak','Sokkala Sky Archipelago','Mysterious Voice'),
 (0,'The South Hyrule Sky Crystal','Jinodok','South Hyrule Sky Archipelago','Mysterious Voice'),
 (0,'The South Lanayru Sky Crystal','Mayanas','South Lanayru Sky Archipelago','Mysterious Voice'),
 (0,'The Tabantha Sky Crystal','Ganos','Tabantha Sky Archipelago','Mysterious Voice'),
 (1,'The West Necluda Sky Crystal','Ukoojisi','West Necluda Sky Archipelago','Mysterious Voice'),
 (0,'The White Bird’s Guidance','Wao-os','Rito Village','Laissa');
CREATE INDEX IF NOT EXISTS "shrinequ_idx" ON "shrinequests" (
	"shrinequ_shrine"
);
COMMIT;
