-- MySQL dump 10.13  Distrib 5.7.44, for Linux (x86_64)
--
-- Host: localhost    Database: codyx_dev
-- ------------------------------------------------------
-- Server version	5.7.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

USE codyx_dev;
--
-- Table structure for table `challenges`
--

DROP TABLE IF EXISTS `challenges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `challenges` (
  `name` varchar(128) NOT NULL,
  `description` varchar(4096) NOT NULL,
  `ex_input` varchar(1024) NOT NULL,
  `output` varchar(1024) NOT NULL,
  `difficulty` varchar(128) NOT NULL,
  `template` json NOT NULL,
  `example` json NOT NULL,
  `stars` int(11) DEFAULT NULL,
  `solved` int(11) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `challenges`
--

LOCK TABLES `challenges` WRITE;
/*!40000 ALTER TABLE `challenges` DISABLE KEYS */;
INSERT INTO `challenges` VALUES ('anagram','Write a function that checks if two strings are anagrams','s1 (string), s2 (string)','True if s1 is an anagram of s2, False otherwise','easy','\"{\'python\': \'def anagram(s1, s2):\\\\n    pass\', \'javascript\': \'exports.anagram = function (str1, str2) {\\\\n    // your code here\\\\n}\'}\"','\"[{\'id\': 1, \'input\': [\'hello\', \'world\'], \'output\': \'False\', \'explanation\': \\\"\'hello\' and \'world\' are not anagrams\\\"}, {\'id\': 2, \'input\': [\'listen\', \'silent\'], \'output\': \'True\', \'explanation\': \\\"\'listen\' and \'silent\' are anagrams\\\"}, {\'id\': 3, \'input\': [\'racecar\', \'carrace\'], \'output\': \'True\', \'explanation\': \\\"\'racecar\' and \'carrace\' are anagrams\\\"}]\"',0,0,'05a67bdb-aff3-48e9-a9d0-32498c08d052','2024-07-26 14:16:41','2024-07-26 14:16:41'),('fibonacci','Write a function that returns the sum of nth number in the Fibonacci sequence','n (0 <= n <= 100)','sum of nth number in the Fibonacci sequence','easy','\"{\\\"python\\\": \\\"def fibonacci(n):\\\\n    pass\\\",\\\"javascript\\\": \\\"exports.fibonacci = function (n) {\\\\n    // your code here\\\\n}\\\"}\"','\"[{\\\"id\\\": 1,\\\"input\\\": \\\"0\\\",\\\"output\\\": \\\"0\\\",\\\"explanation\\\": \\\"0th number in the Fibonacci sequence is 0\\\"},{\\\"id\\\": 2,\\\"input\\\": \\\"1\\\",\\\"output\\\": \\\"1\\\",\\\"explanation\\\": \\\"1st number in the Fibonacci sequence is 1\\\"},{\\\"id\\\": 3,\\\"input\\\": \\\"-1\\\",\\\"output\\\": \\\"1\\\",\\\"explanation\\\": \\\"Negative numbers are not allowed. The absolute value of -1 is 1\\\"},{\\\"id\\\": 4,\\\"input\\\": \\\"6\\\",\\\"output\\\": \\\"8\\\",\\\"explanation\\\": \\\"0 + 1 + 1 + 2 + 3 + 5 = 8\\\"},{\\\"id\\\": 5,\\\"input\\\": \\\"10\\\",\\\"output\\\": \\\"55\\\",\\\"explanation\\\": \\\"0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 = 55\\\"}]\"',0,0,'1ce4d213-addf-4ae9-b135-176c78814f9b','2024-07-26 12:54:33','2024-07-26 12:54:33'),('reverse_string','Write a function that reverses a string','s (string)','reversed string','easy','\"{\'python\': \'def reverse_string(s):\\\\n    pass\', \'javascript\': \'exports.reverseString = function (str) {\\\\n    // your code here\\\\n}\'}\"','\"[{\'id\': 1, \'input\': \'hello\', \'output\': \'olleh\', \'explanation\': \\\"The reverse of \'hello\' is \'olleh\'\\\"}, {\'id\': 2, \'input\': \'world\', \'output\': \'dlrow\', \'explanation\': \\\"The reverse of \'world\' is \'dlrow\'\\\"}, {\'id\': 3, \'input\': \'racecar\', \'output\': \'racecar\', \'explanation\': \\\"The reverse of \'racecar\' is \'racecar\'\\\"}]\"',0,0,'316eb697-4df9-4d16-90aa-ef08ea61972e','2024-07-26 14:16:41','2024-07-26 14:16:41'),('subarray_sum_equals_k','Write a function that finds the total number of continuous subarrays whose sum equals to a given target k','nums (list of integers), k (integer)','number of subarrays','medium','\"{\'python\': \'def subarray_sum_equals_k(nums, k):\\\\n    pass\', \'javascript\': \'exports.subarraySumEqualsK = function (nums, k) {\\\\n    // your code here\\\\n}\'}\"','\"[{\'id\': 1, \'input\': \'[1, 1, 1], 2\', \'output\': \'2\', \'explanation\': \'There are 2 subarrays with a sum of 2: [1, 1] and [1, 1]\'}, {\'id\': 2, \'input\': \'[1, 2, 3], 3\', \'output\': \'2\', \'explanation\': \'There are 2 subarrays with a sum of 3: [1, 2] and [3]\'}, {\'id\': 3, \'input\': \'[1, -1, 0], 0\', \'output\': \'3\', \'explanation\': \'There are 3 subarrays with a sum of 0: [1, -1, 0], [-1, 0], and [0]\'}]\"',0,0,'51415db5-800c-4fe9-ae5c-530f50170aef','2024-07-26 14:16:42','2024-07-26 14:16:42'),('factorial','Write a function that returns the factorial of a number','n (0 <= n <= 100)','factorial of n','easy','\"{\'python\': \'def factorial(n):\\\\n    pass\', \'javascript\': \'exports.factorial = function (n) {\\\\n    // your code here\\\\n}\'}\"','\"[{\'id\': 1, \'input\': \'0\', \'output\': \'1\', \'explanation\': \'Factorial of 0 is 1\'}, {\'id\': 2, \'input\': \'1\', \'output\': \'1\', \'explanation\': \'Factorial of 1 is 1\'}, {\'id\': 3, \'input\': \'-1\', \'output\': \'Factorial of negative number is not possible\', \'explanation\': \'Negative numbers are not allowed\'}, {\'id\': 4, \'input\': \'5\', \'output\': \'120\', \'explanation\': \'5 * 4 * 3 * 2 * 1 = 120\'}, {\'id\': 5, \'input\': \'10\', \'output\': \'3628800\', \'explanation\': \'10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800\'}]\"',0,0,'6edf7ea0-f4ec-4c29-95a3-ed7bc47c9f74','2024-07-26 14:16:41','2024-07-26 14:16:41'),('rotate_array','Write a function that rotates an array to the right by k steps','nums (list of integers), k (integer)','rotated array','medium','\"{\'python\': \'def rotate_array(nums, k):\\\\n    pass\', \'javascript\': \'exports.rotateArray = function (arr, k) {\\\\n    // your code here\\\\n}\'}\"','\"[{\'id\': 1, \'input\': \'[1, 2, 3, 4, 5], 2\', \'output\': \'[4, 5, 1, 2, 3]\', \'explanation\': \'The array [1, 2, 3, 4, 5] rotated to the right by 2 steps becomes [4, 5, 1, 2, 3]\'}, {\'id\': 2, \'input\': \'[1, 2, 3], 4\', \'output\': \'[3, 1, 2]\', \'explanation\': \'The array [1, 2, 3] rotated to the right by 4 steps becomes [3, 1, 2]\'}, {\'id\': 3, \'input\': \'[1, 2, 3, 4, 5, 6, 7], 3\', \'output\': \'[5, 6, 7, 1, 2, 3, 4]\', \'explanation\': \'The array [1, 2, 3, 4, 5, 6, 7] rotated to the right by 3 steps becomes [5, 6, 7, 1, 2, 3, 4]\'}]\"',0,0,'7510a1cd-40f7-4809-9768-947e7b95c72c','2024-07-26 14:16:41','2024-07-26 14:16:41'),('kth_largest_element','Write a function that finds the kth largest element in an unsorted array','nums (list of integers), k (integer)','kth largest element','medium','\"{\'python\': \'def kth_largest_element(nums, k):\\\\n    pass\', \'javascript\': \'exports.kthLargestElement = function (arr, k) {\\\\n    // your code here\\\\n}\'}\"','\"[{\'id\': 1, \'input\': \'[3, 2, 1, 5, 6, 4], 2\', \'output\': \'5\', \'explanation\': \'The 2nd largest element in the array [3, 2, 1, 5, 6, 4] is 5\'}, {\'id\': 2, \'input\': \'[3, 2, 3, 1, 2, 4, 5, 5, 6], 4\', \'output\': \'4\', \'explanation\': \'The 4th largest element in the array [3, 2, 3, 1, 2, 4, 5, 5, 6] is 4\'}, {\'id\': 3, \'input\': \'[-1, 2, 0], 1\', \'output\': \'2\', \'explanation\': \'The 1st largest element in the array [-1, 2, 0] is 2\'}]\"',0,0,'81ed1671-e7fc-4072-8612-a5290d07d5e7','2024-07-26 14:16:41','2024-07-26 14:16:41'),('palindrome','Write a function that checks if a string is a palindrome','s (string)','True if s is a palindrome, False otherwise','easy','\"{\'python\': \'def palindrome(s):\\\\n    pass\', \'javascript\': \'exports.palindrome = function (str) {\\\\n    // your code here\\\\n}\'}\"','\"[{\'id\': 1, \'input\': \'hello\', \'output\': \'False\', \'explanation\': \\\"\'hello\' is not a palindrome\\\"}, {\'id\': 2, \'input\': \'0_0 (: /-\\\\\\\\ :) 0–0\', \'output\': \'True\', \'explanation\': \\\"\'0_0 (: /-\\\\\\\\ :) 0–0\' is a palindrome\\\"}, {\'id\': 3, \'input\': \'madam\', \'output\': \'True\', \'explanation\': \\\"\'madam\' is a palindrome\\\"}]\"',0,0,'99831846-f1d3-4e82-806f-82e7c138c4bd','2024-07-26 14:16:41','2024-07-26 14:16:41'),('merge_intervals','Write a function that merges overlapping intervals','intervals (list of lists)','list of merged intervals','medium','\"{\'python\': \'def merge_intervals(intervals):\\\\n    pass\', \'javascript\': \'exports.mergeIntervals = function (intervals) {\\\\n    // your code here\\\\n}\'}\"','\"[{\'id\': 1, \'input\': \'[[1,3],[2,6],[8,10],[15,18]]\', \'output\': \'[[1,6],[8,10],[15,18]]\', \'explanation\': \'The intervals [[1,3],[2,6],[8,10],[15,18]] can be merged to [[1,6],[8,10],[15,18]]\'}, {\'id\': 2, \'input\': \'[[1,4],[4,5]]\', \'output\': \'[[1,5]]\', \'explanation\': \'The intervals [[1,4],[4,5]] can be merged to [[1,5]]\'}, {\'id\': 3, \'input\': \'[[1,2],[3,5],[6,7],[8,10],[12,16]]\', \'output\': \'[[1,5],[6,7],[8,10],[12,16]]\', \'explanation\': \'The intervals [[1,2],[3,5],[6,7],[8,10],[12,16]] can be merged to [[1,5],[6,7],[8,10],[12,16]]\'}]\"',0,0,'bd43ab39-4ab7-4fa1-b7e5-b8a4eb9fced8','2024-07-26 14:16:41','2024-07-26 14:16:41'),('binary_search','Write a function that performs binary search on a sorted list','nums (sorted list of integers), target (integer)','index of target if found, -1 if not found','medium','\"{\'python\': \'def binary_search(nums, target):\\\\n    pass\', \'javascript\': \'exports.binarySearch = function (arr, target) {\\\\n    // your code here\\\\n}\'}\"','\"[{\'id\': 1, \'input\': \'[1, 2, 3, 4, 5], 3\', \'output\': \'2\', \'explanation\': \'The target number 3 is found at index 2\'}, {\'id\': 2, \'input\': \'[1, 2, 3, 4, 5], 6\', \'output\': \'-1\', \'explanation\': \'The target number 6 is not found in the list\'}, {\'id\': 3, \'input\': \'[1, 3, 5, 7, 9], 5\', \'output\': \'2\', \'explanation\': \'The target number 5 is found at index 2\'}]\"',0,0,'f224c5c3-b04d-4f67-921b-02a99c97a725','2024-07-26 14:16:41','2024-07-26 14:16:41');
/*!40000 ALTER TABLE `challenges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` varchar(20) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `full_name` varchar(60) NOT NULL,
  `badges` varchar(1024) DEFAULT NULL,
  `points` int(11) DEFAULT NULL,
  `starred_challenges` varchar(1024) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `authenticated` tinyint(1) DEFAULT NULL,
  `role` varchar(60) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('MKswe','mk.swe@codyx.com','$2b$12$9NdN8kMEibGVnddIkE.3betyHM4PvC6.98/gXyiZCUmKnLIQ3n8Sm','mk','[]',0,'[]',1,1,'admin','4012b016-c866-4125-80ea-69d8e2e3607e','2024-07-26 01:16:11','2024-07-26 01:16:11');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-26 11:22:21
