create database if not exists loginBot;
use loginBot;

create table user_info(
uid int auto_increment primary key ,
u_name varchar(255) not null,
u_pwd  varchar(255) not null 
);

create table saved_login(
sl int auto_increment primary key,saved_loginsaved_login
uid int not null,
u_login varchar(255) not null,
u_pass varchar(255) not null,
u_url varchar(255) not null,

foreign key(uid) references user_info(uid)
);

ALTER table saved_login add column sl_name varchar(255);
ALTER TABLE user_info ADD UNIQUE (u_name);