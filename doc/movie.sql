drop database if exists douban;

create database douban default charset utf8;

use douban;

drop table if exists movie;
create table movie (
`douban_id` varchar(16) not null,
`title` varchar(1024),
`directors` text,
`scriptwriters` text,
`actors` text,
`types` text,
`release_region` text,
`release_date` text,
`alias` text,
`languages` text,
`duration` text,
`score` text,
`description` text,
`tags` text,
primary key(`douban_id`)
) charset=utf8;

/* type说明：
1表示剧照，
2表示海报，
3表示壁纸

完整的图片url为:
https://movie.douban.com/photos/photo/photo_id
example:
https://movie.douban.com/photos/photo/2285200316/
*/
drop table if exists photo;
create table photo (
`id` int not null auto_increment,
`douban_id` varchar(16),
`type` tinyint,
`photo_id` varchar(16),
primary key(`id`)
) charset=utf8;