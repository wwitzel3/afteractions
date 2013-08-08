-- MySQL dump 10.13  Distrib 5.1.46, for slackware-linux-gnu (x86_64)
--
-- Host: localhost    Database: mssql
-- ------------------------------------------------------
-- Server version	5.1.46-log

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

--
-- Table structure for table `invCategories`
--

DROP TABLE IF EXISTS `invCategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invCategories` (
  `categoryID` tinyint(3) unsigned NOT NULL,
  `categoryName` varchar(100) DEFAULT NULL,
  `description` varchar(3000) DEFAULT NULL,
  `iconID` smallint(6) DEFAULT NULL,
  `published` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`categoryID`),
  KEY `iconID` (`iconID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invCategories`
--

LOCK TABLES `invCategories` WRITE;
/*!40000 ALTER TABLE `invCategories` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `invCategories` VALUES (0,'#System','',NULL,0);
INSERT INTO `invCategories` VALUES (1,'Owner','',NULL,0);
INSERT INTO `invCategories` VALUES (2,'Celestial','',NULL,1);
INSERT INTO `invCategories` VALUES (3,'Station','',NULL,0);
INSERT INTO `invCategories` VALUES (4,'Material','',22,1);
INSERT INTO `invCategories` VALUES (5,'Accessories','',33,1);
INSERT INTO `invCategories` VALUES (6,'Ship','',NULL,1);
INSERT INTO `invCategories` VALUES (7,'Module','',67,1);
INSERT INTO `invCategories` VALUES (8,'Charge','',NULL,1);
INSERT INTO `invCategories` VALUES (9,'Blueprint','',21,1);
INSERT INTO `invCategories` VALUES (10,'Trading','',NULL,0);
INSERT INTO `invCategories` VALUES (11,'Entity','',NULL,0);
INSERT INTO `invCategories` VALUES (14,'Bonus','Character creation bonuses. Like innate skills but genetic rather than learned.',0,0);
INSERT INTO `invCategories` VALUES (16,'Skill','Where all the skills go under.',33,1);
INSERT INTO `invCategories` VALUES (17,'Commodity','',0,1);
INSERT INTO `invCategories` VALUES (18,'Drone','Player owned and controlled drones.',0,1);
INSERT INTO `invCategories` VALUES (20,'Implant','Implant',0,1);
INSERT INTO `invCategories` VALUES (22,'Deployable','',0,1);
INSERT INTO `invCategories` VALUES (23,'Structure','Player owned structure related objects',0,1);
INSERT INTO `invCategories` VALUES (24,'Reaction','',0,1);
INSERT INTO `invCategories` VALUES (25,'Asteroid','',NULL,1);
INSERT INTO `invCategories` VALUES (26,'WorldSpace','Worldspaces and related stuff',NULL,0);
INSERT INTO `invCategories` VALUES (27,'Placeables','Objects that can be fitted inside interiors for practical and decorative purposes',NULL,0);
INSERT INTO `invCategories` VALUES (29,'Abstract','Abstract grouping, global types and groups for the UI, such as Ranks, Ribbons and Medals.',NULL,0);
INSERT INTO `invCategories` VALUES (30,'Apparel','1. clothing, especially outerwear; garments; attire; raiment.\n2. anything that decorates or covers.\n3. superficial appearance; aspect; guise. ',NULL,1);
INSERT INTO `invCategories` VALUES (32,'Subsystem','Subsystems for tech 3 ships',NULL,1);
INSERT INTO `invCategories` VALUES (34,'Ancient Relics','',NULL,1);
INSERT INTO `invCategories` VALUES (35,'Decryptors','',NULL,1);
INSERT INTO `invCategories` VALUES (39,'Infrastructure Upgrades','',NULL,1);
INSERT INTO `invCategories` VALUES (40,'Sovereignty Structures','',NULL,1);
INSERT INTO `invCategories` VALUES (41,'Planetary Interaction','Stuff for planetary interaction',NULL,1);
INSERT INTO `invCategories` VALUES (42,'Planetary Resources','These are Items that can be extracted from a planet. ',NULL,1);
INSERT INTO `invCategories` VALUES (43,'Planetary Commodities','',NULL,1);
INSERT INTO `invCategories` VALUES (49,'Placeables','Placeables are things you can put into rooms. ',NULL,0);
INSERT INTO `invCategories` VALUES (53,'Effects','',NULL,0);
/*!40000 ALTER TABLE `invCategories` ENABLE KEYS */;
UNLOCK TABLES;
commit;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-07-09 16:43:10
