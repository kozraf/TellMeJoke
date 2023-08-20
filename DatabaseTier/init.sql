
-- Create the database
CREATE DATABASE IF NOT EXISTS jokes_db;

-- Use the database
USE jokes_db;

-- Create the jokes table
CREATE TABLE IF NOT EXISTS jokes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    joke TEXT NOT NULL,
    words INT,
    letters INT,
    sentences INT
);
