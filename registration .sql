-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 19, 2023 at 06:37 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `uname` char(90) DEFAULT NULL,
  `pwd` varchar(90) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `fname` char(49) DEFAULT NULL,
  `lname` char(90) DEFAULT NULL,
  `uname` char(90) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  `phone` int(90) DEFAULT NULL,
  `gender` char(40) DEFAULT NULL,
  `pwd` varchar(89) DEFAULT NULL,
  `cpwd` varchar(90) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`fname`, `lname`, `uname`, `email`, `phone`, `gender`, `pwd`, `cpwd`) VALUES
('Akash', 'Bhalshankar', 'akash', 'akashbhalshankar474@gmail.com', 2147483647, 'male', '111111', '111111'),
('Akash', 'Bhalshankar', 'akash', 'akashbhalshankar474@gmail.com', 2147483647, 'male', '1234', 'yy'),
('Akash', 'Bhalshankar', 'new', 'akashbhalshankar474@gmail.com', 2147483647, 'male', '22', '22'),
('Gadila', 'Vamshi', 'login', 'vamshigadila@gmail.com', 2147483647, 'male', '123', '123'),
('Akshay', 'vadskar', 'a', 'akashbhalshankar474@gmail.com', 2147483647, 'male', '1', '1'),
('w', 'w', 'q', 'qq', 4, 'male', '1', '1'),
('Akash', 'Bhalshankar', 'z', 'akashbhalshankar474@gmail.com', 2147483647, 'femal', 'z', 'z'),
('Akash', 'Bhalshankar', 'm', 'akashbhalshankar474@gmail.com', 2147483647, 'male', 'm', 'm');

-- --------------------------------------------------------

--
-- Table structure for table `designer`
--

CREATE TABLE `designer` (
  `fname` char(90) DEFAULT NULL,
  `lname` char(90) DEFAULT NULL,
  `uname` char(90) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  `phone` bigint(90) DEFAULT NULL,
  `gender` char(90) DEFAULT NULL,
  `qual` varchar(90) DEFAULT NULL,
  `work` varchar(99) DEFAULT NULL,
  `pwd` varchar(90) DEFAULT NULL,
  `cpwd` varchar(90) DEFAULT NULL,
  `id` varchar(90) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `designer`
--

INSERT INTO `designer` (`fname`, `lname`, `uname`, `email`, `phone`, `gender`, `qual`, `work`, `pwd`, `cpwd`, `id`) VALUES
('Akash', 'Bhalshankar', 'a', 'akashbhalshankar474@gmail.com', 2147483647, 'male', 'de', 'FullStack webdevelopment', 'a', 'a', 'a'),
('Akash', 'Bhalshankar', 'a', 'akashbhalshankar474@gmail.com', 2147483647, 'male', 'de', 'FullStack webdevelopment', 'a', 'a', 'a'),
('Akash', 'Bhalshankar', 'b', 'akashbhalshankar474@gmail.com', 2147483647, 'male', 'de', 'FullStack webdevelopment', 'b', 'b', 'b'),
('Akash', 'Bhalshankar', 'a', 'akashbhalshankar474@gmail.com', 2147483647, 'femal', 'de', 'FullStack webdevelopment', 'd', 'e', '3'),
('swapna', 'sunkari', 'swapnasunkari', 'swapnaammu2020@gmail.com', 2147483647, 'femal', 'B.Tech', 'kits,4', '12345', '12345', '501');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `productId` int(11) NOT NULL,
  `name` char(90) DEFAULT NULL,
  `image` varchar(90) DEFAULT NULL,
  `description` char(90) DEFAULT NULL,
  `links` char(90) DEFAULT NULL,
  `categoryId` varchar(90) DEFAULT NULL,
  `gender` varchar(90) DEFAULT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`productId`, `name`, `image`, `description`, `links`, `categoryId`, `gender`, `id`) VALUES
(103, 'Wedding', 'khan.jpg', '', 'abc', '501', '2', 0),
(104, 'Wedding', 'wed2.jpg', '', 'abc', '501', '2', 0),
(105, 'shirt', 'khan.jpg', '', 'abc', '1', '1', 0),
(106, 'shirt', 'khan.jpg', 'lehanga', 'abc', '2', '2', 0);

-- --------------------------------------------------------

--
-- Table structure for table `productslinks`
--

CREATE TABLE `productslinks` (
  `productlinkid` int(90) NOT NULL,
  `linkname` varchar(90) DEFAULT NULL,
  `link` varchar(90) DEFAULT NULL,
  `productId` int(90) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `productslinks`
--

INSERT INTO `productslinks` (`productlinkid`, `linkname`, `link`, `productId`) VALUES
(169, 'Saree', 'https://www.myntra.com/saree/angroop/angroop-embellished-sequinned-net-saree/24357712/buy', 103),
(170, 'Jwellery', 'https://www.myntra.com/jewellery-set/sukkhi/sukkhi-gold-plated--white-youthful-kundan-stud', 103),
(171, 'LehangaCholi', 'https://www.myntra.com/topwear/odette/odette-embroidered-sequinned-semi-stitched-lehenga-c', 104),
(172, 'HandBag', 'https://amzn.eu/d/8ggUnfA', 104),
(173, 'Jewellry', 'https://www.myntra.com/jewellery-set/sukkhi/sukkhi-gold-plated--white-youthful-kundan-stud', 104),
(174, 'laptop', 'https://www.amazon.in/sspa/click?', 105),
(175, 'dress', 'https://www.amazon.in/sspa/click?ie=UTF8&spc=MTo4NzY2Mjk1MzM5MDkyNjMwOjE2OTU0NjE1MTc6c3BfY', 105),
(176, 'shirt', 'https://www.ajio.com/men-shirts/c/830216013', 106);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`productId`);

--
-- Indexes for table `productslinks`
--
ALTER TABLE `productslinks`
  ADD PRIMARY KEY (`productlinkid`),
  ADD KEY `productId` (`productId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `productId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT for table `productslinks`
--
ALTER TABLE `productslinks`
  MODIFY `productlinkid` int(90) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=177;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `productslinks`
--
ALTER TABLE `productslinks`
  ADD CONSTRAINT `productslinks_ibfk_1` FOREIGN KEY (`productId`) REFERENCES `products` (`productId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
