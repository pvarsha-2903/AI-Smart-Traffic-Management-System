-- =========================================
-- 🚦 AI SMART TRAFFIC MANAGEMENT DATABASE
-- =========================================

CREATE DATABASE IF NOT EXISTS traffic_db;
USE traffic_db;

DROP TABLE IF EXISTS traffic_data;

CREATE TABLE traffic_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lane VARCHAR(10) NOT NULL,
    vehicles INT NOT NULL,
    wait_time INT NOT NULL,
    signal_status VARCHAR(10) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO traffic_data (lane, vehicles, wait_time, signal_status) VALUES
('North', 50, 30, 'RED'),
('South', 20, 80, 'RED'),
('East', 70, 20, 'GREEN'),
('West', 10, 100, 'RED');

SELECT * FROM traffic_data;

ALTER USER 'root'@'localhost' 
IDENTIFIED WITH mysql_native_password 
BY 'root';

FLUSH PRIVILEGES;
