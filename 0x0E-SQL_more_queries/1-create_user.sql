-- Create a User
CREATE DATABASE IF NOT EXIST hbtn_0d_2;
CREATE USER IF NOT EXIST user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_1@localhost;
