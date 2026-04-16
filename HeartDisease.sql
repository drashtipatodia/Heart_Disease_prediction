-- -------------------------
-- CREATE DATABASE
-- -------------------------
CREATE DATABASE heart_disease;
USE heart_disease;

-- -------------------------
-- MAIN DATA TABLE
-- -------------------------
CREATE TABLE heart_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    sex INT,
    cp INT,
    trestbps INT,
    chol INT,
    fbs INT,
    restecg INT,
    thalach INT,
    exang INT,
    oldpeak FLOAT,
    slope INT,
    ca INT,
    thal INT,
    target INT
);

-- -------------------------
-- PREDICTIONS TABLE
-- -------------------------
CREATE TABLE heart_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    sex INT,
    cp INT,
    trestbps INT,
    chol INT,
    prediction INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -------------------------
-- CHECK DATA
-- -------------------------
SELECT * FROM heart_data;
SELECT COUNT(*) FROM heart_data;

SELECT * FROM heart_predictions;
