-- phpMyAdmin SQL Dump
-- version 4.4.15.8
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 07, 2017 at 06:09 PM
-- Server version: 5.6.31
-- PHP Version: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Quizzer`
--

-- --------------------------------------------------------

--
-- Table structure for table `Instructor`
--

CREATE TABLE IF NOT EXISTS `Instructor` (
  `userID` int(11) NOT NULL,
  `userName` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Instructor`
--

INSERT INTO `Instructor` (`userID`, `userName`, `password`) VALUES
(1, 'Shamyl BM', 'hunter12');

-- --------------------------------------------------------

--
-- Table structure for table `MCQs`
--

CREATE TABLE IF NOT EXISTS `MCQs` (
  `MCQID` int(11) NOT NULL,
  `relatedToQuiz` int(11) NOT NULL,
  `Question` varchar(200) NOT NULL,
  `op1` varchar(200) NOT NULL,
  `op2` varchar(200) NOT NULL,
  `op3` varchar(200) NOT NULL,
  `op4` varchar(200) NOT NULL,
  `correct` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `MCQs`
--

INSERT INTO `MCQs` (`MCQID`, `relatedToQuiz`, `Question`, `op1`, `op2`, `op3`, `op4`, `correct`) VALUES
(1, 1, 'tesring421', 'choice1', 'choice2', 'choice3', 'choice4', 3);

-- --------------------------------------------------------

--
-- Table structure for table `numerical`
--

CREATE TABLE IF NOT EXISTS `numerical` (
  `numericalID` int(11) NOT NULL,
  `relatedToQuiz` int(11) NOT NULL,
  `numericalQuestion` varchar(200) NOT NULL,
  `numericalAns` float NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `numerical`
--

INSERT INTO `numerical` (`numericalID`, `relatedToQuiz`, `numericalQuestion`, `numericalAns`) VALUES
(1, 1, 'testing321', 140);

-- --------------------------------------------------------

--
-- Table structure for table `Quiz`
--

CREATE TABLE IF NOT EXISTS `Quiz` (
  `quizID` int(11) NOT NULL,
  `quizName` varchar(30) NOT NULL,
  `quizTime` int(11) NOT NULL COMMENT 'time entered in minutes',
  `maxScore` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Quiz`
--

INSERT INTO `Quiz` (`quizID`, `quizName`, `quizTime`, `maxScore`) VALUES
(1, 'test1', 10, 30);

-- --------------------------------------------------------

--
-- Table structure for table `Student`
--

CREATE TABLE IF NOT EXISTS `Student` (
  `studentID` int(11) NOT NULL,
  `userName` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Student`
--

INSERT INTO `Student` (`studentID`, `userName`, `password`, `score`) VALUES
(1, 'Khuzaima J', 'dingDong', 0);

-- --------------------------------------------------------

--
-- Table structure for table `trueFalse`
--

CREATE TABLE IF NOT EXISTS `trueFalse` (
  `TFID` int(11) NOT NULL,
  `relatedToQuiz` int(11) NOT NULL,
  `TFquestion` varchar(200) NOT NULL,
  `trueOP` varchar(200) NOT NULL,
  `falseOP` varchar(200) NOT NULL,
  `correctOP` varchar(2) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `trueFalse`
--

INSERT INTO `trueFalse` (`TFID`, `relatedToQuiz`, `TFquestion`, `trueOP`, `falseOP`, `correctOP`) VALUES
(1, 1, 'testing123', 'true', 'false', 'T');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Instructor`
--
ALTER TABLE `Instructor`
  ADD PRIMARY KEY (`userID`);

--
-- Indexes for table `MCQs`
--
ALTER TABLE `MCQs`
  ADD PRIMARY KEY (`MCQID`),
  ADD KEY `relatedToQuiz` (`relatedToQuiz`);

--
-- Indexes for table `numerical`
--
ALTER TABLE `numerical`
  ADD PRIMARY KEY (`numericalID`),
  ADD KEY `relatedToQuiz` (`relatedToQuiz`),
  ADD KEY `relatedToQuiz_2` (`relatedToQuiz`);

--
-- Indexes for table `Quiz`
--
ALTER TABLE `Quiz`
  ADD PRIMARY KEY (`quizID`);

--
-- Indexes for table `Student`
--
ALTER TABLE `Student`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `trueFalse`
--
ALTER TABLE `trueFalse`
  ADD PRIMARY KEY (`TFID`),
  ADD KEY `relatedToQuiz` (`relatedToQuiz`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Instructor`
--
ALTER TABLE `Instructor`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `MCQs`
--
ALTER TABLE `MCQs`
  MODIFY `MCQID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `numerical`
--
ALTER TABLE `numerical`
  MODIFY `numericalID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `Quiz`
--
ALTER TABLE `Quiz`
  MODIFY `quizID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `Student`
--
ALTER TABLE `Student`
  MODIFY `studentID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `trueFalse`
--
ALTER TABLE `trueFalse`
  MODIFY `TFID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `MCQs`
--
ALTER TABLE `MCQs`
  ADD CONSTRAINT `mcqs_ibfk_1` FOREIGN KEY (`relatedToQuiz`) REFERENCES `Quiz` (`quizID`);

--
-- Constraints for table `numerical`
--
ALTER TABLE `numerical`
  ADD CONSTRAINT `numerical_ibfk_1` FOREIGN KEY (`relatedToQuiz`) REFERENCES `Quiz` (`quizID`);

--
-- Constraints for table `trueFalse`
--
ALTER TABLE `trueFalse`
  ADD CONSTRAINT `truefalse_ibfk_1` FOREIGN KEY (`relatedToQuiz`) REFERENCES `Quiz` (`quizID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
