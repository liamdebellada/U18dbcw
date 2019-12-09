BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Trip` (
	`trip_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`destination_id`	INTEGER,
	`personCost`	TEXT,
	`startDate`	TEXT,
	`duration`	TEXT,
	`coach_id`	INTEGER,
	`driver_id`	INTEGER,
	FOREIGN KEY(`driver_id`) REFERENCES `Driver`(`driver_id`),
	FOREIGN KEY(`destination_id`) REFERENCES `Destination`(`destination_id`),
	FOREIGN KEY(`coach_id`) REFERENCES `Coach`(`coach_id`)
);

CREATE TABLE IF NOT EXISTS `Driver` (
	`driver_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`firstName`	TEXT,
	`secondName`	TEXT
);

CREATE TABLE IF NOT EXISTS `Destination` (
	`destination_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`destName`	TEXT,
	`hotelName`	TEXT
);

CREATE TABLE IF NOT EXISTS `Customer` (
	`customer_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`firstName`	TEXT,
	`surname`	TEXT,
	`AddressLine1`	TEXT,
	`AddressLine2`	TEXT,
	`Postcode`	TEXT,
	`phoneNum`	TEXT,
	`email`	TEXT,
	`specialNeed`	TEXT
);

CREATE TABLE IF NOT EXISTS `Coach` (
	`coach_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`registration`	TEXT,
	`seatNumber`	TEXT
);

CREATE TABLE IF NOT EXISTS `Booking` (
	`booking_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`customer_id`	INTEGER,
	`trip_id`	INTEGER,
	`seatNumber`	TEXT,
	`bookingDate`	TEXT,
	FOREIGN KEY(`trip_id`) REFERENCES `Trip`(`trip_id`),
	FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`customer_id`)
);


COMMIT;
