-- 13 lignes avec noms de démonstration N1/P1, etc.
-- À importer une seule fois dans une table vide, après schema.sql.
SET NAMES utf8mb4;
USE `grille`;
INSERT INTO `enseignant` (`id`,`nom`,`prenom`,`date_effet`,`grade`,`type_garde`) VALUES
(1, 'N1', 'P1', '2020-01-01', 'MCA', 'A to B'),
(2, 'N2', 'P2', '2020-01-02', 'MCA', 'A to B'),
(3, 'N3', 'P3', '2020-01-03', 'MCA', 'B to C'),
(4, 'N4', 'P4', '2020-01-04', 'MCH', 'A to B'),
(5, 'N5', 'P5', '2020-01-05', 'MCH', 'A to B'),
(6, 'N6', 'P6', '2020-01-06', 'MCH', 'B to C'),
(7, 'N7', 'P7', '2020-01-07', 'MCH', 'B to C'),
(8, 'N8', 'P8', '2020-01-08', 'MCH', 'B to C'),
(9, 'N9', 'P9', '2020-01-09', 'PES', 'A to B'),
(10, 'N10', 'P10', '2020-01-10', 'PES', 'A to B'),
(11, 'N11', 'P11', '2020-01-11', 'PES', 'A to B'),
(12, 'N12', 'P12', '2020-01-12', 'PES', 'B to C'),
(13, 'N13', 'P13', '2020-01-13', 'PES', 'C to D');
