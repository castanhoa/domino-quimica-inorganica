-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: jogo
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Dumping data for table `pecas`
--

LOCK TABLES `pecas` WRITE;
/*!40000 ALTER TABLE `pecas` DISABLE KEYS */;
INSERT INTO `pecas` VALUES (1,'Base','Acido'),(2,'Base','Base'),(3,'Base','Oxido'),(4,'Base','Sal'),(5,'Base','Sal'),(6,'Base','Oxido'),(7,'Base','Base'),(8,'Base','Acido'),(9,'Acido','Acido'),(10,'Acido','Base'),(11,'Acido','Oxido'),(12,'Acido','Sal'),(13,'Acido','Acido'),(14,'Acido','Base'),(15,'Acido','Oxido'),(16,'Acido','Sal'),(17,'Sal','Acido'),(18,'Sal','Base'),(19,'Sal','Sal'),(20,'Sal','Oxido'),(21,'Sal','Acido'),(22,'Sal','Base'),(23,'Sal','Sal'),(24,'Sal','Oxido'),(25,'Oxido','Acido'),(26,'Oxido','Base'),(27,'Oxido','Sal'),(28,'Oxido','Oxido'),(29,'Oxido','Acido'),(30,'Oxido','Base'),(31,'Oxido','Sal'),(32,'Oxido','Oxido');
/*!40000 ALTER TABLE `pecas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-06 11:32:31
