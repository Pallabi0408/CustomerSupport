-- CREATE DATABASE IF NOT EXISTS customer_support_db;
-- USE customer_support_db;

-- CREATE TABLE IF NOT EXISTS Users (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     username VARCHAR(50) NOT NULL UNIQUE,
--     password_hash VARCHAR(255) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE IF NOT EXISTS Tickets (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     user_id INT,
--     text TEXT NOT NULL,
--     status VARCHAR(20) DEFAULT 'open',
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
-- );

-- CREATE TABLE IF NOT EXISTS Predictions (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     ticket_id INT,
--     category VARCHAR(50),
--     sentiment VARCHAR(20),
--     summary TEXT,
--     auto_reply TEXT,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (ticket_id) REFERENCES Tickets(id) ON DELETE CASCADE
-- );
