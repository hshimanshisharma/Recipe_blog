-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: python_project
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `role` varchar(45) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (2,'Emma','emma@gmail.com','1452369870','12','Super-admin'),(4,'Anna','anna@gmail.com','7419638521','1234','Admin');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `Name` varchar(100) NOT NULL,
  `Description` text,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('abcefg','jcbdskbc'),('demo1','demo1');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `duration` int NOT NULL,
  `ingredients` text NOT NULL,
  `category` varchar(50) NOT NULL,
  `user_id` int NOT NULL,
  `image` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `name_idx` (`category`),
  KEY `id_idx` (`user_id`),
  CONSTRAINT `id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `name` FOREIGN KEY (`category`) REFERENCES `category` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
INSERT INTO `recipe` VALUES (1,'ubj,k','bukj',15,'hbuilgyu','demo1',2,''),(2,'ubgugbk','gibhuil',25,'ygibk,','abcefg',2,''),(4,'Sparkling Mango Pineapple Sangria','Stir pineapple juice, mango juice, pineapple rum, mango rum, chunked pineapple, and mango slices together in a large pitcher. Chill for 2 to 4 hours.\n\nAdd Prosecco before serving. Stir and serve cold.',130,'1/2 cup pineapple juice\n\n1/2 cup mango juice\n\n1/2 cup pineapple rum\n\n1/2 cup mango rum\n\n1/2 fresh pineapple - peeled, cored, and cut into chunks\n\n2 mangos - peeled, seeded, and sliced\n\n1 (750mL) bottle Prosecco sparkling wine','demo1',2,''),(12,'Gold Rush','In a small saucepan, combine honey and water over medium heat. Bring to a simmer, stirring, until honey is dissolved. Remove from heat and cool completely. To account for evaporation, add a splash of water to bring the total volume of syrup up to 3 fluid ounces, if necessary.\n\nAdd 1 cup of ice to a cocktail shaker. Add bourbon, honey syrup and lemon juice. Cover and shake until chilled, 15 to 20 seconds. Fill a rocks glass with remaining ice cubes or 1 large ice sphere and strain cocktail over the ice. Garnish with lemon twist.',26,'2 cups ice\n\n2 fluid ounces bourbon\n\n3/4 fluid ounce honey syrup\n\n3/4 fluid ounce fresh lemon juice\n\nlemon twist, for garnish','demo1',2,'recipy_images/12.png'),(13,'Chocolate Cake','Gather all ingredients.\nPreheat oven to 350 degrees F (175 degrees C). Grease and flour two nine inch round pans.\nAdd the eggs, milk, oil and vanilla, mix for 2 minutes on medium speed of mixer.Stir in the boiling water last. Batter will be thin.\n\n\nIn a large bowl, stir together the sugar, flour, cocoa, baking powder, baking soda and salt.Stir in the boiling water last. Batter will be thin.\n\nPour evenly into the prepared pans.Bake 30 to 35 minutes in the preheated oven, until the cake tests done with a toothpick. Cool in the pans for 10 minutes, then remove to a wire rack to cool completely.',60,'2 cups white sugar\n\n1 ¾ cups all-purpose flour\n\n¾ cup unsweetened cocoa powder\n\n1 ½ teaspoons baking powder\n\n1 ½ teaspoons baking soda\n\n1 teaspoon salt\n\n2 eggs\n\n1 cup milk\n\n½ cup vegetable oil\n\n2 teaspoons vanilla extract\n\n1 cup boiling water','abcefg',2,'recipy_images/13.png'),(14,'White Sauce Pasta','Boil raw pasta according to the instructions given on the package or follow following instructions; Take 4-5 cups water in deep sauce pan, bring it to boil over medium flame. When it start boiling, add 3/4 cup Penne pasta and 1/2 teaspoon salt.Boil them until al-dente (cooked but not very soft). It will take around 10-12 minutes. To check whether pasta is cooked or not, take one pasta in a fork and bite it. If it is little firm to bite, it is cooked. If it is too hard to bite, it requires more cooking.Transfer cooked pasta to a large colander and drain excess water.',15,'3/4 cup Penne Pasta or any Pasta\n1/2 teaspoon Salt\n4-5 cups Water','demo1',2,'recipy_images/14.png'),(15,'Red sauce Pasta','firstly, in a large kadai boil 6 cup water and 1 tsp salt.\nonce the water comes to a boil, add 2 cup pasta. i have used elicoidali pasta, you can alternatively use penne pasta.\nboil for 7 minutes, or until the pasta is cooked al dente.\ndrain off the pasta and keep aside.',20,'2 tbsp olive oil\n▢2 clove garlic, finely chopped\n▢1 onion, finely chopped\n▢1 tsp chilli flakes\n▢1 tsp mixed herbs\n▢¼ tsp pepper powder\n▢½ tsp salt','demo1',2,'recipy_images/15.png');
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `address` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Mehak','mehak@gmail.com','1245369878','1234','FEMALE','eifeihlonhei'),(2,'Kate','kate@gmail.com','1524369870','741','FEMALE','lnfioshiufhin'),(3,'Akash','akash@gmail.com','1523698742','123','MALE','fnhuiawebfl');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-28 16:44:19
