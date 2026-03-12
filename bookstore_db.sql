-- MySQL dump 10.13  Distrib 8.0.45, for macos15 (arm64)
--
-- Host: 127.0.0.1    Database: bookstore_db
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book_genres`
--

DROP TABLE IF EXISTS `book_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_genres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `type` enum('fiction','non-fiction') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_genres`
--

LOCK TABLES `book_genres` WRITE;
/*!40000 ALTER TABLE `book_genres` DISABLE KEYS */;
INSERT INTO `book_genres` VALUES (1,'Self-Improvement','non-fiction'),(2,'Biography','non-fiction'),(3,'History','non-fiction'),(4,'Technology','non-fiction'),(5,'Religion','non-fiction'),(6,'Fantasy','fiction'),(7,'Sci-Fi','fiction'),(8,'Romance','fiction'),(9,'Thriller','fiction'),(10,'Crime','fiction'),(11,'Textbook','non-fiction'),(12,'Business & Economics','non-fiction'),(13,'Health & Fitness','non-fiction'),(14,'Travel','non-fiction'),(15,'Cooking','non-fiction'),(16,'Computer Science','non-fiction'),(17,'Adventure','fiction'),(18,'Automotive','non-fiction'),(19,'Psychology','non-fiction'),(20,'Productivity','non-fiction'),(21,'Philosophy','non-fiction'),(22,'Children','fiction'),(23,'Young Adult','fiction'),(24,'Finance','non-fiction');
/*!40000 ALTER TABLE `book_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_sales`
--

DROP TABLE IF EXISTS `book_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_sales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `book_id` int NOT NULL,
  `branch_id` int NOT NULL,
  `transaction_date` date NOT NULL,
  `quantity` int NOT NULL,
  `sales` float DEFAULT NULL,
  `redeemed_points` float DEFAULT NULL,
  `payment_method` enum('cash','debit_card','credit_card','ewallet','qris','point_redemption') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `fk_book_sales_book` (`book_id`),
  KEY `fk_book_sales_branch` (`branch_id`),
  CONSTRAINT `book_sales_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_book_sales_book` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
  CONSTRAINT `fk_book_sales_branch` FOREIGN KEY (`branch_id`) REFERENCES `branches` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=138 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_sales`
--

LOCK TABLES `book_sales` WRITE;
/*!40000 ALTER TABLE `book_sales` DISABLE KEYS */;
INSERT INTO `book_sales` VALUES (3,12,1,1,'2026-03-09',1,249000,0,'qris'),(4,12,2,1,'2026-03-09',1,599000,0,'qris'),(6,NULL,1,1,'2026-03-09',1,249000,0,'cash'),(7,NULL,6,2,'2026-03-09',1,349000,0,'debit_card'),(8,12,8,2,'2026-03-09',1,0,649,'point_redemption'),(9,NULL,7,1,'2026-03-09',1,389000,0,'ewallet'),(10,1,2,1,'2026-03-09',1,599000,0,'cash'),(11,13,10,1,'2026-03-10',1,319000,0,'qris'),(12,14,11,1,'2026-03-10',1,189000,0,'cash'),(13,15,12,6,'2026-03-10',1,429000,0,'credit_card'),(14,16,15,2,'2026-03-10',1,499000,0,'debit_card'),(15,17,16,7,'2026-03-10',1,799000,0,'qris'),(16,18,17,3,'2026-03-10',1,529000,0,'ewallet'),(17,19,18,11,'2026-03-10',2,518000,0,'cash'),(18,20,20,8,'2026-03-10',1,299000,0,'qris'),(19,NULL,11,9,'2026-03-10',1,189000,0,'cash'),(20,NULL,7,1,'2026-03-10',1,389000,0,'debit_card'),(21,12,10,2,'2026-03-11',1,319000,0,'ewallet'),(22,13,14,6,'2026-03-11',1,399000,0,'qris'),(23,14,15,17,'2026-03-11',1,499000,0,'credit_card'),(24,15,19,12,'2026-03-11',1,349000,0,'cash'),(25,16,20,18,'2026-03-11',1,299000,0,'qris'),(26,17,21,16,'2026-03-11',1,279000,0,'debit_card'),(27,18,1,2,'2026-03-11',1,249000,0,'point_redemption'),(28,19,10,14,'2026-03-11',1,319000,0,'cash'),(29,NULL,18,11,'2026-03-11',1,259000,0,'ewallet'),(30,NULL,13,4,'2026-03-11',1,179000,0,'cash'),(31,20,11,15,'2026-03-12',2,378000,0,'qris'),(32,12,12,7,'2026-03-12',1,429000,0,'credit_card'),(33,13,16,10,'2026-03-12',1,799000,0,'debit_card'),(34,14,17,14,'2026-03-12',1,529000,0,'ewallet'),(35,15,20,8,'2026-03-12',1,0,299,'point_redemption'),(36,12,1,1,'2026-01-03',1,249000,0,'qris'),(37,1,2,1,'2026-01-03',1,599000,0,'cash'),(38,NULL,7,1,'2026-01-04',1,389000,0,'ewallet'),(39,13,10,1,'2026-01-05',1,319000,0,'debit_card'),(40,14,11,2,'2026-01-10',1,189000,0,'qris'),(41,15,12,6,'2026-01-10',1,429000,0,'credit_card'),(42,NULL,5,1,'2026-01-11',1,369000,0,'cash'),(43,16,15,2,'2026-01-12',1,499000,0,'debit_card'),(44,17,16,7,'2026-01-17',1,799000,0,'qris'),(45,NULL,3,7,'2026-01-18',1,249000,0,'cash'),(46,18,17,3,'2026-01-19',1,529000,0,'ewallet'),(47,19,18,11,'2026-01-20',2,518000,0,'cash'),(48,20,20,8,'2026-01-24',1,299000,0,'qris'),(49,NULL,9,1,'2026-01-25',1,259000,0,'debit_card'),(50,12,10,2,'2026-01-26',1,319000,0,'ewallet'),(51,13,14,6,'2026-01-27',1,399000,0,'qris'),(52,14,15,3,'2026-01-29',1,499000,0,'credit_card'),(53,NULL,6,2,'2026-01-30',1,349000,0,'cash'),(54,15,19,12,'2026-01-30',1,349000,0,'qris'),(55,16,1,9,'2026-01-31',1,249000,0,'point_redemption'),(56,12,2,1,'2026-02-02',1,599000,0,'qris'),(57,NULL,7,1,'2026-02-03',1,389000,0,'cash'),(58,13,10,14,'2026-02-04',1,319000,0,'debit_card'),(59,14,11,9,'2026-02-08',1,189000,0,'ewallet'),(60,15,12,7,'2026-02-09',1,429000,0,'credit_card'),(61,NULL,5,1,'2026-02-10',1,369000,0,'cash'),(62,16,15,3,'2026-02-15',1,499000,0,'qris'),(63,17,16,10,'2026-02-16',1,799000,0,'debit_card'),(64,NULL,3,7,'2026-02-17',1,249000,0,'cash'),(65,18,17,14,'2026-02-22',1,529000,0,'ewallet'),(66,19,18,11,'2026-02-23',1,259000,0,'cash'),(67,20,20,8,'2026-02-24',1,299000,0,'qris'),(68,NULL,1,1,'2026-02-26',1,249000,0,'cash'),(69,12,10,2,'2026-02-27',1,319000,0,'ewallet'),(70,13,14,6,'2026-02-28',1,399000,0,'qris'),(71,1,1,1,'2025-01-05',1,249000,0,'cash'),(72,12,2,1,'2025-01-12',1,599000,0,'qris'),(73,NULL,7,1,'2025-01-20',1,389000,0,'ewallet'),(74,13,10,2,'2025-02-03',1,319000,0,'debit_card'),(75,14,11,9,'2025-02-11',1,189000,0,'cash'),(76,NULL,5,1,'2025-02-22',1,369000,0,'qris'),(77,15,12,6,'2025-03-07',1,429000,0,'credit_card'),(78,16,15,3,'2025-03-15',1,499000,0,'debit_card'),(79,NULL,3,7,'2025-03-28',1,249000,0,'cash'),(80,17,16,10,'2025-04-04',1,799000,0,'qris'),(81,18,17,14,'2025-04-13',1,529000,0,'ewallet'),(82,NULL,9,1,'2025-04-25',1,259000,0,'cash'),(83,19,18,11,'2025-05-06',2,518000,0,'cash'),(84,20,20,8,'2025-05-14',1,299000,0,'qris'),(85,NULL,6,2,'2025-05-27',1,349000,0,'debit_card'),(86,1,4,1,'2025-06-02',1,329000,0,'cash'),(87,12,1,2,'2025-06-18',1,249000,0,'ewallet'),(88,NULL,7,1,'2025-06-29',1,389000,0,'qris'),(89,13,10,14,'2025-07-05',1,319000,0,'debit_card'),(90,14,14,6,'2025-07-16',1,399000,0,'qris'),(91,NULL,2,1,'2025-07-30',1,599000,0,'cash'),(92,15,15,2,'2025-08-03',1,499000,0,'credit_card'),(93,16,19,12,'2025-08-19',1,349000,0,'cash'),(94,NULL,1,9,'2025-08-27',1,249000,0,'ewallet'),(95,17,16,7,'2025-09-09',1,799000,0,'qris'),(96,18,17,3,'2025-09-17',1,529000,0,'debit_card'),(97,NULL,5,1,'2025-09-26',1,369000,0,'cash'),(98,19,11,15,'2025-10-04',1,189000,0,'qris'),(99,20,12,7,'2025-10-15',1,429000,0,'credit_card'),(100,NULL,9,1,'2025-10-28',1,259000,0,'cash'),(101,1,3,7,'2025-11-06',1,249000,0,'ewallet'),(102,12,10,2,'2025-11-18',1,319000,0,'qris'),(103,NULL,20,8,'2025-11-29',1,299000,0,'cash'),(104,13,14,6,'2025-12-03',1,399000,0,'credit_card'),(105,14,15,17,'2025-12-12',1,499000,0,'debit_card'),(106,NULL,7,1,'2025-12-27',1,389000,0,'ewallet'),(107,21,22,1,'2025-07-08',1,329000,0,'qris'),(108,22,23,6,'2025-07-15',1,279000,0,'cash'),(109,NULL,24,4,'2025-07-27',1,219000,0,'ewallet'),(110,23,25,1,'2025-08-05',1,289000,0,'debit_card'),(111,24,26,2,'2025-08-17',1,559000,0,'credit_card'),(112,NULL,29,3,'2025-08-28',1,589000,0,'cash'),(113,25,27,7,'2025-09-04',1,829000,0,'qris'),(114,26,28,2,'2025-09-12',1,589000,0,'debit_card'),(115,NULL,30,11,'2025-09-25',1,359000,0,'cash'),(116,27,31,8,'2025-10-06',1,199000,0,'ewallet'),(117,28,22,14,'2025-10-18',1,329000,0,'qris'),(118,NULL,23,15,'2025-10-29',1,279000,0,'cash'),(119,29,26,3,'2025-11-07',1,559000,0,'credit_card'),(120,30,27,10,'2025-11-15',1,829000,0,'debit_card'),(121,NULL,28,6,'2025-11-26',1,589000,0,'cash'),(122,21,29,12,'2025-12-05',1,589000,0,'qris'),(123,22,30,18,'2025-12-17',1,359000,0,'ewallet'),(124,NULL,31,13,'2025-12-28',1,199000,0,'cash'),(125,23,22,2,'2026-01-06',1,329000,0,'qris'),(126,24,23,6,'2026-01-11',1,279000,0,'cash'),(127,25,26,17,'2026-01-19',1,559000,0,'debit_card'),(128,NULL,30,11,'2026-01-24',1,359000,0,'ewallet'),(129,26,27,16,'2026-02-04',1,829000,0,'credit_card'),(130,27,28,14,'2026-02-10',1,589000,0,'qris'),(131,NULL,24,5,'2026-02-21',1,219000,0,'cash'),(132,28,31,8,'2026-02-26',1,199000,0,'debit_card'),(133,29,22,1,'2026-03-10',1,329000,0,'qris'),(134,30,26,2,'2026-03-10',1,559000,0,'credit_card'),(135,NULL,29,3,'2026-03-11',1,589000,0,'cash'),(136,21,30,18,'2026-03-11',1,359000,0,'ewallet'),(137,22,31,13,'2026-03-12',1,0,199,'point_redemption');
/*!40000 ALTER TABLE `book_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_stocks`
--

DROP TABLE IF EXISTS `book_stocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_stocks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `branch_id` int NOT NULL,
  `stock` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_book_stocks_branch` (`branch_id`),
  KEY `fk_book_stocks_book` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_stocks`
--

LOCK TABLES `book_stocks` WRITE;
/*!40000 ALTER TABLE `book_stocks` DISABLE KEYS */;
INSERT INTO `book_stocks` VALUES (1,1,1,18),(2,1,2,20),(3,2,1,18),(4,5,1,10),(5,7,1,7),(7,8,2,4),(8,8,3,5),(9,1,9,5),(10,6,2,4),(12,3,7,10),(13,10,1,8),(14,10,2,10),(15,10,14,7),(16,11,1,12),(17,11,9,10),(18,11,15,8),(19,12,6,6),(20,12,7,8),(21,12,16,5),(22,13,4,9),(23,13,5,7),(24,14,2,6),(25,14,6,8),(26,15,2,9),(27,15,3,7),(28,15,17,6),(29,16,7,4),(30,16,10,5),(31,17,3,8),(32,17,14,6),(33,18,11,10),(34,19,12,9),(35,20,8,15),(36,20,18,10),(37,21,16,6),(38,22,1,10),(39,22,2,12),(40,22,14,8),(41,23,6,9),(42,23,15,7),(43,24,4,8),(44,24,5,6),(45,25,1,7),(46,25,9,5),(47,26,2,11),(48,26,3,9),(49,26,17,6),(50,27,7,5),(51,27,10,7),(52,27,16,4),(53,28,2,8),(54,28,6,7),(55,28,14,5),(56,29,3,6),(57,29,12,8),(58,30,11,9),(59,30,18,7),(60,31,8,10),(61,31,13,6);
/*!40000 ALTER TABLE `book_stocks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `genre_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` decimal(12,2) NOT NULL,
  `author` varchar(255) NOT NULL,
  `reserved_stock` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `fk_books_genre` (`genre_id`),
  CONSTRAINT `fk_books_genre` FOREIGN KEY (`genre_id`) REFERENCES `book_genres` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,1,'Atomic Habits',249000.00,'James Clear',45),(2,2,'Elon Musk',599000.00,'Walter Isaacson',20),(3,1,'Ego is the Enemy',249000.00,'Ryan Holiday',40),(4,1,'Stillness is the Key',329000.00,'Ryan Holiday',65),(5,12,'The Psychology of Money',369000.00,'Morgan Housel',18),(6,12,'The Personal MBA',349000.00,'Josh Kaufman',20),(7,17,'The Alchemist',389000.00,'Paula Coelho',42),(8,16,'Introduction To Machine Learning With Python',649000.00,'Andreas C. Muller, Sarah Guido',20),(9,8,'A Little Life',259000.00,'Hanya Yanagihara',100),(10,20,'Deep Work',319000.00,'Cal Newport',50),(11,24,'Rich Dad Poor Dad',189000.00,'Robert T. Kiyosaki',60),(12,24,'The Intelligent Investor',429000.00,'Benjamin Graham',35),(13,21,'Meditations',179000.00,'Marcus Aurelius',40),(14,19,'Thinking, Fast and Slow',399000.00,'Daniel Kahneman',30),(15,16,'Clean Code',499000.00,'Robert C. Martin',45),(16,16,'Designing Data-Intensive Applications',799000.00,'Martin Kleppmann',25),(17,4,'Grokking Algorithms',529000.00,'Aditya Bhargava',40),(18,23,'The Hunger Games',259000.00,'Suzanne Collins',55),(19,7,'Dune',349000.00,'Frank Herbert',38),(20,22,'Harry Potter and the Sorcerer\'s Stone',299000.00,'J. K. Rowling',70),(21,18,'How Cars Work',279000.00,'Tom Newton',20),(22,20,'The 7 Habits of Highly Effective People',329000.00,'Stephen R. Covey',48),(23,24,'The Millionaire Next Door',279000.00,'Thomas J. Stanley',36),(24,21,'Letters from a Stoic',219000.00,'Seneca',32),(25,19,'Atomic Focus',289000.00,'Marco Ellis',28),(26,16,'Python Crash Course',559000.00,'Eric Matthes',40),(27,16,'Hands-On Machine Learning',829000.00,'Aurelien Geron',26),(28,4,'System Design Interview',589000.00,'Alex Xu',34),(29,7,'Project Hail Mary',359000.00,'Andy Weir',30),(30,23,'The Fault in Our Stars',239000.00,'John Green',42),(31,22,'Charlotte\'s Web',199000.00,'E. B. White',24);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branches`
--

DROP TABLE IF EXISTS `branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branches` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `province` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `address` (`address`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branches`
--

LOCK TABLES `branches` WRITE;
/*!40000 ALTER TABLE `branches` DISABLE KEYS */;
INSERT INTO `branches` VALUES (1,'Maxi Jagakarsa','Jl. Moh. Kahfi 1 No. 121','Jakarta Selatan','DKI Jakarta'),(2,'Maxi Cipete','Jl. Cipete Raya No. 67','Jakarta Selatan','DKI Jakarta'),(3,'Maxi Lebak Bulus','Jl. Lebak Bulus Raya No. 33A','Jakarta Selatan','DKI Jakarta'),(4,'Maxi Kemang','Jl. Kemang Timur Raya No. 71C','Jakarta Selatan','DKI Jakarta'),(5,'Maxi Kemanggisan','Jl. K.H. Syahdan No. 129F','Jakarta Barat','DKI Jakarta'),(6,'Maxi Menteng','Jl. Teuku Cik Ditiro No. 441','Jakarta Pusat','DKI Jakarta'),(7,'Maxi Plus Kuningan City','Kuningan City GF 56-58, Jl. Prof. Dr. Satrio No, 18','Jakarta Selatan','DKI Jakarta'),(8,'Maxi Palembang','Jl. Kolonel Atmo No. 1221','Palembang','Sumatera Selatan'),(9,'Maxi Bogor','Jl. Papandayan No. 79','Kota Bogor','Jawa Barat'),(10,'Maxi Gading Serpong','Ruko San Lorenzo Kav. 12-13, Jl. Gading Serpong Boulevard','Kabupaten Tangerang','Banten'),(11,'Maxi Yogyakarta','Jl. Letjen Suprapto No. 50R','Yogyakarta','DI Yogyakarta'),(12,'Maxi Bandung','Jl. Otto Iskandardinata No. 14','Kota Bandung','Jawa Barat'),(13,'Maxi Pejaten','Jl. Pejaten Barat No. 200','Jakarta Selatan','DKI Jakarta'),(14,'Maxi Depok','Jl. Margonda Raya No. 88','Depok','Jawa Barat'),(15,'Maxi Bekasi','Jl. Ahmad Yani No. 21','Kota Bekasi','Jawa Barat'),(16,'Maxi Surabaya','Jl. Raya Darmo No. 101','Surabaya','Jawa Timur'),(17,'Maxi Semarang','Jl. Pandanaran No. 55','Semarang','Jawa Tengah'),(18,'Maxi Medan','Jl. Gatot Subroto No. 77','Medan','Sumatera Utara');
/*!40000 ALTER TABLE `branches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `points` float DEFAULT '0',
  `tier` enum('bronze','silver','gold','platinum','diamond') NOT NULL DEFAULT 'bronze',
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_number` (`phone_number`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Andi Pratama','081234567801',599,'bronze','andi.pratama@email.com'),(2,'Budi Santoso','081234567802',0,'bronze','budi.santoso@email.com'),(3,'Citra Lestari','081234567803',0,'bronze','citra.lestari@email.com'),(4,'Dimas Saputra','081234567804',0,'bronze','dimas.saputra@email.com'),(5,'Eka Wulandari','081234567805',0,'bronze','eka.wulandari@email.com'),(6,'Farhan Akbar','081234567806',0,'bronze','farhan.akbar@email.com'),(7,'Gita Permata','081234567807',0,'bronze','gita.permata@email.com'),(8,'Hendra Wijaya','081234567808',0,'bronze','hendra.wijaya@email.com'),(9,'Indah Sari','081234567809',0,'bronze','indah.sari@email.com'),(10,'Joko Susilo','081234567810',0,'bronze','joko.susilo@email.com'),(12,'Alif Rahmadian','08127199238',199,'bronze','alifrah78@gmail.com'),(13,'Karin Putri','081234567811',120,'bronze','karin.putri@email.com'),(14,'Lutfi Ramadhan','081234567812',850,'silver','lutfi.ramadhan@email.com'),(15,'Mira Ananda','081234567813',1500,'gold','mira.ananda@email.com'),(16,'Naufal Hidayat','081234567814',300,'bronze','naufal.hidayat@email.com'),(17,'Putra Mahendra','081234567815',2400,'platinum','putra.mahendra@email.com'),(18,'Rania Salsabila','081234567816',700,'silver','rania.salsabila@email.com'),(19,'Taufik Akbar','081234567817',50,'bronze','taufik.akbar@email.com'),(20,'Vina Maharani','081234567818',5200,'diamond','vina.maharani@email.com'),(21,'Bagas Pranoto','081234567819',90,'bronze','bagas.pranoto@email.com'),(22,'Claudia Felicia','081234567820',1250,'gold','claudia.felicia@email.com'),(23,'Daffa Maulana','081234567821',430,'bronze','daffa.maulana@email.com'),(24,'Elsa Nathania','081234567822',980,'silver','elsa.nathania@email.com'),(25,'Fikri Hanan','081234567823',2750,'platinum','fikri.hanan@email.com'),(26,'Gracia Valencia','081234567824',640,'silver','gracia.valencia@email.com'),(27,'Haidar Rizqullah','081234567825',110,'bronze','haidar.rizqullah@email.com'),(28,'Intan Maharani','081234567826',5100,'diamond','intan.maharani@email.com'),(29,'Jason Gunawan','081234567827',150,'bronze','jason.gunawan@email.com'),(30,'Kayla Putri','081234567828',1750,'gold','kayla.putri@email.com');
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

-- Dump completed on 2026-03-12 18:30:16
