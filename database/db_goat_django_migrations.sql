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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-05-12 13:26:58.684437'),(2,'auth','0001_initial','2025-05-12 13:26:59.732993'),(3,'admin','0001_initial','2025-05-12 13:26:59.980577'),(4,'admin','0002_logentry_remove_auto_add','2025-05-12 13:26:59.991306'),(5,'admin','0003_logentry_add_action_flag_choices','2025-05-12 13:27:00.006695'),(6,'app_goat','0001_initial','2025-05-12 13:27:00.042149'),(7,'app_goat','0002_diseas_cause_diseas_sympton_diseas_title_and_more','2025-05-12 13:27:00.319450'),(8,'contenttypes','0002_remove_content_type_name','2025-05-12 13:27:00.514305'),(9,'auth','0002_alter_permission_name_max_length','2025-05-12 13:27:00.631232'),(10,'auth','0003_alter_user_email_max_length','2025-05-12 13:27:00.683307'),(11,'auth','0004_alter_user_username_opts','2025-05-12 13:27:00.694982'),(12,'auth','0005_alter_user_last_login_null','2025-05-12 13:27:00.793669'),(13,'auth','0006_require_contenttypes_0002','2025-05-12 13:27:00.800728'),(14,'auth','0007_alter_validators_add_error_messages','2025-05-12 13:27:00.817809'),(15,'auth','0008_alter_user_username_max_length','2025-05-12 13:27:00.949081'),(16,'auth','0009_alter_user_last_name_max_length','2025-05-12 13:27:01.046283'),(17,'auth','0010_alter_group_name_max_length','2025-05-12 13:27:01.073937'),(18,'auth','0011_update_proxy_permissions','2025-05-12 13:27:01.086854'),(19,'auth','0012_alter_user_first_name_max_length','2025-05-12 13:27:01.206341'),(20,'sessions','0001_initial','2025-05-12 13:27:01.286922'),(21,'app_goat','0003_rename_diseas_diseases','2025-05-14 13:00:56.109530'),(22,'app_goat','0004_diseases_img_relative_url','2025-05-16 14:08:14.819686'),(23,'app_goat','0005_remove_diseases_img_relative_url_diseases_image','2025-06-28 01:29:53.541449');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
