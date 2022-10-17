/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.6.7-MariaDB : Database - restaurantmanagement
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`restaurantmanagement` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;

USE `restaurantmanagement`;

/*Table structure for table `carttable` */

DROP TABLE IF EXISTS `carttable`;

CREATE TABLE `carttable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `foodname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;

/*Data for the table `carttable` */

insert  into `carttable`(`id`,`email`,`foodname`) values 
(24,'aaa@gmail.com','Caesar Selections');

/*Table structure for table `checkouttable` */

DROP TABLE IF EXISTS `checkouttable`;

CREATE TABLE `checkouttable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `foodname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

/*Data for the table `checkouttable` */

/*Table structure for table `restable` */

DROP TABLE IF EXISTS `restable`;

CREATE TABLE `restable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;

/*Data for the table `restable` */

insert  into `restable`(`id`,`name`,`price`,`url`) values 
(1,'Lobster Bisque',5.95,'assets/img/menu/lobster-bisque.jpg'),
(2,'Crab Cake',7.95,'assets/img/menu/cake.jpg'),
(3,'Tuscan',9.95,'assets/img/menu/tuscan-grilled.jpg'),
(4,'Greek Salad',9.95,'assets/img/menu/greek-salad.jpg'),
(5,'Lobster Roll',12.95,'assets/img/menu/lobster-roll.jpg'),
(6,'Bread Barrel',6.95,'assets/img/menu/bread-barrel.jpg'),
(7,'Caesar Selections',8.95,'assets/img/menu/caesar.jpg'),
(8,'Mozzarella Stick',4.95,'assets/img/menu/mozzarella.jpg'),
(9,'Spinash Salad',9.95,'assets/img/menu/spinach-salad.jpg');

/*Table structure for table `usertable` */

DROP TABLE IF EXISTS `usertable`;

CREATE TABLE `usertable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  `budget` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

/*Data for the table `usertable` */

insert  into `usertable`(`id`,`email`,`password`,`role`,`budget`) values 
(1,'aaa@gmail.com','aaa',1,700),
(2,'bbb@gmail.com','zzz',1,300),
(3,'ccc@gmail.com','zzz',1,500);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
