CREATE TABLE airline(
    name VARCHAR(30),
    PRIMARY KEY(name)
);
   
CREATE TABLE airplane(
    airline_name VARCHAR(50),
    ID INT,
    num_seats INT NOT NULL,
    manufacturing_company VARCHAR(50) NOT NULL,
    model_num VARCHAR(15) NOT NULL,
    manufacturing_date DATE NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY(airline_name, ID),
    FOREIGN KEY(airline_name) REFERENCES airline(name)
);

CREATE TABLE airport(
    code VARCHAR(20),
    name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    num_terminals INT NOT NULL,
    airport_type VARCHAR(30) NOT NULL,
	PRIMARY KEY (code)
);

CREATE TABLE flight(
    airline_name VARCHAR(50),
    flight_number VARCHAR(50),
    departure_time TIME,
    departure_date DATE,
    arrival_date DATE NOT NULL,
    arrival_time TIME NOT NULL,
    base_price FLOAT NOT NULL,
    flight_status VARCHAR(20) NOT NULL,
    departure_airport_code VARCHAR(20) NOT NULL,
    arrival_airport_code VARCHAR(20) NOT NULL,
    airplane_id INT,
    PRIMARY KEY(airline_name,flight_number,departure_time,departure_date),
    FOREIGN KEY(airline_name,airplane_id) REFERENCES airplane(airline_name,ID),
    FOREIGN KEY(departure_airport_code) REFERENCES airport(code),
    FOREIGN KEY(arrival_airport_code) REFERENCES airport(code)
);

CREATE TABLE ticket(
    ID INT,
    ticket_price FLOAT NOT NULL,
    airline_name VARCHAR(50),
    flight_number VARCHAR(50),
    departure_time TIME,
    departure_date DATE,
    PRIMARY KEY(ID),
    FOREIGN KEY(airline_name,flight_number,departure_time,departure_date) REFERENCES flight(airline_name,flight_number,departure_time,departure_date)
);

CREATE TABLE airline_staff(
    username VARCHAR(50),
    airline_name VARCHAR(50),
    password VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    PRIMARY KEY (username),
    FOREIGN KEY (airline_name) REFERENCES airline(name)
);
 
CREATE TABLE customer(
    email_address VARCHAR(50),
    password VARCHAR(50) NOT NULL,
    first_name VARCHAR(50)NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    building_name VARCHAR(50) NOT NULL,
    street_name VARCHAR(50) NOT NULL,
    apt_num VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zipcode INT NOT NULL, 
    date_of_birth DATE NOT NULL,
    passport_number VARCHAR(50) NOT NULL,
    passport_expiration DATE NOT NULL,
    passport_country VARCHAR(50) NOT NULL,
    PRIMARY KEY (email_address)
);

CREATE TABLE customer_phone_number(
    email_address VARCHAR(50),
    phone_number VARCHAR(50),
    PRIMARY KEY(email_address,phone_number),
    FOREIGN KEY(email_address) REFERENCES customer(email_address)
);

CREATE TABLE airline_staff_phone_number(
    username VARCHAR(50),
    phone_number VARCHAR(50),
    PRIMARY KEY(username,phone_number),
    FOREIGN KEY(username) REFERENCES airline_staff(username)
);

CREATE TABLE airline_staff_email(
    username VARCHAR(50),
    email_address VARCHAR(50),
    PRIMARY KEY(username,email_address),
    FOREIGN KEY(username) REFERENCES airline_staff(username)
);

CREATE TABLE maintenance_procedure(
    airline_name VARCHAR(50),
    ID INT,
    maintenance_start_time TIME NOT NULL,
    maintenance_start_date DATE NOT NULL,
    maintenance_end_time TIME NOT NULL,
    maintenance_end_date DATE NOT NULL,
    PRIMARY KEY (airline_name,ID),
    FOREIGN KEY (airline_name,ID) REFERENCES airplane(airline_name,ID)
);

CREATE TABLE rate(
    email_address VARCHAR(50),
    airline_name VARCHAR(50),
    flight_number VARCHAR(50),
    departure_time TIME,
    departure_date DATE,
    comments VARCHAR(100) NOT NULL,
    rating INT NOT NULL,
    PRIMARY KEY(email_address,airline_name,flight_number,departure_time,departure_date),
    FOREIGN KEY (email_address) REFERENCES customer(email_address),
    FOREIGN KEY (airline_name,flight_number,departure_time,departure_date) REFERENCES flight(airline_name,flight_number,departure_time,departure_date)
);

CREATE TABLE purchase(
    email_address VARCHAR(50),
    ID INT,
    ticket_user_first_name VARCHAR(50) NOT NULL,
    ticket_user_last_name VARCHAR(50) NOT NULL,
    ticket_user_date_of_birth DATE NOT NULL,
    purchase_date DATE NOT NULL,
    purchase_time TIME NOT NULL,
    card_type VARCHAR(50) NOT NULL,
    card_number DECIMAL(20,0) NOT NULL,
    card_name VARCHAR(50) NOT NULL,
    expiration_date DATE NOT NULL,
    PRIMARY KEY(email_address,ID),
FOREIGN KEY(email_address) REFERENCES customer(email_address),
    FOREIGN KEY(ID) REFERENCES ticket(ID)
);
