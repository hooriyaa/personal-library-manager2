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


