/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - evoting
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`evoting` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `evoting`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add course_table',7,'add_course_table'),
(26,'Can change course_table',7,'change_course_table'),
(27,'Can delete course_table',7,'delete_course_table'),
(28,'Can view course_table',7,'view_course_table'),
(29,'Can add electiondate_table',8,'add_electiondate_table'),
(30,'Can change electiondate_table',8,'change_electiondate_table'),
(31,'Can delete electiondate_table',8,'delete_electiondate_table'),
(32,'Can view electiondate_table',8,'view_electiondate_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add electioncoordinator_table',10,'add_electioncoordinator_table'),
(38,'Can change electioncoordinator_table',10,'change_electioncoordinator_table'),
(39,'Can delete electioncoordinator_table',10,'delete_electioncoordinator_table'),
(40,'Can view electioncoordinator_table',10,'view_electioncoordinator_table'),
(41,'Can add nominees_table',11,'add_nominees_table'),
(42,'Can change nominees_table',11,'change_nominees_table'),
(43,'Can delete nominees_table',11,'delete_nominees_table'),
(44,'Can view nominees_table',11,'view_nominees_table'),
(45,'Can add student_table',12,'add_student_table'),
(46,'Can change student_table',12,'change_student_table'),
(47,'Can delete student_table',12,'delete_student_table'),
(48,'Can view student_table',12,'view_student_table'),
(49,'Can add result_table',13,'add_result_table'),
(50,'Can change result_table',13,'change_result_table'),
(51,'Can delete result_table',13,'delete_result_table'),
(52,'Can view result_table',13,'view_result_table'),
(53,'Can add complaint_table',14,'add_complaint_table'),
(54,'Can change complaint_table',14,'change_complaint_table'),
(55,'Can delete complaint_table',14,'delete_complaint_table'),
(56,'Can view complaint_table',14,'view_complaint_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(14,'voteApp','complaint_table'),
(7,'voteApp','course_table'),
(10,'voteApp','electioncoordinator_table'),
(8,'voteApp','electiondate_table'),
(9,'voteApp','login_table'),
(11,'voteApp','nominees_table'),
(13,'voteApp','result_table'),
(12,'voteApp','student_table');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-04-27 08:56:42.992424'),
(2,'auth','0001_initial','2024-04-27 08:56:43.430739'),
(3,'admin','0001_initial','2024-04-27 08:56:43.549745'),
(4,'admin','0002_logentry_remove_auto_add','2024-04-27 08:56:43.556918'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-04-27 08:56:43.563867'),
(6,'contenttypes','0002_remove_content_type_name','2024-04-27 08:56:43.614681'),
(7,'auth','0002_alter_permission_name_max_length','2024-04-27 08:56:43.654770'),
(8,'auth','0003_alter_user_email_max_length','2024-04-27 08:56:43.670464'),
(9,'auth','0004_alter_user_username_opts','2024-04-27 08:56:43.733465'),
(10,'auth','0005_alter_user_last_login_null','2024-04-27 08:56:43.782040'),
(11,'auth','0006_require_contenttypes_0002','2024-04-27 08:56:43.782040'),
(12,'auth','0007_alter_validators_add_error_messages','2024-04-27 08:56:43.790012'),
(13,'auth','0008_alter_user_username_max_length','2024-04-27 08:56:43.840581'),
(14,'auth','0009_alter_user_last_name_max_length','2024-04-27 08:56:43.891337'),
(15,'auth','0010_alter_group_name_max_length','2024-04-27 08:56:43.909301'),
(16,'auth','0011_update_proxy_permissions','2024-04-27 08:56:43.917302'),
(17,'auth','0012_alter_user_first_name_max_length','2024-04-27 08:56:43.961693'),
(18,'sessions','0001_initial','2024-04-27 08:56:44.008286'),
(19,'voteApp','0001_initial','2024-04-27 08:56:44.421807');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('qbrki0uhghlfjh4ng7y6j4szgldl2zxt','eyJlaWQiOjksIm9vIjoxfQ:1s10rS:QB3Q-FQhcFhNjltPVCIttiMA3Za1kYflbR-gNdKLiOI','2024-05-12 09:30:18.336107');

/*Table structure for table `voteapp_complaint_table` */

DROP TABLE IF EXISTS `voteapp_complaint_table`;

CREATE TABLE `voteapp_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(50) NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `voteApp_complaint_ta_STUDENT_id_b9938422_fk_voteApp_s` (`STUDENT_id`),
  CONSTRAINT `voteApp_complaint_ta_STUDENT_id_b9938422_fk_voteApp_s` FOREIGN KEY (`STUDENT_id`) REFERENCES `voteapp_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_complaint_table` */

insert  into `voteapp_complaint_table`(`id`,`complaint`,`date`,`reply`,`STUDENT_id`) values 
(2,'ikkkoojb','2024-04-29','pending',10),
(3,'ikkkoojb','2024-04-29','pending',10);

/*Table structure for table `voteapp_course_table` */

DROP TABLE IF EXISTS `voteapp_course_table`;

CREATE TABLE `voteapp_course_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `course` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_course_table` */

/*Table structure for table `voteapp_electioncoordinator_table` */

DROP TABLE IF EXISTS `voteapp_electioncoordinator_table`;

CREATE TABLE `voteapp_electioncoordinator_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `DOB` date NOT NULL,
  `image` varchar(100) NOT NULL,
  `phone_no` bigint NOT NULL,
  `Email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `voteApp_electioncoor_LOGIN_id_1356cb2d_fk_voteApp_l` (`LOGIN_id`),
  CONSTRAINT `voteApp_electioncoor_LOGIN_id_1356cb2d_fk_voteApp_l` FOREIGN KEY (`LOGIN_id`) REFERENCES `voteapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_electioncoordinator_table` */

insert  into `voteapp_electioncoordinator_table`(`id`,`name`,`DOB`,`image`,`phone_no`,`Email`,`LOGIN_id`) values 
(1,'adhil','2002-07-10','1713408661473_AMCvs4W.png',1234567890,'asd@gmail.com',2);

/*Table structure for table `voteapp_electiondate_table` */

DROP TABLE IF EXISTS `voteapp_electiondate_table`;

CREATE TABLE `voteapp_electiondate_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `post` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `election_date` date NOT NULL,
  `details` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_electiondate_table` */

insert  into `voteapp_electiondate_table`(`id`,`post`,`date`,`election_date`,`details`) values 
(1,'prsident','2024-04-27','2024-04-28','aaz'),
(2,'ward member','2024-04-28','2024-04-30','asdfd');

/*Table structure for table `voteapp_login_table` */

DROP TABLE IF EXISTS `voteapp_login_table`;

CREATE TABLE `voteapp_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_login_table` */

insert  into `voteapp_login_table`(`id`,`username`,`password`,`type`) values 
(1,'ashik','123','student'),
(2,'adhil','222','election_cordinator'),
(3,'adhil','234','student'),
(4,'sharmin','333','student'),
(5,'admin','admin','admin'),
(7,'naveen','naveen','student'),
(11,'jasuu','love','student'),
(12,'ash','234','student'),
(13,'athiraa','athi','student'),
(14,'zenha','123','student'),
(15,'zenha1','123','student');

/*Table structure for table `voteapp_nominees_table` */

DROP TABLE IF EXISTS `voteapp_nominees_table`;

CREATE TABLE `voteapp_nominees_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `ELECTION_DATE_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `voteApp_nominees_tab_STUDENT_id_f55b31c1_fk_voteApp_s` (`STUDENT_id`),
  KEY `voteApp_nominees_tab_ELECTION_DATE_id_74b3f8e7_fk_voteApp_e` (`ELECTION_DATE_id`),
  CONSTRAINT `voteApp_nominees_tab_ELECTION_DATE_id_74b3f8e7_fk_voteApp_e` FOREIGN KEY (`ELECTION_DATE_id`) REFERENCES `voteapp_electiondate_table` (`id`),
  CONSTRAINT `voteApp_nominees_tab_STUDENT_id_f55b31c1_fk_voteApp_s` FOREIGN KEY (`STUDENT_id`) REFERENCES `voteapp_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_nominees_table` */

insert  into `voteapp_nominees_table`(`id`,`date`,`status`,`ELECTION_DATE_id`,`STUDENT_id`) values 
(1,'2024-04-27','rejected',1,1),
(2,'2024-04-27','pending',1,1),
(3,'2024-04-27','accepted',1,3),
(6,'2024-04-29','pending',1,11),
(7,'2024-04-29','rejected',2,11),
(8,'2024-04-29','accepted',2,13);

/*Table structure for table `voteapp_result_table` */

DROP TABLE IF EXISTS `voteapp_result_table`;

CREATE TABLE `voteapp_result_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `vote` int NOT NULL,
  `NOMINEES_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `voteApp_result_table_NOMINEES_id_9fc03e11_fk_voteApp_n` (`NOMINEES_id`),
  KEY `voteApp_result_table_STUDENT_id_f814a8e6_fk_voteApp_s` (`STUDENT_id`),
  CONSTRAINT `voteApp_result_table_NOMINEES_id_9fc03e11_fk_voteApp_n` FOREIGN KEY (`NOMINEES_id`) REFERENCES `voteapp_nominees_table` (`id`),
  CONSTRAINT `voteApp_result_table_STUDENT_id_f814a8e6_fk_voteApp_s` FOREIGN KEY (`STUDENT_id`) REFERENCES `voteapp_student_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_result_table` */

insert  into `voteapp_result_table`(`id`,`vote`,`NOMINEES_id`,`STUDENT_id`) values 
(1,1,1,1),
(2,1,1,3),
(3,1,1,2),
(4,1,3,10),
(5,1,3,11),
(6,1,3,13),
(7,1,8,13);

/*Table structure for table `voteapp_student_table` */

DROP TABLE IF EXISTS `voteapp_student_table`;

CREATE TABLE `voteapp_student_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Fname` varchar(50) NOT NULL,
  `Lname` varchar(50) NOT NULL,
  `DOB` date NOT NULL,
  `gender` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `phone_no` bigint NOT NULL,
  `image` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `voteApp_student_tabl_LOGIN_id_f210dff6_fk_voteApp_l` (`LOGIN_id`),
  CONSTRAINT `voteApp_student_tabl_LOGIN_id_f210dff6_fk_voteApp_l` FOREIGN KEY (`LOGIN_id`) REFERENCES `voteapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_student_table` */

insert  into `voteapp_student_table`(`id`,`Fname`,`Lname`,`DOB`,`gender`,`Email`,`phone_no`,`image`,`LOGIN_id`) values 
(1,'Mohamed','Ashik','2002-08-27','male','asw@gmail.com',9497159770,'IMG_20240327_112446.jpg',1),
(2,'adhil','shinad','2024-04-18','male','adwa@gmail.com',9194971597,'IMG_4170_3ZDzOdQ.HEIC',3),
(3,'sharmin','hameed','2024-04-21','female','aws@gmail.com',9497915480,'IMG_4170_C0MFIaS.HEIC',4),
(5,'naveen','john','1993-04-21','male','naveentjohn@gmail.com',9876543210,'IMG-20240427-WA0003_rtJ4Z3O.jpg',7),
(9,'jasmin','raneesh','2024-04-28','female','jaffarjasmin8@gmail.com',9946088884,'IMG_4170_Fa3MF3Q.HEIC',11),
(10,'ash','mohd','2024-04-26','male','asw@gmail.com',9194971594,'IMG_20240428_165647.jpg',12),
(11,'Athira','Ravi','2024-04-18','female','athirapootheri003@gmail.com',9778235643,'IMG_20240429_093236.jpg',13),
(12,'Fathimath ','Zenha C','2002-06-22','FEMALE','zenha806@gmail.com',9778236806,'10.png',14),
(13,'Fathimath','Zenha','2002-06-22','FEMALE','zenha806@gmail.com',9778236806,'IMG_20240429_121654.jpg',15);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
