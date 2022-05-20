-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2022 at 11:12 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank_loan_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `S.No` int(255) NOT NULL,
  `EMAIL_ID` varchar(35) NOT NULL,
  `MOBILE_NO` varchar(13) NOT NULL,
  `NAME` varchar(34) NOT NULL,
  `ADDRESS` varchar(54) NOT NULL,
  `PAN` varchar(10) NOT NULL,
  `COMPANY_NAME` varchar(20) NOT NULL,
  `CURRENT_SALARY` int(10) NOT NULL,
  `PREVIOUS_SALARY` int(10) NOT NULL,
  `HOUSE` varchar(10) NOT NULL,
  `RENT` int(10) NOT NULL,
  `EXPENSE` int(10) NOT NULL,
  `TOTAL_EMI` int(10) NOT NULL,
  `TOTAL_EMI_AMOUNT` int(10) NOT NULL,
  `PREVIOUS_HIKE_DATE` date NOT NULL,
  `ESTIMATE_HIKE_DATE` date NOT NULL,
  `BANK_NAME` varchar(30) NOT NULL,
  `LOAN_DURING` varchar(20) NOT NULL,
  `ELIGIBLITY` varchar(20) NOT NULL,
  `Eligible_Amount` int(10) NOT NULL,
  `One_Month_EMI` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`S.No`, `EMAIL_ID`, `MOBILE_NO`, `NAME`, `ADDRESS`, `PAN`, `COMPANY_NAME`, `CURRENT_SALARY`, `PREVIOUS_SALARY`, `HOUSE`, `RENT`, `EXPENSE`, `TOTAL_EMI`, `TOTAL_EMI_AMOUNT`, `PREVIOUS_HIKE_DATE`, `ESTIMATE_HIKE_DATE`, `BANK_NAME`, `LOAN_DURING`, `ELIGIBLITY`, `Eligible_Amount`, `One_Month_EMI`) VALUES
(1, 'yegappans2910@gmail.com', '9361326066', 'Yegappan S', '219/6 VSR complex ,Aranthangi ,Pudukottai', 'AQUE87345U', 'CARTRABBIT', 35000, 33000, 'Own House', 0, 11800, 0, 0, '2021-05-01', '2022-05-01', 'STATE BANK OF INDIA', '12', 'ELIGIBLE', 194880, 16240),
(2, 'sakthivel@gmail.com', '9753759375', 'Sakthivel', 'Erode main ,Erode', 'HIUI87645U', 'CTS', 30000, 25000, 'Rental Hou', 6000, 20500, 2, 6000, '2021-11-30', '2022-03-01', 'STATE BANK OF INDIA', '12', 'NOT ELIGIBLE', 0, 0),
(3, 'yogalingam@gmail.com', '9935873873', 'yogalingam', 'perundurai,erode', 'FGFJH56578', 'TCS', 40000, 38000, 'Own House', 0, 13000, 1, 3000, '2022-03-15', '2022-07-16', 'STATE BANK OF INDIA', '12', 'ELIGIBLE', 201600, 16800),
(4, 'sudharsan@gmail.com', '9976873873', 'sudharsan', 'kumbakonam main road,Kumbakonam', 'GJHGF65875', 'INFOSYS', 50000, 43000, 'Own House', 0, 19300, 0, 0, '2022-01-01', '2022-09-01', 'ICICI BANK', '16', 'ELIGIBLE', 343840, 21490),
(5, 'vijay@gmail.com', '9979876873', 'vijay kumar', 'perundurai main road,erode', 'GJGUT56576', 'WIPRO', 30000, 25000, 'Rental Hou', 4000, 24000, 2, 6000, '2022-01-01', '2022-09-01', 'ICICI BANK', '16', 'NOT ELIGIBLE', 0, 0),
(6, 'vikram@gmail.com', '9867898767', 'vikram k', '137/14a,vr appartments,chennai', 'ADRYG56788', 'ZOHO', 50000, 45000, 'Own House', 0, 20000, 0, 0, '2021-12-01', '2022-12-01', 'STATE BANK OF INDIA', '12', 'ELIGIBLE', 180000, 15000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`S.No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `S.No` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
