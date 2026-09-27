/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - aicybershield_new
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`aicybershield_new` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `aicybershield_new`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

insert  into `auth_group`(`id`,`name`) values 
(1,'admin'),
(2,'Expert'),
(3,'User');

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
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
(25,'Can add chat_table',7,'add_chat_table'),
(26,'Can change chat_table',7,'change_chat_table'),
(27,'Can delete chat_table',7,'delete_chat_table'),
(28,'Can view chat_table',7,'view_chat_table'),
(29,'Can add expert_table',8,'add_expert_table'),
(30,'Can change expert_table',8,'change_expert_table'),
(31,'Can delete expert_table',8,'delete_expert_table'),
(32,'Can view expert_table',8,'view_expert_table'),
(33,'Can add tips_table',9,'add_tips_table'),
(34,'Can change tips_table',9,'change_tips_table'),
(35,'Can delete tips_table',9,'delete_tips_table'),
(36,'Can view tips_table',9,'view_tips_table'),
(37,'Can add user_table',10,'add_user_table'),
(38,'Can change user_table',10,'change_user_table'),
(39,'Can delete user_table',10,'delete_user_table'),
(40,'Can view user_table',10,'view_user_table'),
(41,'Can add feedback_table',11,'add_feedback_table'),
(42,'Can change feedback_table',11,'change_feedback_table'),
(43,'Can delete feedback_table',11,'delete_feedback_table'),
(44,'Can view feedback_table',11,'view_feedback_table'),
(45,'Can add doubt_table',12,'add_doubt_table'),
(46,'Can change doubt_table',12,'change_doubt_table'),
(47,'Can delete doubt_table',12,'delete_doubt_table'),
(48,'Can view doubt_table',12,'view_doubt_table'),
(49,'Can add video_table',13,'add_video_table'),
(50,'Can change video_table',13,'change_video_table'),
(51,'Can delete video_table',13,'delete_video_table'),
(52,'Can view video_table',13,'view_video_table'),
(53,'Can add password reset otp',14,'add_passwordresetotp'),
(54,'Can change password reset otp',14,'change_passwordresetotp'),
(55,'Can delete password reset otp',14,'delete_passwordresetotp'),
(56,'Can view password reset otp',14,'view_passwordresetotp'),
(57,'Can add uploadpost',15,'add_uploadpost'),
(58,'Can change uploadpost',15,'change_uploadpost'),
(59,'Can delete uploadpost',15,'delete_uploadpost'),
(60,'Can view uploadpost',15,'view_uploadpost'),
(61,'Can add like',16,'add_like'),
(62,'Can change like',16,'change_like'),
(63,'Can delete like',16,'delete_like'),
(64,'Can view like',16,'view_like'),
(65,'Can add comment',17,'add_comment'),
(66,'Can change comment',17,'change_comment'),
(67,'Can delete comment',17,'delete_comment'),
(68,'Can view comment',17,'view_comment'),
(69,'Can add user_ post',18,'add_user_post'),
(70,'Can change user_ post',18,'change_user_post'),
(71,'Can delete user_ post',18,'delete_user_post'),
(72,'Can view user_ post',18,'view_user_post'),
(73,'Can add post notification',19,'add_postnotification'),
(74,'Can change post notification',19,'change_postnotification'),
(75,'Can delete post notification',19,'delete_postnotification'),
(76,'Can view post notification',19,'view_postnotification'),
(77,'Can add post_comment',20,'add_post_comment'),
(78,'Can change post_comment',20,'change_post_comment'),
(79,'Can delete post_comment',20,'delete_post_comment'),
(80,'Can view post_comment',20,'view_post_comment'),
(81,'Can add user_like',21,'add_user_like'),
(82,'Can change user_like',21,'change_user_like'),
(83,'Can delete user_like',21,'delete_user_like'),
(84,'Can view user_like',21,'view_user_like'),
(85,'Can add request',22,'add_request'),
(86,'Can change request',22,'change_request'),
(87,'Can delete request',22,'delete_request'),
(88,'Can view request',22,'view_request'),
(89,'Can add complaint',23,'add_complaint'),
(90,'Can change complaint',23,'change_complaint'),
(91,'Can delete complaint',23,'delete_complaint'),
(92,'Can view complaint',23,'view_complaint'),
(93,'Can add rewview_rating',24,'add_rewview_rating'),
(94,'Can change rewview_rating',24,'change_rewview_rating'),
(95,'Can delete rewview_rating',24,'delete_rewview_rating'),
(96,'Can view rewview_rating',24,'view_rewview_rating'),
(97,'Can add malicious app',25,'add_maliciousapp'),
(98,'Can change malicious app',25,'change_maliciousapp'),
(99,'Can delete malicious app',25,'delete_maliciousapp'),
(100,'Can view malicious app',25,'view_maliciousapp'),
(101,'Can add phishing link',26,'add_phishinglink'),
(102,'Can change phishing link',26,'change_phishinglink'),
(103,'Can delete phishing link',26,'delete_phishinglink'),
(104,'Can view phishing link',26,'view_phishinglink');

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$1000000$sGz1jBa4lKcIunRw44py8C$fyCaTFE//5XwU56CX6avMyerdgtvUgBjnm4YUv+nN8s=','2026-01-29 04:01:41.414978',1,'admin','','','admin@gmail.com',1,1,'2026-01-21 11:06:34.000000'),
(2,'pbkdf2_sha256$1000000$u0BdEfWa3GWBQZjr8KvCpS$ORkCeng/NJhzeUYGb0XgnumKOX2/0cryE/6Q1GfM5h0=',NULL,0,'sankar','sankar','','sankar@gmail.com',0,1,'2026-01-21 11:12:05.243880'),
(3,'pbkdf2_sha256$1000000$yjly96xWHXBs6nRsh0CioE$3X4R+7IF3ufYq5J9mT1/Gda9Ur5Cf6Vn1oiAM9qYgEY=',NULL,0,'Sankar@123','sankar','','sankar@gmail.con',0,1,'2026-01-28 12:16:40.090580'),
(4,'pbkdf2_sha256$1000000$4IU4WNjRDAxWk72OXs8ldY$SmPszf4QtYNyxPnvsTnRGtUbFZ4aO819gjhQW5fMj7A=',NULL,0,'Adnan@123','adnan','','adnan@gmail.com',0,1,'2026-01-28 12:18:57.456046'),
(5,'pbkdf2_sha256$1000000$rtD6APX0rqqkhTenwSm64L$4//toRllLuwGpAPMAJqtSVIE79vwTPfiLEhG8nZYxjo=',NULL,0,'renji','rk','','rk@gmail.com',0,1,'2026-01-28 13:46:38.104124');

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

insert  into `auth_user_groups`(`id`,`user_id`,`group_id`) values 
(1,1,1),
(2,2,2),
(3,3,3),
(4,4,3),
(5,5,3);

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values 
(1,'2026-01-21 11:07:29.555217','1','admin',1,'[{\"added\": {}}]',3,1),
(2,'2026-01-21 11:08:21.067571','2','Expert',1,'[{\"added\": {}}]',3,1),
(3,'2026-01-21 11:08:46.400972','3','User',1,'[{\"added\": {}}]',3,1),
(4,'2026-01-21 11:10:48.139726','1','admin',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1);

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'myapp','chat_table'),
(17,'myapp','comment'),
(23,'myapp','complaint'),
(12,'myapp','doubt_table'),
(8,'myapp','expert_table'),
(11,'myapp','feedback_table'),
(16,'myapp','like'),
(25,'myapp','maliciousapp'),
(14,'myapp','passwordresetotp'),
(26,'myapp','phishinglink'),
(20,'myapp','post_comment'),
(19,'myapp','postnotification'),
(22,'myapp','request'),
(24,'myapp','rewview_rating'),
(9,'myapp','tips_table'),
(15,'myapp','uploadpost'),
(21,'myapp','user_like'),
(18,'myapp','user_post'),
(10,'myapp','user_table'),
(13,'myapp','video_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2026-01-21 11:00:40.162078'),
(2,'auth','0001_initial','2026-01-21 11:00:40.597861'),
(3,'admin','0001_initial','2026-01-21 11:00:40.754748'),
(4,'admin','0002_logentry_remove_auto_add','2026-01-21 11:00:40.760716'),
(5,'admin','0003_logentry_add_action_flag_choices','2026-01-21 11:00:40.764397'),
(6,'contenttypes','0002_remove_content_type_name','2026-01-21 11:00:40.818736'),
(7,'auth','0002_alter_permission_name_max_length','2026-01-21 11:00:40.862088'),
(8,'auth','0003_alter_user_email_max_length','2026-01-21 11:00:40.882431'),
(9,'auth','0004_alter_user_username_opts','2026-01-21 11:00:40.890936'),
(10,'auth','0005_alter_user_last_login_null','2026-01-21 11:00:40.942149'),
(11,'auth','0006_require_contenttypes_0002','2026-01-21 11:00:40.945901'),
(12,'auth','0007_alter_validators_add_error_messages','2026-01-21 11:00:40.947524'),
(13,'auth','0008_alter_user_username_max_length','2026-01-21 11:00:41.005499'),
(14,'auth','0009_alter_user_last_name_max_length','2026-01-21 11:00:41.057435'),
(15,'auth','0010_alter_group_name_max_length','2026-01-21 11:00:41.073480'),
(16,'auth','0011_update_proxy_permissions','2026-01-21 11:00:41.073480'),
(17,'auth','0012_alter_user_first_name_max_length','2026-01-21 11:00:41.146031'),
(18,'myapp','0001_initial','2026-01-21 11:00:41.634606'),
(19,'myapp','0002_passwordresetotp','2026-01-21 11:00:41.644537'),
(20,'myapp','0003_uploadpost_like_comment','2026-01-21 11:00:41.865417'),
(21,'myapp','0004_user_table_image_user_uploadpost','2026-01-21 11:00:41.963377'),
(22,'myapp','0005_user_post_postnotification_delete_user_uploadpost','2026-01-21 11:00:42.108107'),
(23,'myapp','0006_alter_postnotification_user','2026-01-21 11:00:42.219719'),
(24,'myapp','0007_post_comment','2026-01-21 11:00:42.326599'),
(25,'myapp','0008_user_like','2026-01-21 11:00:42.423309'),
(26,'myapp','0009_request','2026-01-21 11:00:42.501265'),
(27,'myapp','0010_complaint_rewview_rating','2026-01-21 11:00:42.603116'),
(28,'myapp','0011_delete_complaint_table','2026-01-21 11:00:42.605122'),
(29,'sessions','0001_initial','2026-01-21 11:00:42.626991'),
(30,'myapp','0012_maliciousapp','2026-01-29 12:03:29.902654'),
(31,'myapp','0013_phishinglink','2026-01-29 12:23:47.655987');

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
('gsx4loprbttl9vyxho7542iyk26y30ax','.eJxVjDsOwjAQBe_iGlle4y8lfc5g7XodHECOFCcV4u4QKQW0b2beSyTc1pq2XpY0sbgIEKffjTA_StsB37HdZpnnti4TyV2RB-1ymLk8r4f7d1Cx12-tTKCgSJNnwsjxbGAEsNFmJIM2gEKnxhKz8Vkb7xRr5yMRqIBQghPvD9gqN2Y:1vlJDx:JJyGYuynTsJCpfV9HGSivDm76oPm1CbsoGliq7ZT7Yk','2026-02-12 04:01:41.444344');

/*Table structure for table `myapp_chat_table` */

DROP TABLE IF EXISTS `myapp_chat_table`;

CREATE TABLE `myapp_chat_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `FROM_id` int NOT NULL,
  `TO_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chat_table_FROM_id_83cb11bb_fk_auth_user_id` (`FROM_id`),
  KEY `myapp_chat_table_TO_id_906cf48c_fk_auth_user_id` (`TO_id`),
  CONSTRAINT `myapp_chat_table_FROM_id_83cb11bb_fk_auth_user_id` FOREIGN KEY (`FROM_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_chat_table_TO_id_906cf48c_fk_auth_user_id` FOREIGN KEY (`TO_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_chat_table` */

insert  into `myapp_chat_table`(`id`,`message`,`date`,`FROM_id`,`TO_id`) values 
(1,'hi','2026-01-28',3,2),
(2,'hi','2026-01-29',4,2);

/*Table structure for table `myapp_comment` */

DROP TABLE IF EXISTS `myapp_comment`;

CREATE TABLE `myapp_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comment` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(500) NOT NULL,
  `USERID_id` int NOT NULL,
  `UPLOADPOST_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_comment_USERID_id_9f3e5c38_fk_auth_user_id` (`USERID_id`),
  KEY `myapp_comment_UPLOADPOST_id_f0f2b468_fk_myapp_uploadpost_id` (`UPLOADPOST_id`),
  CONSTRAINT `myapp_comment_UPLOADPOST_id_f0f2b468_fk_myapp_uploadpost_id` FOREIGN KEY (`UPLOADPOST_id`) REFERENCES `myapp_uploadpost` (`id`),
  CONSTRAINT `myapp_comment_USERID_id_9f3e5c38_fk_auth_user_id` FOREIGN KEY (`USERID_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_comment` */

/*Table structure for table `myapp_complaint` */

DROP TABLE IF EXISTS `myapp_complaint`;

CREATE TABLE `myapp_complaint` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaint_USER_id_21ed0b20_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_complaint_USER_id_21ed0b20_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_complaint` */

/*Table structure for table `myapp_doubt_table` */

DROP TABLE IF EXISTS `myapp_doubt_table`;

CREATE TABLE `myapp_doubt_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doubt` varchar(500) NOT NULL,
  `reply` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `EXPERT_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_doubt_table_EXPERT_id_37521c2b_fk_myapp_expert_table_id` (`EXPERT_id`),
  KEY `myapp_doubt_table_USER_id_297682e8_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_doubt_table_EXPERT_id_37521c2b_fk_myapp_expert_table_id` FOREIGN KEY (`EXPERT_id`) REFERENCES `myapp_expert_table` (`id`),
  CONSTRAINT `myapp_doubt_table_USER_id_297682e8_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_doubt_table` */

/*Table structure for table `myapp_expert_table` */

DROP TABLE IF EXISTS `myapp_expert_table`;

CREATE TABLE `myapp_expert_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` bigint NOT NULL,
  `place` varchar(50) NOT NULL,
  `qualification` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `status` varchar(100) NOT NULL,
  `LOGIN_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_expert_table_LOGIN_id_c5c8ca75_fk_auth_user_id` (`LOGIN_id`),
  CONSTRAINT `myapp_expert_table_LOGIN_id_c5c8ca75_fk_auth_user_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_expert_table` */

insert  into `myapp_expert_table`(`id`,`name`,`email`,`phone`,`place`,`qualification`,`post`,`status`,`LOGIN_id`) values 
(1,'sankar','sankar@gmail.com',9876543210,'kozhikode','mca','kkd town','accepted',2);

/*Table structure for table `myapp_feedback_table` */

DROP TABLE IF EXISTS `myapp_feedback_table`;

CREATE TABLE `myapp_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(500) NOT NULL,
  `rating` int NOT NULL,
  `date` date NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_table_USER_id_f8994646_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_feedback_table_USER_id_f8994646_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_feedback_table` */

/*Table structure for table `myapp_like` */

DROP TABLE IF EXISTS `myapp_like`;

CREATE TABLE `myapp_like` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `like_dislike` varchar(100) NOT NULL,
  `USERID_id` int NOT NULL,
  `UPLOADPOST_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_like_USERID_id_0004010a_fk_auth_user_id` (`USERID_id`),
  KEY `myapp_like_UPLOADPOST_id_72662db3_fk_myapp_uploadpost_id` (`UPLOADPOST_id`),
  CONSTRAINT `myapp_like_UPLOADPOST_id_72662db3_fk_myapp_uploadpost_id` FOREIGN KEY (`UPLOADPOST_id`) REFERENCES `myapp_uploadpost` (`id`),
  CONSTRAINT `myapp_like_USERID_id_0004010a_fk_auth_user_id` FOREIGN KEY (`USERID_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_like` */

/*Table structure for table `myapp_maliciousapp` */

DROP TABLE IF EXISTS `myapp_maliciousapp`;

CREATE TABLE `myapp_maliciousapp` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `package_name` varchar(255) NOT NULL,
  `result` varchar(50) NOT NULL,
  `checked_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `package_name` (`package_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_maliciousapp` */

insert  into `myapp_maliciousapp`(`id`,`package_name`,`result`,`checked_at`) values 
(1,'com.facebook','Malicious','2026-01-29 12:10:04.964088');

/*Table structure for table `myapp_passwordresetotp` */

DROP TABLE IF EXISTS `myapp_passwordresetotp`;

CREATE TABLE `myapp_passwordresetotp` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `otp` varchar(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `used` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_passwordresetotp` */

/*Table structure for table `myapp_phishinglink` */

DROP TABLE IF EXISTS `myapp_phishinglink`;

CREATE TABLE `myapp_phishinglink` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL,
  `result` varchar(20) NOT NULL,
  `checked_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_phishinglink` */

/*Table structure for table `myapp_post_comment` */

DROP TABLE IF EXISTS `myapp_post_comment`;

CREATE TABLE `myapp_post_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comment` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(500) NOT NULL,
  `UPLOADPOST_id` bigint NOT NULL,
  `USERID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_post_comment_UPLOADPOST_id_1e80cb9e_fk_myapp_user_post_id` (`UPLOADPOST_id`),
  KEY `myapp_post_comment_USERID_id_40fb5807_fk_myapp_user_table_id` (`USERID_id`),
  CONSTRAINT `myapp_post_comment_UPLOADPOST_id_1e80cb9e_fk_myapp_user_post_id` FOREIGN KEY (`UPLOADPOST_id`) REFERENCES `myapp_user_post` (`id`),
  CONSTRAINT `myapp_post_comment_USERID_id_40fb5807_fk_myapp_user_table_id` FOREIGN KEY (`USERID_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_post_comment` */

insert  into `myapp_post_comment`(`id`,`comment`,`date`,`status`,`UPLOADPOST_id`,`USERID_id`) values 
(1,'good','2026-01-28','normal',12,3);

/*Table structure for table `myapp_postnotification` */

DROP TABLE IF EXISTS `myapp_postnotification`;

CREATE TABLE `myapp_postnotification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `bottom` varchar(100) NOT NULL,
  `left` varchar(100) NOT NULL,
  `right` varchar(100) NOT NULL,
  `top` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  `POST_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_postnotification_POST_id_7b4f6867_fk_myapp_user_post_id` (`POST_id`),
  KEY `myapp_postnotification_USER_id_b633cd6a_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_postnotification_POST_id_7b4f6867_fk_myapp_user_post_id` FOREIGN KEY (`POST_id`) REFERENCES `myapp_user_post` (`id`),
  CONSTRAINT `myapp_postnotification_USER_id_b633cd6a_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_postnotification` */

/*Table structure for table `myapp_request` */

DROP TABLE IF EXISTS `myapp_request`;

CREATE TABLE `myapp_request` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `FROM_id` bigint NOT NULL,
  `TO_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_request_FROM_id_7471bff1_fk_myapp_user_table_id` (`FROM_id`),
  KEY `myapp_request_TO_id_acb5945a_fk_myapp_user_table_id` (`TO_id`),
  CONSTRAINT `myapp_request_FROM_id_7471bff1_fk_myapp_user_table_id` FOREIGN KEY (`FROM_id`) REFERENCES `myapp_user_table` (`id`),
  CONSTRAINT `myapp_request_TO_id_acb5945a_fk_myapp_user_table_id` FOREIGN KEY (`TO_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_request` */

insert  into `myapp_request`(`id`,`date`,`status`,`FROM_id`,`TO_id`) values 
(1,'2026-01-29','pending',3,1);

/*Table structure for table `myapp_rewview_rating` */

DROP TABLE IF EXISTS `myapp_rewview_rating`;

CREATE TABLE `myapp_rewview_rating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `rating` varchar(100) NOT NULL,
  `review` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_rewview_rating_USER_id_eaa348d6_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_rewview_rating_USER_id_eaa348d6_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_rewview_rating` */

/*Table structure for table `myapp_tips_table` */

DROP TABLE IF EXISTS `myapp_tips_table`;

CREATE TABLE `myapp_tips_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `details` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `EXPERT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_tips_table_EXPERT_id_ef72031f_fk_myapp_expert_table_id` (`EXPERT_id`),
  CONSTRAINT `myapp_tips_table_EXPERT_id_ef72031f_fk_myapp_expert_table_id` FOREIGN KEY (`EXPERT_id`) REFERENCES `myapp_expert_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_tips_table` */

/*Table structure for table `myapp_uploadpost` */

DROP TABLE IF EXISTS `myapp_uploadpost`;

CREATE TABLE `myapp_uploadpost` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `post` varchar(400) NOT NULL,
  `caption` varchar(500) NOT NULL,
  `LOGIN_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_uploadpost_LOGIN_id_b6b98c48_fk_auth_user_id` (`LOGIN_id`),
  CONSTRAINT `myapp_uploadpost_LOGIN_id_b6b98c48_fk_auth_user_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_uploadpost` */

/*Table structure for table `myapp_user_like` */

DROP TABLE IF EXISTS `myapp_user_like`;

CREATE TABLE `myapp_user_like` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `like_dislike` varchar(100) NOT NULL,
  `UPLOADPOST_id` bigint NOT NULL,
  `USERID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_like_UPLOADPOST_id_2096b00a_fk_myapp_user_post_id` (`UPLOADPOST_id`),
  KEY `myapp_user_like_USERID_id_df9b1804_fk_myapp_user_table_id` (`USERID_id`),
  CONSTRAINT `myapp_user_like_UPLOADPOST_id_2096b00a_fk_myapp_user_post_id` FOREIGN KEY (`UPLOADPOST_id`) REFERENCES `myapp_user_post` (`id`),
  CONSTRAINT `myapp_user_like_USERID_id_df9b1804_fk_myapp_user_table_id` FOREIGN KEY (`USERID_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_user_like` */

insert  into `myapp_user_like`(`id`,`like_dislike`,`UPLOADPOST_id`,`USERID_id`) values 
(1,'',12,3);

/*Table structure for table `myapp_user_post` */

DROP TABLE IF EXISTS `myapp_user_post`;

CREATE TABLE `myapp_user_post` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `post` varchar(400) NOT NULL,
  `caption` varchar(500) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_post_USER_id_ca841f1f_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_user_post_USER_id_ca841f1f_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_user_post` */

insert  into `myapp_user_post`(`id`,`date`,`post`,`caption`,`USER_id`) values 
(12,'2026-01-28','/media/user/202601281920530300.bmp','renjith',2),
(13,'2026-01-29','/media/user/202601290938231850.bmp','again renjith',2);

/*Table structure for table `myapp_user_table` */

DROP TABLE IF EXISTS `myapp_user_table`;

CREATE TABLE `myapp_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` bigint NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `LOGIN_id` int NOT NULL,
  `image` varchar(400) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_table_LOGIN_id_76a60eb1_fk_auth_user_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_table_LOGIN_id_76a60eb1_fk_auth_user_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_user_table` */

insert  into `myapp_user_table`(`id`,`name`,`email`,`phone`,`place`,`post`,`LOGIN_id`,`image`) values 
(1,'sankar','sankar@gmail.con',9632587410,'malappuram ','klr',3,'/media/user/20260128-174639.jpg'),
(2,'adnan','adnan@gmail.com',9632587410,'ponnani','mlp',4,'/media/user/20260128-174857.jpg'),
(3,'rk','rk@gmail.com',7878787878,'la','ost',5,'/media/user/20260128-191637.jpg');

/*Table structure for table `myapp_video_table` */

DROP TABLE IF EXISTS `myapp_video_table`;

CREATE TABLE `myapp_video_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `video` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `EXPERT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_video_table_EXPERT_id_c46c5e59_fk_myapp_expert_table_id` (`EXPERT_id`),
  CONSTRAINT `myapp_video_table_EXPERT_id_c46c5e59_fk_myapp_expert_table_id` FOREIGN KEY (`EXPERT_id`) REFERENCES `myapp_expert_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_video_table` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
