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
(37,'Can add nominees_table',10,'add_nominees_table'),
(38,'Can change nominees_table',10,'change_nominees_table'),
(39,'Can delete nominees_table',10,'delete_nominees_table'),
(40,'Can view nominees_table',10,'view_nominees_table'),
(41,'Can add student_table',11,'add_student_table'),
(42,'Can change student_table',11,'change_student_table'),
(43,'Can delete student_table',11,'delete_student_table'),
(44,'Can view student_table',11,'view_student_table'),
(45,'Can add result_table',12,'add_result_table'),
(46,'Can change result_table',12,'change_result_table'),
(47,'Can delete result_table',12,'delete_result_table'),
(48,'Can view result_table',12,'view_result_table'),
(49,'Can add electioncoordinator_table',13,'add_electioncoordinator_table'),
(50,'Can change electioncoordinator_table',13,'change_electioncoordinator_table'),
(51,'Can delete electioncoordinator_table',13,'delete_electioncoordinator_table'),
(52,'Can view electioncoordinator_table',13,'view_electioncoordinator_table'),
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
(13,'voteApp','electioncoordinator_table'),
(8,'voteApp','electiondate_table'),
(9,'voteApp','login_table'),
(10,'voteApp','nominees_table'),
(12,'voteApp','result_table'),
(11,'voteApp','student_table');

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
(1,'contenttypes','0001_initial','2024-03-22 04:22:02.657506'),
(2,'auth','0001_initial','2024-03-22 04:22:03.183269'),
(3,'admin','0001_initial','2024-03-22 04:22:03.302060'),
(4,'admin','0002_logentry_remove_auto_add','2024-03-22 04:22:03.318202'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-03-22 04:22:03.318202'),
(6,'contenttypes','0002_remove_content_type_name','2024-03-22 04:22:03.397082'),
(7,'auth','0002_alter_permission_name_max_length','2024-03-22 04:22:03.443953'),
(8,'auth','0003_alter_user_email_max_length','2024-03-22 04:22:03.475333'),
(9,'auth','0004_alter_user_username_opts','2024-03-22 04:22:03.491272'),
(10,'auth','0005_alter_user_last_login_null','2024-03-22 04:22:03.553926'),
(11,'auth','0006_require_contenttypes_0002','2024-03-22 04:22:03.553926'),
(12,'auth','0007_alter_validators_add_error_messages','2024-03-22 04:22:03.570251'),
(13,'auth','0008_alter_user_username_max_length','2024-03-22 04:22:03.647868'),
(14,'auth','0009_alter_user_last_name_max_length','2024-03-22 04:22:03.710373'),
(15,'auth','0010_alter_group_name_max_length','2024-03-22 04:22:03.726745'),
(16,'auth','0011_update_proxy_permissions','2024-03-22 04:22:03.726745'),
(17,'auth','0012_alter_user_first_name_max_length','2024-03-22 04:22:03.789342'),
(18,'sessions','0001_initial','2024-03-22 04:22:03.820509'),
(19,'voteApp','0001_initial','2024-03-22 04:22:04.132977');

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
('a32gwb8xwxji5w2hbcj3z1fu5iwau30o','eyJlaWQiOjEsIm9vIjo3fQ:1rsGDx:xvufg--QtSwLzcwZa_Sn0kv6-QtAFtzkgyJv_e-HsPA','2024-04-18 06:05:21.831119');

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_complaint_table` */

insert  into `voteapp_complaint_table`(`id`,`complaint`,`date`,`reply`,`STUDENT_id`) values 
(7,'afsr','2024-04-04',';;',4),
(8,'fgffbv','2024-04-05','pending',4);

/*Table structure for table `voteapp_course_table` */

DROP TABLE IF EXISTS `voteapp_course_table`;

CREATE TABLE `voteapp_course_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `course` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_course_table` */

insert  into `voteapp_course_table`(`id`,`course`,`description`) values 
(1,'information technology','abc'),
(2,'qwe','asdf');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_electioncoordinator_table` */

insert  into `voteapp_electioncoordinator_table`(`id`,`name`,`DOB`,`image`,`phone_no`,`Email`,`LOGIN_id`) values 
(1,'zenha','2002-06-22','Screenshot 2023-09-19 093040_PBc56QI.png',1234567890,'zzzz@gmail.com',2),
(2,'ashik','2024-02-28','2n_Jp33PNR.png',1234567899,'zzz@gmail.com',3);

/*Table structure for table `voteapp_electiondate_table` */

DROP TABLE IF EXISTS `voteapp_electiondate_table`;

CREATE TABLE `voteapp_electiondate_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `post` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `election_date` date NOT NULL,
  `details` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_electiondate_table` */

insert  into `voteapp_electiondate_table`(`id`,`post`,`date`,`election_date`,`details`) values 
(1,'abcc','2024-03-01','2024-03-02','details');

/*Table structure for table `voteapp_login_table` */

DROP TABLE IF EXISTS `voteapp_login_table`;

CREATE TABLE `voteapp_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_login_table` */

insert  into `voteapp_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'azz','zzz','election_cordinator'),
(3,'azo','asdf','election_cordinator'),
(4,'re','875','student'),
(6,'asw','12345','student'),
(10,'aqa','122','student'),
(11,'wer','1234','student');

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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_nominees_table` */

insert  into `voteapp_nominees_table`(`id`,`date`,`status`,`ELECTION_DATE_id`,`STUDENT_id`) values 
(3,'2024-03-01','rejected',1,1),
(9,'2024-04-04','rejected',1,4),
(10,'2024-04-04','rejected',1,4),
(11,'2024-04-04','pending',1,4),
(12,'2024-04-04','pending',1,4),
(13,'2024-04-04','pending',1,4),
(14,'2024-04-05','accepted',1,4),
(15,'2024-04-05','accepted',1,4),
(16,'2024-04-05','pending',1,4),
(17,'2024-04-05','pending',1,4),
(18,'2024-04-05','pending',1,4),
(19,'2024-04-05','pending',1,4),
(20,'2024-04-05','pending',1,5);

/*Table structure for table `voteapp_result_table` */

DROP TABLE IF EXISTS `voteapp_result_table`;

CREATE TABLE `voteapp_result_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `vote` int NOT NULL,
  `NOMINEES_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `voteApp_result_table_NOMINEES_id_9fc03e11_fk_voteApp_n` (`NOMINEES_id`),
  CONSTRAINT `voteApp_result_table_NOMINEES_id_9fc03e11_fk_voteApp_n` FOREIGN KEY (`NOMINEES_id`) REFERENCES `voteapp_nominees_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_result_table` */

insert  into `voteapp_result_table`(`id`,`vote`,`NOMINEES_id`) values 
(1,100,9),
(2,1,9),
(3,1,9),
(4,1,14),
(5,1,9),
(6,1,9),
(7,1,9),
(8,1,14),
(9,1,14),
(10,1,14),
(11,1,14),
(12,1,14),
(13,1,14),
(14,1,14),
(15,1,14);

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `voteapp_student_table` */

insert  into `voteapp_student_table`(`id`,`Fname`,`Lname`,`DOB`,`gender`,`Email`,`phone_no`,`image`,`LOGIN_id`) values 
(1,'ashik','abc','2024-02-29','female','jjgg@gmail.com',2345656789,' ddd',4),
(4,'mohamed ','ashik','2024-04-04','male','a@gmail.com',311646790,'Screenshot_2024-04-01-13-44-53-486_com.example.evoting.jpg',10),
(5,'athira','pp','2024-04-14','female','asa@gmail.com',6449941594,'IMG_0348.JPG',11);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
