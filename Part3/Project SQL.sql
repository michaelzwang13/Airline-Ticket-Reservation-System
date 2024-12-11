-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Dec 11, 2024 at 12:05 AM
-- Server version: 8.0.35
-- PHP Version: 8.2.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Project`
--

-- --------------------------------------------------------

--
-- Table structure for table `airline`
--

CREATE TABLE `airline` (
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `airline`
--

INSERT INTO `airline` (`name`) VALUES
('JetBlue');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff`
--

CREATE TABLE `airline_staff` (
  `username` varchar(50) NOT NULL,
  `airline_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `date_of_birth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `airline_staff`
--

INSERT INTO `airline_staff` (`username`, `airline_name`, `password`, `first_name`, `last_name`, `date_of_birth`) VALUES
('admin', 'JetBlue', 'e2fc714c4727ee9395f324cd2e7f331f', 'Roe', 'Jones', '1978-05-25');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff_email`
--

CREATE TABLE `airline_staff_email` (
  `username` varchar(50) NOT NULL,
  `email_address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `airline_staff_email`
--

INSERT INTO `airline_staff_email` (`username`, `email_address`) VALUES
('admin', 'staff1@nyu.edu'),
('admin', 'staff2@nyu.edu');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff_phone_number`
--

CREATE TABLE `airline_staff_phone_number` (
  `username` varchar(50) NOT NULL,
  `phone_number` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `airline_staff_phone_number`
--

INSERT INTO `airline_staff_phone_number` (`username`, `phone_number`) VALUES
('admin', '11122223333'),
('admin', '44455556666');

-- --------------------------------------------------------

--
-- Table structure for table `airplane`
--

CREATE TABLE `airplane` (
  `airline_name` varchar(50) NOT NULL,
  `airplane_id` int NOT NULL,
  `num_seats` int NOT NULL,
  `manufacturing_company` varchar(50) NOT NULL,
  `model_num` varchar(15) NOT NULL,
  `manufacturing_date` date NOT NULL,
  `age` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `airplane`
--

INSERT INTO `airplane` (`airline_name`, `airplane_id`, `num_seats`, `manufacturing_company`, `model_num`, `manufacturing_date`, `age`) VALUES
('JetBlue', 1, 4, 'Boeing', 'B-101', '2013-05-02', 10),
('JetBlue', 2, 4, 'Airbus', 'A-101', '2011-05-02', 12),
('JetBlue', 3, 50, 'Boeing', 'B-101', '2015-05-02', 8);

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `code` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `num_terminals` int NOT NULL,
  `airport_type` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`code`, `name`, `city`, `country`, `num_terminals`, `airport_type`) VALUES
('BEI', 'BEI', 'Beijing', 'China', 2, 'Both'),
('BOS', 'BOS', 'Boston', 'USA', 2, 'Both'),
('HKA', 'HKA', 'Hong Kong', 'China', 2, 'Both'),
('JFK', 'JFK', 'NYC', 'USA', 4, 'Both'),
('LAX', 'LAX', 'Los Angeles', 'USA', 2, 'Both'),
('PVG', 'PVG', 'Shanghai', 'China', 2, 'Both'),
('SFO', 'SFO', 'San Francisco', 'USA', 2, 'Both'),
('SHEN', 'SHEN', 'Shenzhen', 'China', 2, 'Both');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `email_address` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `building_name` varchar(50) NOT NULL,
  `street_name` varchar(50) NOT NULL,
  `apt_num` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zipcode` int NOT NULL,
  `date_of_birth` date NOT NULL,
  `passport_number` varchar(50) NOT NULL,
  `passport_expiration` date NOT NULL,
  `passport_country` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`email_address`, `password`, `first_name`, `last_name`, `building_name`, `street_name`, `apt_num`, `city`, `state`, `zipcode`, `date_of_birth`, `passport_number`, `passport_expiration`, `passport_country`) VALUES
('testcustomer@nyu.edu', '81dc9bdb52d04dc20036dbd8313ed055', 'Jon', 'Snow', '1555', 'Jay St', '', 'Brooklyn', 'New York', 11201, '1999-12-19', '54321', '2025-12-24', 'USA'),
('user1@nyu.edu', '81dc9bdb52d04dc20036dbd8313ed055', 'Alice', 'Bob', '5405', 'Jay Street', '', 'Brooklyn', 'New York', 11201, '1999-11-19', '54322', '2025-12-25', 'USA'),
('user2@nyu.edu', '81dc9bdb52d04dc20036dbd8313ed055', 'Cathy', 'Wood', '1702', 'Jay Street', '', 'Brooklyn', 'New York', 11201, '1999-10-19', '54323', '2025-10-24', 'USA'),
('user3@nyu.edu', '81dc9bdb52d04dc20036dbd8313ed055', 'Trudy', 'Jones', '1890', 'Jay Street', '', 'Brooklyn', 'New York', 11201, '1999-09-19', '54324', '2025-09-24', 'USA');

-- --------------------------------------------------------

--
-- Table structure for table `customer_phone_number`
--

CREATE TABLE `customer_phone_number` (
  `email_address` varchar(50) NOT NULL,
  `phone_number` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `customer_phone_number`
--

INSERT INTO `customer_phone_number` (`email_address`, `phone_number`) VALUES
('testcustomer@nyu.edu', '12343214321'),
('user1@nyu.edu', '12343224322'),
('user2@nyu.edu', '12343234323'),
('user3@nyu.edu', '12343244324');

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `airline_name` varchar(50) NOT NULL,
  `flight_number` varchar(50) NOT NULL,
  `departure_time` time NOT NULL,
  `departure_date` date NOT NULL,
  `arrival_date` date NOT NULL,
  `arrival_time` time NOT NULL,
  `base_price` float NOT NULL,
  `flight_status` varchar(20) NOT NULL,
  `departure_airport_code` varchar(20) NOT NULL,
  `arrival_airport_code` varchar(20) NOT NULL,
  `airplane_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`airline_name`, `flight_number`, `departure_time`, `departure_date`, `arrival_date`, `arrival_time`, `base_price`, `flight_status`, `departure_airport_code`, `arrival_airport_code`, `airplane_id`) VALUES
('JetBlue', '102', '13:25:00', '2024-09-20', '2024-09-20', '16:50:00', 300, 'On-Time', 'SFO', 'LAX', 3),
('JetBlue', '104', '13:25:00', '2024-10-04', '2024-10-04', '16:50:00', 300, 'On-Time', 'PVG', 'BEI', 3),
('JetBlue', '106', '13:25:00', '2024-08-04', '2024-08-04', '16:50:00', 350, 'Delayed', 'SFO', 'LAX', 3),
('JetBlue', '134', '13:25:00', '2023-12-15', '2023-12-15', '16:50:00', 300, 'Delayed', 'JFK', 'BOS', 3),
('JetBlue', '206', '13:25:00', '2025-02-04', '2025-02-04', '16:50:00', 300, 'On-Time', 'SFO', 'LAX', 2),
('JetBlue', '207', '13:25:00', '2025-03-04', '2025-03-04', '16:50:00', 300, 'Delayed', 'LAX', 'SFO', 2),
('JetBlue', '296', '13:25:00', '2024-12-30', '2024-12-30', '16:50:00', 3000, 'On-Time', 'PVG', 'SFO', 1),
('JetBlue', '715', '10:25:00', '2024-09-28', '2024-09-28', '13:50:00', 500, 'Delayed', 'PVG', 'BEI', 1),
('JetBlue', '839', '13:25:00', '2023-12-26', '2023-12-26', '16:50:00', 300, 'On-Time', 'SHEN', 'BEI', 3);

-- --------------------------------------------------------

--
-- Table structure for table `maintenance_procedure`
--

CREATE TABLE `maintenance_procedure` (
  `airline_name` varchar(50) NOT NULL,
  `airplane_id` int NOT NULL,
  `maintenance_start_time` time NOT NULL,
  `maintenance_start_date` date NOT NULL,
  `maintenance_end_time` time NOT NULL,
  `maintenance_end_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `maintenance_procedure`
--

INSERT INTO `maintenance_procedure` (`airline_name`, `airplane_id`, `maintenance_start_time`, `maintenance_start_date`, `maintenance_end_time`, `maintenance_end_date`) VALUES
('JetBlue', 1, '13:25:00', '2025-01-27', '07:25:00', '2025-01-29'),
('JetBlue', 2, '13:25:00', '2025-01-27', '07:25:00', '2025-01-29');

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--

CREATE TABLE `purchase` (
  `email_address` varchar(50) NOT NULL,
  `ID` int NOT NULL,
  `ticket_user_first_name` varchar(50) NOT NULL,
  `ticket_user_last_name` varchar(50) NOT NULL,
  `ticket_user_date_of_birth` date NOT NULL,
  `purchase_date` date NOT NULL,
  `purchase_time` time NOT NULL,
  `card_type` varchar(50) NOT NULL,
  `card_number` decimal(20,0) NOT NULL,
  `card_name` varchar(50) NOT NULL,
  `expiration_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `purchase`
--

INSERT INTO `purchase` (`email_address`, `ID`, `ticket_user_first_name`, `ticket_user_last_name`, `ticket_user_date_of_birth`, `purchase_date`, `purchase_time`, `card_type`, `card_number`, `card_name`, `expiration_date`) VALUES
('testcustomer@nyu.edu', 1, 'Jon', 'Snow', '1999-12-19', '2024-08-17', '11:55:55', 'credit', 1111222233334444, 'Jon Snow', '2025-03-01'),
('testcustomer@nyu.edu', 52, 'Jon', 'Snow', '1999-12-19', '2024-09-28', '11:55:55', 'credit', 1111222233334444, 'Jon Snow', '2024-03-01'),
('testcustomer@nyu.edu', 101, 'Jon', 'Snow', '1999-12-19', '2024-08-02', '11:55:55', 'credit', 1111222233334444, 'Jon Snow', '2024-03-01'),
('testcustomer@nyu.edu', 156, 'Jon', 'Snow', '1999-12-19', '2024-09-25', '11:55:55', 'credit', 1111222233334444, 'Jon Snow', '2024-03-01'),
('testcustomer@nyu.edu', 259, 'Jon', 'Snow', '1999-12-19', '2024-05-02', '11:55:55', 'credit', 1111222233334444, 'Jon Snow', '2024-03-01'),
('testcustomer@nyu.edu', 314, 'Jon', 'Snow', '1999-12-19', '2023-12-17', '11:55:55', 'credit', 1111222233334444, 'Jon Snow', '2024-03-01'),
('user1@nyu.edu', 2, 'Alice', 'Bob', '1999-11-19', '2024-08-16', '11:55:55', 'credit', 1111222233335555, 'Alice Bob', '2025-03-01'),
('user1@nyu.edu', 51, 'Alice', 'Bob', '1999-11-19', '2024-08-21', '11:55:55', 'credit', 1111222233335555, 'Alice Bob', '2024-03-01'),
('user1@nyu.edu', 152, 'Alice', 'Bob', '1999-11-19', '2024-11-21', '11:55:55', 'credit', 1111222233335555, 'Alice Bob', '2024-03-01'),
('user1@nyu.edu', 155, 'Alice', 'Bob', '1999-11-19', '2024-08-15', '11:55:55', 'credit', 1111222233335555, 'Alice Bob', '2024-03-01'),
('user1@nyu.edu', 313, 'Alice', 'Bob', '1999-11-19', '2024-11-22', '11:55:55', 'credit', 1111222233334444, 'Alice Bob', '2024-03-01'),
('user2@nyu.edu', 3, 'Cathy', 'Wood', '1999-10-19', '2024-09-14', '11:55:55', 'credit', 1111222233335555, 'Cathy Wood', '2025-03-01'),
('user2@nyu.edu', 153, 'Cathy', 'Wood', '1999-10-19', '2024-09-19', '11:55:55', 'credit', 1111222233335555, 'Cathy Wood', '2024-03-01'),
('user3@nyu.edu', 4, 'Trudy', 'Jones', '1999-09-19', '2024-07-14', '11:55:55', 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01'),
('user3@nyu.edu', 102, 'Trudy', 'Jones', '1999-09-19', '2024-07-23', '11:55:55', 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01'),
('user3@nyu.edu', 151, 'Trudy', 'Jones', '1999-09-19', '2024-11-20', '11:55:55', 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01'),
('user3@nyu.edu', 263, 'Trudy', 'Jones', '1999-09-19', '2023-10-23', '11:55:55', 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01'),
('user3@nyu.edu', 317, 'Trudy', 'Jones', '1999-09-19', '2023-12-23', '11:55:55', 'credit', 1111222233335555, 'Trudy Jones', '2024-03-01');

-- --------------------------------------------------------

--
-- Table structure for table `rate`
--

CREATE TABLE `rate` (
  `email_address` varchar(50) NOT NULL,
  `airline_name` varchar(50) NOT NULL,
  `flight_number` varchar(50) NOT NULL,
  `departure_time` time NOT NULL,
  `departure_date` date NOT NULL,
  `comments` varchar(100) NOT NULL,
  `rating` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `rate`
--

INSERT INTO `rate` (`email_address`, `airline_name`, `flight_number`, `departure_time`, `departure_date`, `comments`, `rating`) VALUES
('testcustomer@nyu.edu', 'JetBlue', '102', '13:25:00', '2024-09-20', 'Very Comfortable', 4),
('testcustomer@nyu.edu', 'JetBlue', '104', '13:25:00', '2024-10-04', 'Customer Care services are not good', 1),
('user1@nyu.edu', 'JetBlue', '102', '13:25:00', '2024-09-20', 'Relaxing, check-in and onboarding very professional', 5),
('user1@nyu.edu', 'JetBlue', '104', '13:25:00', '2024-10-04', 'Comfortable journey and Professional', 5),
('user2@nyu.edu', 'JetBlue', '102', '13:25:00', '2024-09-20', 'Satisfied and will use the same flight again', 3);

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `ID` int NOT NULL,
  `ticket_price` float NOT NULL,
  `airline_name` varchar(50) DEFAULT NULL,
  `flight_number` varchar(50) DEFAULT NULL,
  `departure_time` time DEFAULT NULL,
  `departure_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`ID`, `ticket_price`, `airline_name`, `flight_number`, `departure_time`, `departure_date`) VALUES
(1, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(2, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(3, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(4, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(5, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(6, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(7, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(8, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(9, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(10, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(11, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(12, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(13, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(14, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(15, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(16, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(17, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(18, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(19, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(20, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(21, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(22, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(23, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(24, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(25, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(26, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(27, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(28, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(29, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(30, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(31, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(32, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(33, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(34, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(35, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(36, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(37, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(38, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(39, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(40, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(41, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(42, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(43, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(44, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(45, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(46, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(47, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(48, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(49, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(50, 300, 'JetBlue', '102', '13:25:00', '2024-09-20'),
(51, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(52, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(53, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(54, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(55, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(56, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(57, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(58, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(59, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(60, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(61, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(62, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(63, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(64, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(65, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(66, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(67, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(68, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(69, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(70, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(71, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(72, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(73, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(74, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(75, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(76, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(77, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(78, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(79, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(80, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(81, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(82, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(83, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(84, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(85, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(86, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(87, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(88, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(89, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(90, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(91, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(92, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(93, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(94, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(95, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(96, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(97, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(98, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(99, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(100, 300, 'JetBlue', '104', '13:25:00', '2024-10-04'),
(101, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(102, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(103, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(104, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(105, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(106, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(107, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(108, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(109, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(110, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(111, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(112, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(113, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(114, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(115, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(116, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(117, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(118, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(119, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(120, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(121, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(122, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(123, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(124, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(125, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(126, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(127, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(128, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(129, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(130, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(131, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(132, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(133, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(134, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(135, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(136, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(137, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(138, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(139, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(140, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(141, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(142, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(143, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(144, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(145, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(146, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(147, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(148, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(149, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(150, 350, 'JetBlue', '106', '13:25:00', '2024-08-04'),
(151, 300, 'JetBlue', '206', '13:25:00', '2025-02-04'),
(152, 300, 'JetBlue', '206', '13:25:00', '2025-02-04'),
(153, 300, 'JetBlue', '206', '13:25:00', '2025-02-04'),
(154, 300, 'JetBlue', '206', '13:25:00', '2025-02-04'),
(155, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(156, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(157, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(158, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(159, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(160, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(161, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(162, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(163, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(164, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(165, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(166, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(167, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(168, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(169, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(170, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(171, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(172, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(173, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(174, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(175, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(176, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(177, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(178, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(179, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(180, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(181, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(182, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(183, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(184, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(185, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(186, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(187, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(188, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(189, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(190, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(191, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(192, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(193, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(194, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(195, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(196, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(197, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(198, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(199, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(200, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(201, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(202, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(203, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(204, 300, 'JetBlue', '207', '13:25:00', '2025-03-04'),
(259, 500, 'JetBlue', '715', '10:25:00', '2024-09-28'),
(260, 500, 'JetBlue', '715', '10:25:00', '2024-09-28'),
(261, 500, 'JetBlue', '715', '10:25:00', '2024-09-28'),
(262, 500, 'JetBlue', '715', '10:25:00', '2024-09-28'),
(263, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(264, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(265, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(266, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(267, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(268, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(269, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(270, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(271, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(272, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(273, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(274, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(275, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(276, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(277, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(278, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(279, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(280, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(281, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(282, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(283, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(284, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(285, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(286, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(287, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(288, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(289, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(290, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(291, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(292, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(293, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(294, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(295, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(296, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(297, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(298, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(299, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(300, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(301, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(302, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(303, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(304, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(305, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(306, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(307, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(308, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(309, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(310, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(311, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(312, 300, 'JetBlue', '134', '13:25:00', '2023-12-15'),
(313, 3000, 'JetBlue', '296', '13:25:00', '2024-12-30'),
(314, 3000, 'JetBlue', '296', '13:25:00', '2024-12-30'),
(315, 3000, 'JetBlue', '296', '13:25:00', '2024-12-30'),
(316, 3000, 'JetBlue', '296', '13:25:00', '2024-12-30'),
(317, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(318, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(319, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(320, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(321, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(322, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(323, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(324, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(325, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(326, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(327, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(328, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(329, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(330, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(331, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(332, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(333, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(334, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(335, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(336, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(337, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(338, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(339, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(340, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(341, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(342, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(343, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(344, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(345, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(346, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(347, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(348, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(349, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(350, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(351, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(352, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(353, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(354, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(355, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(356, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(357, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(358, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(359, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(360, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(361, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(362, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(363, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(364, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(365, 300, 'JetBlue', '839', '13:25:00', '2023-12-26'),
(366, 300, 'JetBlue', '839', '13:25:00', '2023-12-26');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airline`
--
ALTER TABLE `airline`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD PRIMARY KEY (`username`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airline_staff_email`
--
ALTER TABLE `airline_staff_email`
  ADD PRIMARY KEY (`username`,`email_address`);

--
-- Indexes for table `airline_staff_phone_number`
--
ALTER TABLE `airline_staff_phone_number`
  ADD PRIMARY KEY (`username`,`phone_number`);

--
-- Indexes for table `airplane`
--
ALTER TABLE `airplane`
  ADD PRIMARY KEY (`airline_name`,`airplane_id`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`code`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`email_address`);

--
-- Indexes for table `customer_phone_number`
--
ALTER TABLE `customer_phone_number`
  ADD PRIMARY KEY (`email_address`,`phone_number`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`airline_name`,`flight_number`,`departure_time`,`departure_date`),
  ADD KEY `airline_name` (`airline_name`,`airplane_id`),
  ADD KEY `departure_airport_code` (`departure_airport_code`),
  ADD KEY `arrival_airport_code` (`arrival_airport_code`);

--
-- Indexes for table `maintenance_procedure`
--
ALTER TABLE `maintenance_procedure`
  ADD PRIMARY KEY (`airline_name`,`airplane_id`,`maintenance_start_time`,`maintenance_start_date`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`email_address`,`ID`),
  ADD KEY `ID` (`ID`);

--
-- Indexes for table `rate`
--
ALTER TABLE `rate`
  ADD PRIMARY KEY (`email_address`,`airline_name`,`flight_number`,`departure_time`,`departure_date`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`departure_time`,`departure_date`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `airline_name` (`airline_name`,`flight_number`,`departure_time`,`departure_date`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD CONSTRAINT `airline_staff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);

--
-- Constraints for table `airline_staff_email`
--
ALTER TABLE `airline_staff_email`
  ADD CONSTRAINT `airline_staff_email_ibfk_1` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`);

--
-- Constraints for table `airline_staff_phone_number`
--
ALTER TABLE `airline_staff_phone_number`
  ADD CONSTRAINT `airline_staff_phone_number_ibfk_1` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`);

--
-- Constraints for table `airplane`
--
ALTER TABLE `airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);

--
-- Constraints for table `customer_phone_number`
--
ALTER TABLE `customer_phone_number`
  ADD CONSTRAINT `customer_phone_number_ibfk_1` FOREIGN KEY (`email_address`) REFERENCES `customer` (`email_address`);

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airline_name`,`airplane_id`) REFERENCES `airplane` (`airline_name`, `airplane_id`),
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`departure_airport_code`) REFERENCES `airport` (`code`),
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`arrival_airport_code`) REFERENCES `airport` (`code`);

--
-- Constraints for table `maintenance_procedure`
--
ALTER TABLE `maintenance_procedure`
  ADD CONSTRAINT `maintenance_procedure_ibfk_1` FOREIGN KEY (`airline_name`,`airplane_id`) REFERENCES `airplane` (`airline_name`, `airplane_id`);

--
-- Constraints for table `purchase`
--
ALTER TABLE `purchase`
  ADD CONSTRAINT `purchase_ibfk_1` FOREIGN KEY (`email_address`) REFERENCES `customer` (`email_address`),
  ADD CONSTRAINT `purchase_ibfk_2` FOREIGN KEY (`ID`) REFERENCES `ticket` (`ID`);

--
-- Constraints for table `rate`
--
ALTER TABLE `rate`
  ADD CONSTRAINT `rate_ibfk_1` FOREIGN KEY (`email_address`) REFERENCES `customer` (`email_address`),
  ADD CONSTRAINT `rate_ibfk_2` FOREIGN KEY (`airline_name`,`flight_number`,`departure_time`,`departure_date`) REFERENCES `flight` (`airline_name`, `flight_number`, `departure_time`, `departure_date`);

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`airline_name`,`flight_number`,`departure_time`,`departure_date`) REFERENCES `flight` (`airline_name`, `flight_number`, `departure_time`, `departure_date`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
