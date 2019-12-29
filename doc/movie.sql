drop database if exists douban;

create database douban default charset utf8mb4;

use douban;

drop table if exists movie;
create table movie (
    `douban_id` varchar(16) not null primary key comment '豆瓣的标记id当主键,顺便用来去重',
    `title` varchar(1024) not null default '' comment '标题',
    `directors` text comment  '导演',
    `scriptwriters` text comment '编剧',
    `actors` text comment '演员',
    `types` text comment '类别',
    `release_region` text comment '上映地区',
    `release_date` text comment '上映日期',
    `alias` text comment '别名',
    `languages` text comment '语言',
    `duration` text comment '播放时长',
    `score` text comment '评分',
    `description` text comment '描述',
    `tags` text comment '标签',
    `create_at` timestamp not null default current_timestamp
) engine=innodb default charset=utf8mb4;

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