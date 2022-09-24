DROP DATABASE IF EXISTS TODOS;

CREATE DATABASE TODOS;

USE TODOS;

DROP TABLE IF EXISTS todo;

CREATE TABLE todo(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date VARCHAR(20),
    content VARCHAR(50),
    is_done BOOLEAN
);

-- INSERT INTO todo(date, content, is_done) VALUES('2022-08-01', 'test1', false);
-- INSERT INTO todo(date, content, is_done) VALUES('2022-08-02', 'test2', false);
