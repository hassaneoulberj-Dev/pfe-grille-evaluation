-- Structure exportée du serveur MySQL 8.0. Installation neuve uniquement.
CREATE DATABASE IF NOT EXISTS `grille` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `grille`;
CREATE TABLE `enseignant` (
  `id` int NOT NULL,
  `nom` text NOT NULL,
  `prenom` text NOT NULL,
  `date_effet` date DEFAULT NULL,
  `grade` text NOT NULL,
  `type_garde` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
