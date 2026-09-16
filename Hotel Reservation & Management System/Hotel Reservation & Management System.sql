-- Hotel Reservation & Management System --

-- DataBase --
CREATE DATABASE hotel_management_db;

-- Tables --
USE hotel_management_db;

-- Table 1 --
CREATE TABLE guests(
id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(25),
last_name VARCHAR(25),
phone VARCHAR(15),
email VARCHAR(25)
);

-- Table 2 --
CREATE TABLE room_types(
id INT PRIMARY KEY AUTO_INCREMENT,
type_name VARCHAR(15),
price_per_night INT NOT NULL,
capacity INT NOT NULL
);

-- Table 3 --
CREATE TABLE rooms(
id INT PRIMARY KEY AUTO_INCREMENT,
room_number INT NOT NULL,
room_type_id INT NOT NULL,
status CHAR(15),

FOREIGN KEY (room_type_id)
REFERENCES room_types(id)
);

-- Table 4 --
CREATE TABLE reservations(
id INT PRIMARY KEY AUTO_INCREMENT,
guest_id INT NOT NULL,
room_id INT NOT NULL,
check_in DATE NOT NULL,
check_out DATE NOT NULL,
status CHAR(15),

FOREIGN KEY (room_id)
REFERENCES rooms(id),

FOREIGN KEY (room_id)
REFERENCES rooms(id)
);

-- Table 5 --
CREATE TABLE payments(
id INT PRIMARY KEY AUTO_INCREMENT,
reservation_id INT NOT NULL,
amount INT NOT NULL,
payment_method CHAR NOT NULL,
payment_date DATE NOT NULL,

FOREIGN KEY (reservation_id)
REFERENCES reservations(id)
);