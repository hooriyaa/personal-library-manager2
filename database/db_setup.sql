-- CREATE DATABASE library_db;
-- USE library_db;

-- CREATE TABLE books (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     author VARCHAR(255) NOT NULL,
--     genre VARCHAR(100),
--     status ENUM('Available', 'Checked Out') DEFAULT 'Available',
--     added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    publication_year INT,
    Genre VARCHAR(100),
    ReadStatus BOOLEAN,
    Rating INT,
    Summary TEXT
);


