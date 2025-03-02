-- ● Write SQL query to solve the problem given below
-- Here we are talking about the Bank related information of a person.
-- For which you need to create three tables named as Bank, Account holder and Loan table.

create database BANK_OF_IMROZ;
use BANK_OF_IMROZ;

-- #######################################################################################

-- And solve the problem stated below.

-- Create a Bank table, attributes are : branch id, branch name, branch city

CREATE TABLE bank_table (
    branch_id INT PRIMARY KEY,  
    branch_name VARCHAR(30) NOT NULL, 
    branch_city VARCHAR(20) NOT NULL
);

select * from bank_table;

-- #######################################################################################

-- Create a Loan table, attributes are : loan no, branch id, account holder’s id, loan 
-- amount and loan type

CREATE TABLE loan_table (
    loan_no INT PRIMARY KEY AUTO_INCREMENT, 
    branch_id INT, 
    account_holder_id INT, 
    loan_amount DECIMAL(15,2) NOT NULL, 
    loan_type VARCHAR(20) NOT NULL,
    FOREIGN KEY (branch_id) REFERENCES bank_table(branch_id) ON DELETE CASCADE,
    FOREIGN KEY (account_holder_id) REFERENCES account_holder(account_holder_id) ON DELETE CASCADE
);

select * from loan_table;

-- #######################################################################################

-- Create a table named as Account holder for the same scenario containing the
-- attributes are account holder’s id, account no, account holder’s name,
-- city,contact, date of account created, account status (active or terminated),
-- account type and balance.

CREATE TABLE account_holder (
    account_holder_id INT PRIMARY KEY,         
    account_no VARCHAR(20) UNIQUE NOT NULL,    
    account_holder_name VARCHAR(50) NOT NULL, 
    city VARCHAR(30) NOT NULL,               
    contact VARCHAR(15) UNIQUE NOT NULL,     
    date_of_creation DATE NOT NULL,         
    account_status ENUM('active', 'terminated') NOT NULL, 
    account_type VARCHAR(20) NOT NULL,         
    balance DECIMAL(15,2) NOT NULL DEFAULT 0.00
);

select *  from account_holder;

-- #######################################################################################

-- ● Consider an example where there’s an account holder table where we are
-- doing an intra bank transfer i.e. a person holding account A is trying to
-- transfer $100 to account B.
-- - for this you have to make a transaction in sql which can
-- transfer fund from account A to B
-- - Make sure after the transaction the account information
-- have to be updated for both the credit account and the
-- debited account

DELIMITER //
CREATE PROCEDURE TransferFunds(IN from_account VARCHAR(20), IN to_account VARCHAR(20), 
IN amount DECIMAL(15,2))
BEGIN DECLARE available_balance DECIMAL(15,2);
    SELECT balance INTO available_balance FROM account_holder WHERE account_no = from_account;
    IF available_balance >= amount THEN
        START TRANSACTION;
        UPDATE account_holder SET balance = balance - amount WHERE account_no = from_account;
        UPDATE account_holder SET balance = balance + amount WHERE account_no = to_account;
        COMMIT;
        SELECT 'Transaction Successful' AS Message;
    ELSE ROLLBACK;
        SELECT 'Transaction Failed: Insufficient Balance' AS Message;
    END IF;
END //
DELIMITER ;
CALL TransferFunds('A12345', 'B67890', 100);

select * from account_holder;

-- #######################################################################################
-- ● Also fetch the details of the account holder who are related from the same city

SELECT city, GROUP_CONCAT(account_holder_name SEPARATOR ', ') AS Account_Holders
FROM account_holder
GROUP BY city
HAVING COUNT(account_holder_id) > 1;

-- +--------+------------------------------------------------------------------------+
-- | city   | Account_Holders                                                        |
-- +--------+------------------------------------------------------------------------+
-- | Goa    | Salman Khan, sahil khan, Govinda                                       |
-- | Indore | Akshay Kumar, Ranveer singh                                            |
-- | Jaipur | Anil Kapoor, Shahruk khan, Ranveer Kapoor, Aamir khan, Amitab bachchan |
-- +--------+------------------------------------------------------------------------+

-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

SELECT A.account_holder_id AS Holder1_ID, A.account_holder_name AS Holder1_Name, 
       B.account_holder_id AS Holder2_ID, B.account_holder_name AS Holder2_Name, 
       A.city
FROM account_holder A JOIN account_holder B ON A.city = B.city 
AND A.account_holder_id < B.account_holder_id ORDER BY A.city;

-- +------------+----------------+------------+-----------------+--------+
-- | Holder1_ID | Holder1_Name   | Holder2_ID | Holder2_Name    | city   |
-- +------------+----------------+------------+-----------------+--------+
-- |        102 | Salman Khan    |        107 | sahil khan      | Goa    |
-- |        102 | Salman Khan    |        108 | Govinda         | Goa    |
-- |        107 | sahil khan     |        108 | Govinda         | Goa    |
-- |        103 | Akshay Kumar   |        109 | Ranveer singh   | Indore |
-- |        104 | Anil Kapoor    |        106 | Shahruk khan    | Jaipur |
-- |        104 | Anil Kapoor    |        110 | Ranveer Kapoor  | Jaipur |
-- |        104 | Anil Kapoor    |        111 | Aamir khan      | Jaipur |
-- |        104 | Anil Kapoor    |        112 | Amitab bachchan | Jaipur |
-- |        106 | Shahruk khan   |        110 | Ranveer Kapoor  | Jaipur |
-- |        106 | Shahruk khan   |        111 | Aamir khan      | Jaipur |
-- |        106 | Shahruk khan   |        112 | Amitab bachchan | Jaipur |
-- |        110 | Ranveer Kapoor |        111 | Aamir khan      | Jaipur |
-- |        110 | Ranveer Kapoor |        112 | Amitab bachchan | Jaipur |
-- |        111 | Aamir khan     |        112 | Amitab bachchan | jaipur |
-- +------------+----------------+------------+-----------------+--------+

-- #######################################################################################

-- ● Write a query to fetch account number and account holder name, whose
-- accounts were created after 15th of any month

SELECT account_no, account_holder_name, date_of_creation FROM ACCOUNT_HOLDER 
WHERE DAY(date_of_creation) > 15;

-- +------------+---------------------+------------------+
-- | account_no | account_holder_name | date_of_creation |
-- +------------+---------------------+------------------+
-- | A12345     | Hritik Roshan       | 2024-02-16       |
-- | C54321     | Akshay Kumar        | 2024-03-20       |
-- | E45678     | Varun Dhavan        | 2024-04-18       |
-- | A125345    | sahil khan          | 2024-02-16       |
-- | C543h21    | Ranveer singh       | 2024-03-20       |
-- | E45678h    | Aamir khan          | 2024-04-18       |
-- +------------+---------------------+------------------+

-- #######################################################################################

-- ● Write a query to display the city name and count the branches in that city.
-- Give the count of branches an alias name of Count_Branch.

SELECT branch_city, COUNT(branch_id) AS Count_Branch
FROM bank_table
GROUP BY branch_city;

-- +----------------+--------------+
-- | branch_city    | Count_Branch |
-- +----------------+--------------+
-- | Panjab         |            1 |
-- | Rajasthan      |            1 |
-- | Gujrat         |            1 |
-- | Madhya Pradesh |            4 |
-- | Goa            |            7 |
-- | HIMACHAL       |            3 |
-- | KERAL          |            3 |
-- +----------------+--------------+

-- #######################################################################################

-- ● Write a query to display the account holder’s id, account holder’s name,
-- branch id, and loan amount for people who have taken loans. (NOTE : use
-- sql join concept to solve the query)

-- Make sure to make your code clean kneat

SELECT ah.account_holder_id, 
       ah.account_holder_name, 
       l.branch_id, 
       l.loan_amount
FROM account_holder ah
JOIN loan_table l ON ah.account_holder_id = l.account_holder_id;

-- +-------------------+---------------------+-----------+-------------+
-- | account_holder_id | account_holder_name | branch_id | loan_amount |
-- +-------------------+---------------------+-----------+-------------+
-- |               101 | Hritik Roshan       |         1 |    50000.00 |
-- |               102 | Salman Khan         |         2 |   100000.00 |
-- |               104 | Anil Kapoor         |         4 |    20000.00 |
-- |               105 | Varun Dhavan        |         5 |    30000.00 |
-- |               108 | Govinda             |         6 |   715000.00 |
-- |               109 | Ranveer singh       |         7 |  7150500.00 |
-- |               110 | Ranveer Kapoor      |         8 |   550500.00 |
-- +-------------------+---------------------+-----------+-------------+

-- #######################################################################################

-- Insert data into bank_table
INSERT INTO bank_table (branch_id, branch_name, branch_city) VALUES
(1, 'Panjab National Bank', 'Panjab'),
(2, 'State Bank of India', 'Rajasthan'),
(3, 'AXIS Bank', 'Gujrat'),
(4, 'Kotak Mahindra', 'Madhya Pradesh'),
(5, 'Union Bank', 'Goa'),
(6, 'Panjab National Bank', 'HIMACHAL'),
(7, 'State Bank of India', 'KERAL'),
(8, 'AXIS Bank', 'GOA'),
(9, 'Kotak Mahindra', 'Madhya Pradesh'),
(10, 'Union Bank', 'Goa'),
(11, 'Panjab National Bank', 'HIMACHAL'),
(12, 'State Bank of India', 'KERAL'),
(13, 'AXIS Bank', 'GOA'),
(14, 'Kotak Mahindra', 'Madhya Pradesh'),
(15, 'Union Bank', 'Goa'),
(16, 'Panjab National Bank', 'HIMACHAL'),
(17, 'State Bank of India', 'KERAL'),
(18, 'AXIS Bank', 'GOA'),
(19, 'Kotak Mahindra', 'Madhya Pradesh'),
(20, 'Union Bank', 'Goa');

-- Insert data into account_holder
INSERT INTO account_holder (account_holder_id, account_no, account_holder_name, city, contact, 
date_of_creation, account_status, account_type, balance) VALUES
(101, 'A12345', 'Hritik Roshan', 'Chandigarh', '1234567890', '2024-02-16', 'active', 'Savings', 500.00),
(102, 'B67890', 'Salman Khan', 'Goa', '9876543210', '2024-03-10', 'active', 'Current', 700.00),
(103, 'C54321', 'Akshay Kumar', 'Indore', '4561237890', '2024-03-20', 'active', 'Savings', 1000.00),
(104, 'D98765', 'Anil Kapoor', 'Jaipur', '7893216540', '2024-02-14', 'active', 'Current', 300.00),
(105, 'E45678', 'Varun Dhavan', 'Mumbai', '3216549870', '2024-04-18', 'terminated', 'Savings', 200.00),
(106, 'F12345', 'Shahruk khan', 'Jaipur', '78932165440', '2024-02-14', 'active', 'Current', 900.00),
(107, 'A125345', 'sahil khan', 'Goa', '12345657890', '2024-02-16', 'active', 'Savings', 500.00),
(108, 'B678590', 'Govinda', 'Goa', '987654321054', '2024-03-10', 'active', 'Current', 700.00),
(109, 'C543h21', 'Ranveer singh', 'Indore', '456541237890', '2024-03-20', 'active', 'Savings', 1000.00),
(110, 'D9876h5', 'Ranveer Kapoor', 'Jaipur', '789354216540', '2024-02-14', 'active', 'Current', 300.00),
(111, 'E45678h', 'Aamir khan', 'jaipur', '3216549875540', '2024-04-18', 'terminated', 'Savings', 200.00),
(112, 'F1234d5', 'Amitab bachchan', 'Jaipur', '7893254165440', '2024-02-14', 'active', 'Current', 900.00);

-- Insert data into loan_table
INSERT INTO loan_table (branch_id, account_holder_id, loan_amount, loan_type) VALUES
(1, 101, 50000.00, 'Personal'),
(2, 102, 100000.00, 'Home'),
(4, 104, 20000.00, 'Education'),
(5, 105, 30000.00, 'Business'),
(6, 108, 715000.00, 'jet'),
(7, 109, 7150500.00, 'plane'),
(8, 110, 550500.00, 'yatch');




