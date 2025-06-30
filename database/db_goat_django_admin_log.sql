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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-05-12 14:10:25.768115','1','Diseas object (1)',1,'[{\"added\": {}}]',7,1),(2,'2025-05-15 09:39:11.355582','2','Diseases object (2)',1,'[{\"added\": {}}]',7,1),(3,'2025-05-15 09:39:53.850748','3','Diseases object (3)',1,'[{\"added\": {}}]',7,1),(4,'2025-05-15 09:40:29.487019','4','Diseases object (4)',1,'[{\"added\": {}}]',7,1),(5,'2025-05-15 09:43:57.284565','5','Diseases object (5)',1,'[{\"added\": {}}]',7,1),(6,'2025-05-16 06:32:31.246724','6','Diseases object (6)',1,'[{\"added\": {}}]',7,1),(7,'2025-05-16 06:34:20.516780','7','Diseases object (7)',1,'[{\"added\": {}}]',7,1),(8,'2025-05-16 06:35:16.075939','8','Diseases object (8)',1,'[{\"added\": {}}]',7,1),(9,'2025-05-16 06:37:12.318420','9','Diseases object (9)',1,'[{\"added\": {}}]',7,1),(10,'2025-05-16 06:38:26.801660','10','Diseases object (10)',1,'[{\"added\": {}}]',7,1),(11,'2025-05-16 06:39:45.440681','11','Diseases object (11)',1,'[{\"added\": {}}]',7,1),(12,'2025-05-16 14:19:22.592532','11','Diseases object (11)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(13,'2025-05-16 14:19:29.440414','11','Diseases object (11)',2,'[]',7,1),(14,'2025-05-16 14:20:33.734005','9','Diseases object (9)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(15,'2025-05-16 14:20:40.317424','9','Diseases object (9)',2,'[]',7,1),(16,'2025-05-16 14:21:04.045795','8','Diseases object (8)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(17,'2025-05-16 14:21:51.239228','7','Diseases object (7)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(18,'2025-05-16 14:22:10.241070','6','Diseases object (6)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(19,'2025-05-16 14:22:34.003474','5','Diseases object (5)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(20,'2025-05-16 14:23:16.079288','4','Diseases object (4)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(21,'2025-05-16 14:23:47.234173','3','Diseases object (3)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(22,'2025-05-16 14:24:07.414220','2','Diseases object (2)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(23,'2025-05-16 14:25:07.999046','1','Diseases object (1)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(24,'2025-05-16 14:26:05.535684','10','Diseases object (10)',2,'[{\"changed\": {\"fields\": [\"Img relative url\"]}}]',7,1),(25,'2025-06-28 01:33:53.990414','12','test (id=12)',1,'[{\"added\": {}}]',7,1),(26,'2025-06-28 01:47:30.690957','12','test (id=12)',3,'',7,1),(27,'2025-06-28 01:49:33.293764','9','โรค พี พี อาร์ (id=9)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(28,'2025-06-28 01:50:49.700122','5','โรคข้ออักเสบ (id=5)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(29,'2025-06-28 01:51:14.334968','7','โรคข้อและสมองอักเสบในแพะ (id=7)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(30,'2025-06-28 01:51:27.929165','6','โรคตาอักเสบ (id=6)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(31,'2025-06-28 01:51:58.367076','11','โรคปอดบวมจากแบคทีเรีย (id=11)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(32,'2025-06-28 01:52:07.011052','11','โรคปอดบวมจากแบคทีเรีย (id=11)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(33,'2025-06-28 01:52:45.769072','2','โรคปากเปื่อยพุพอง (id=2)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(34,'2025-06-28 01:52:55.029691','1','โรคปากและเท้าเปื่อย (id=1)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(35,'2025-06-28 01:53:08.756646','8','โรคผิวหนัง (id=8)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(36,'2025-06-28 01:53:21.340959','10','โรควัณโรค (id=10)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(37,'2025-06-28 01:53:31.027853','4','โรคเมลิออยด์ (id=4)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(38,'2025-06-28 01:53:38.822306','3','โรคแอนแทรกซ์ (id=3)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
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
