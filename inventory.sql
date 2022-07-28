-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 27, 2022 at 07:02 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `Product_Name` varchar(100) NOT NULL,
  `Product_Quantity` varchar(100) NOT NULL,
  `Product_SKU` varchar(100) CHARACTER SET utf8 NOT NULL,
  `Selling_Price` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`Product_Name`, `Product_Quantity`, `Product_SKU`, `Selling_Price`) VALUES
('Chair', '3', 'CH', '1200'),
('Headphone', '2', 'HP', '1200');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `Transaction_ID` int(100) NOT NULL,
  `Sold_Quantity` varchar(100) NOT NULL,
  `SKU` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Transaction_Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`Transaction_ID`, `Sold_Quantity`, `SKU`, `Transaction_Date`) VALUES
(13, '1', 'HP', '2022-07-26'),
(14, '1', 'HP', '2022-07-26'),
(15, '1', 'CH', '2022-07-26'),
(16, '1', 'CH', '2022-07-26'),
(17, '1', 'HP', '2022-07-26'),
(18, '2', 'HP', '2022-07-26'),
(19, '1', 'CH', '2022-07-26'),
(20, '1', 'HP', '2022-07-26'),
(21, '3', 'HP', '2022-07-26'),
(22, '1', 'CH', '2022-07-26');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UID` int(100) NOT NULL,
  `UserName` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UID`, `UserName`, `Password`) VALUES
(7, 'Ayush', 'Nepal2014!'),
(8, 'Ayush1', 'Nepal2014!'),
(9, 'Ayush22', '12345'),
(10, 'Test', 'Nepal'),
(11, 'abcd', '222'),
(12, 'TestUser', '123'),
(13, 'Unique', '123'),
(14, 'Unique2', '123'),
(15, 'Unique3', '12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`Product_SKU`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`Transaction_ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `Transaction_ID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `UID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
