
drop database if exists douban;

create database douban default charset utf8;

use douban;

drop table if exists movie;
create table movie (
`id` int not null auto_increment,
`douban_id` int,
`title` varchar(1024),
`directors` varchar(128),
`scriptwriters` varchar(128),
`actors` varchar(1024),
`types` varchar(256),
`release_region` varchar(128),
`release_date` varchar(128),
`alias` varchar(126),
`languages` varchar(128),
`duration` int,
`score` float,
`description` text,
`tags` varchar(1024),
`link` varchar(32),
`posters` varchar(1024),
primary key(`id`)
) charset=utf8;
