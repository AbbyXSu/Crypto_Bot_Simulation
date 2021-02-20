CREATE TABLE IF NOT EXISTS Reports
    (
            id INTEGER NOT NULL AUTO_INCREMENT,
            revenue VARCHAR(30) NOT NULL,
            expense VARCHAR(30) NOT NULL,
            PLtype  VARCHAR(150) NOT NULL,
            income  VARCHAR(150) NOT NULL,
            efficiency_ratio VARCHAR(150) NOT NULL,
            PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `Reports` WRITE;
/*!40000 ALTER TABLE `Reports` DISABLE KEYS */;
INSERT INTO `Reports` VALUES (1,'500','500','breakeven','0','0');
/*!40000 ALTER TABLE `Reports` ENABLE KEYS */;
UNLOCK TABLES;
