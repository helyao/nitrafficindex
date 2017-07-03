/*
Navicat MySQL Data Transfer

Source Server         : iLinuxPC
Source Server Version : 50555
Source Host           : 192.168.1.100:3306
Source Database       : traffic

Target Server Type    : MYSQL
Target Server Version : 50555
File Encoding         : 65001

Date: 2017-06-27 14:56:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tra_info
-- ----------------------------
DROP TABLE IF EXISTS `tra_info`;
CREATE TABLE `tra_info` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `id` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `startName` varchar(100) DEFAULT NULL,
  `endName` varchar(100) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `roadGrade` tinyint(4) DEFAULT NULL,
  `avgspeed` double(4,1) DEFAULT NULL,
  `sIndex` double(4,1) DEFAULT NULL,
  `cIndex` double(4,1) DEFAULT NULL,
  `bIndex` double(4,1) DEFAULT NULL,
  `dir` varchar(100) DEFAULT NULL,
  `rticLonlats` varchar(255) DEFAULT NULL,
  `rticId` varchar(255) DEFAULT NULL,
  `vkt` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
