-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: db_goat
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('brlw2a35svenzg72xti4aqw098po9hj5','.eJxVjLsOAiEQAP-F2hBei8HS3m8gC7vIqYHkuKuM_25IrtB2ZjJvEXHfatwHr3EhcRFanH5ZwvzkNgU9sN27zL1t65LkTORhh7x14tf1aP8GFUedW1Y-sAJA7RIkBQ4wsGWvAriM2lPwkEAXyMYYsomssYpsKGgK27P4fAHHOTdf:1uETdr:ASDZ5FCz7FmTSW2jsCOeFSrHnCYX4DrVFpQB2ZIfblA','2025-05-26 13:56:27.630531'),('f93244sljwnrh0suu8q6ybvxgatztdxp','.eJxVjLsOAiEQAP-F2hBei8HS3m8gC7vIqYHkuKuM_25IrtB2ZjJvEXHfatwHr3EhcRFanH5ZwvzkNgU9sN27zL1t65LkTORhh7x14tf1aP8GFUedW1Y-sAJA7RIkBQ4wsGWvAriM2lPwkEAXyMYYsomssYpsKGgK27P4fAHHOTdf:1uKHRZ:D_1Jvw8U5p5ZC2g_YcBmeCOaIgs4g286r7KWd0BzS-A','2025-06-11 14:07:45.891405'),('rcgbhumiod2uaxxgy9okfl2dad61glu8','.eJxVjLsOAiEQAP-F2hBei8HS3m8gC7vIqYHkuKuM_25IrtB2ZjJvEXHfatwHr3EhcRFanH5ZwvzkNgU9sN27zL1t65LkTORhh7x14tf1aP8GFUedW1Y-sAJA7RIkBQ4wsGWvAriM2lPwkEAXyMYYsomssYpsKGgK27P4fAHHOTdf:1uVJmp:27HDYb6iewfVU_sNmQYNCP85ZS_ehjZNcitsciwJnjs','2025-07-12 00:51:19.931120');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-30 19:25:18
