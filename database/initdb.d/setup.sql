CREATE TABLE data (
    id int(11) not null primary key auto_increment,
    url varchar(255) not null,
    title varchar(100) not null,
    date_added datetime not null
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
