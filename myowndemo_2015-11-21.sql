# ************************************************************
# Sequel Pro SQL dump
# Version 4499
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.6.26-log)
# Database: myowndemo
# Generation Time: 2015-11-21 11:47:24 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table education
# ------------------------------------------------------------

DROP TABLE IF EXISTS `education`;

CREATE TABLE `education` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `school` varchar(11) NOT NULL DEFAULT '',
  `major` varchar(11) NOT NULL DEFAULT '',
  `timeRange` varchar(13) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `education` WRITE;
/*!40000 ALTER TABLE `education` DISABLE KEYS */;

INSERT INTO `education` (`id`, `uid`, `school`, `major`, `timeRange`)
VALUES
	(1,1,'中南大学','计算机科学与技术','2009.9-2013'),
	(2,1,'尚志中学','高中','2006.9-2009');

/*!40000 ALTER TABLE `education` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table resume
# ------------------------------------------------------------

DROP TABLE IF EXISTS `resume`;

CREATE TABLE `resume` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `realName` varchar(8) NOT NULL DEFAULT 'NOT NULL',
  `sex` char(1) NOT NULL DEFAULT '',
  `intro` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `resume` WRITE;
/*!40000 ALTER TABLE `resume` DISABLE KEYS */;

INSERT INTO `resume` (`id`, `realName`, `sex`, `intro`)
VALUES
	(1,'于敬晖','M','我是一个python工程师,有三年的工作经验,半吊子C的水平,会一点java,爱谁谁.就问你一句你看');

/*!40000 ALTER TABLE `resume` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table skills
# ------------------------------------------------------------

DROP TABLE IF EXISTS `skills`;

CREATE TABLE `skills` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `skillName` varchar(11) DEFAULT '',
  `skillIntro` varchar(100) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table work
# ------------------------------------------------------------

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `corpName` varchar(11) DEFAULT NULL,
  `vocation` varchar(11) DEFAULT NULL,
  `timeRange` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `work` WRITE;
/*!40000 ALTER TABLE `work` DISABLE KEYS */;

INSERT INTO `work` (`id`, `uid`, `corpName`, `vocation`, `timeRange`)
VALUES
	(1,1,'南方航空','java软件工程师','2013.7-2015.4'),
	(2,1,'鹰漠旅行','python软件工程师','2015.8-至今');

/*!40000 ALTER TABLE `work` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
