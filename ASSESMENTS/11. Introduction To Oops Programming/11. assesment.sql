-- ● Write SQL query to solve the problem given below
-- Consider a scenario in which you have to create a table called Nobel_win where you
-- have given the information about the entity who has achieved nobel prize in a particular
-- subject all over the world.
-- Over here the table Nobel_win will contain attributes like year, subject, winner, country and
-- category
-- You need to use the sql commands to create the table given and to solve the problem given
-- below.
-- Eg :

-- +----+------+------------+------------------------+---------+----------------+
-- | ID | YEAR | SUBJECT    | WINNER                 | COUNTRY | CATEGORY       |
-- +----+------+------------+------------------------+---------+----------------+
-- |  1 | 1970 | Physics    | Hannes Alfven          | Sweden  | Scientist      |
-- |  2 | 1970 | Physics    | Louis Neel             | France  | Scientist      |
-- |  3 | 1970 | Chemistry  | Luis Federico Leloir   | France  | Scientist      |
-- |  4 | 1970 | Physiology | Ulf von Euler          | Sweden  | Scientist      |
-- |  5 | 1970 | Physiology | Bernard Katz           | Germany | Scientist      |
-- |  6 | 1970 | Literature | Aleksandr Solzhenitsyn | Russia  | Linguist       |
-- |  7 | 1970 | Economics  | Paul Samuelson         | USA     | Economist      |
-- |  8 | 1970 | Physiology | Julius Axelrod         | USA     | Scientist      |
-- |  9 | 1971 | Physics    | Dennis Gabor           | Hungary | Scientist      |
-- | 10 | 1971 | Chemistry  | Gerhard Herzberg       | Germany | Scientist      |
-- | 11 | 1971 | Peace      | Willy Brandt           | Germany | Chancellor     |
-- | 12 | 1971 | Literature | Pablo Neruda           | Chile   | Linguist       |
-- | 13 | 1971 | Economics  | Simon Kuznets          | Russia  | Economist      |
-- | 14 | 1978 | Peace      | Anwar al-Sadat         | Egypt   | President      |
-- | 15 | 1978 | Peace      | Menachem Begin         | Israel  | Prime Minister |
-- | 16 | 1987 | Chemistry  | Donald J. Cram         | USA     | Scientist      |
-- | 17 | 1987 | Chemistry  | Jean-Marie Lehn        | France  | Scientist      |
-- | 18 | 1987 | Physiology | Susumu Tonegawa        | Japan   | Scientist      |
-- | 19 | 1987 | Physics    | Johannes Georg Bednorz | Germany | Scientist      |
-- | 20 | 1987 | Literature | Joseph Brodsky         | Russia  | Linguist       |
-- | 21 | 1987 | Economics  | Robert Solow           | USA     | Economist      |
-- | 22 | 1994 | Economics  | Reinhard Selten        | Germany | Economist      |
-- | 23 | 1994 | Peace      | Yitzhak Rabin          | Israel  | Prime Minister |
-- | 24 | 1994 | Literature | Kenzaburo Oe           | Japan   | Linguist       |
-- +----+------+------------+------------------------+---------+----------------+
create database NOBEL_WINNERS_DATA;
show databases;
USE NOBEL_WINNERS_DATA;
CREATE TABLE NOBEL_WIN ( ID INT PRIMARY KEY AUTO_INCREMENT , YEAR INT, SUBJECT VARCHAR(20), WINNER VARCHAR(30), COUNTRY VARCHAR(15), CATEOGRY VARCHAR(15));
INSERT INTO NOBEL_WIN (YEAR, SUBJECT, WINNER, COUNTRY, CATEOGRY) VALUES
(1970, 'Physics', 'Hannes Alfven', 'Sweden', 'Scientist'),
(1970, 'Physics', 'Louis Neel', 'France', 'Scientist'),
(1970, 'Chemistry', 'Luis Federico Leloir', 'France', 'Scientist'),
(1970, 'Physiology', 'Ulf von Euler', 'Sweden', 'Scientist'),
(1970, 'Physiology', 'Bernard Katz', 'Germany', 'Scientist'),
(1970, 'Literature', 'Aleksandr Solzhenitsyn', 'Russia', 'Linguist'),
(1970, 'Economics', 'Paul Samuelson', 'USA', 'Economist'),
(1970, 'Physiology', 'Julius Axelrod', 'USA', 'Scientist'),
(1971, 'Physics', 'Dennis Gabor', 'Hungary', 'Scientist'),
(1971, 'Chemistry', 'Gerhard Herzberg', 'Germany', 'Scientist'),
(1971, 'Peace', 'Willy Brandt', 'Germany', 'Chancellor'),
(1971, 'Literature', 'Pablo Neruda', 'Chile', 'Linguist'),
(1971, 'Economics', 'Simon Kuznets', 'Russia', 'Economist'),
(1978, 'Peace', 'Anwar al-Sadat', 'Egypt', 'President'),
(1978, 'Peace', 'Menachem Begin', 'Israel', 'Prime Minister'),
(1987, 'Chemistry', 'Donald J. Cram', 'USA', 'Scientist'),
(1987, 'Chemistry', 'Jean-Marie Lehn', 'France', 'Scientist'),
(1987, 'Physiology', 'Susumu Tonegawa', 'Japan', 'Scientist'),
(1987, 'Physics', 'Johannes Georg Bednorz', 'Germany', 'Scientist'),
(1987, 'Literature', 'Joseph Brodsky', 'Russia', 'Linguist'),
(1987, 'Economics', 'Robert Solow', 'USA', 'Economist'),
(1994, 'Economics', 'Reinhard Selten', 'Germany', 'Economist'),
(1994, 'Peace', 'Yitzhak Rabin', 'Israel', 'Prime Minister'),
(1994, 'Literature', 'Kenzaburo Oe', 'Japan', 'Linguist');

ALTER TABLE NOBEL_WIN RENAME COLUMN CATEOGRY TO CATEGORY;

select *  from NOBEL_WIN;

-- #############################################################################################################################\

-- Now make sure to solve the following query :

-- #############################################################################################################################\

-- ● Write sql query to find the nobel prize winners of the year 1970. Return year,subject and winner.
SELECT YEAR, SUBJECT, WINNER FROM NOBEL_WIN WHERE YEAR = 1970;
-- +------+------------+------------------------+
-- | YEAR | SUBJECT    | WINNER                 |
-- +------+------------+------------------------+
-- | 1970 | Physics    | Hannes Alfven          |
-- | 1970 | Physics    | Louis Neel             |
-- | 1970 | Chemistry  | Luis Federico Leloir   |
-- | 1970 | Physiology | Ulf von Euler          |
-- | 1970 | Physiology | Bernard Katz           |
-- | 1970 | Literature | Aleksandr Solzhenitsyn |
-- | 1970 | Economics  | Paul Samuelson         |
-- | 1970 | Physiology | Julius Axelrod         |
-- +------+------------+------------------------+
-- #############################################################################################################################\

-- ● Write sql query to find the nobel prize winners in chemistry between the years 1965
-- and 1975. Begin and end values are included Return year, subject, winner and country.

SELECT YEAR, SUBJECT, WINNER, COUNTRY FROM NOBEL_WIN WHERE SUBJECT = "chemistry" and year between 1965 and 1975;

-- +------+-----------+----------------------+---------+
-- | YEAR | SUBJECT   | WINNER               | COUNTRY |
-- +------+-----------+----------------------+---------+
-- | 1970 | Chemistry | Luis Federico Leloir | France  |
-- | 1971 | Chemistry | Gerhard Herzberg     | Germany |
-- +------+-----------+----------------------+---------+

-- #############################################################################################################################\

-- ● Write sql query to retrieve the details of the winners whose first name matches with
-- the string ‘Louis’. Return year,subject,winner,country

SELECT YEAR, SUBJECT, WINNER, COUNTRY FROM NOBEL_WIN WHERE WINNER LIKE "Louis%";

-- +------+---------+------------+---------+
-- | YEAR | SUBJECT | WINNER     | COUNTRY |
-- +------+---------+------------+---------+
-- | 1970 | Physics | Louis Neel | France  |
-- +------+---------+------------+---------+

-- #############################################################################################################################\

-- ● Write sql query to find Nobel prize winners for the subject that does not begin with
-- the letter ‘P’. Order the result by year, descending and winner in ascending

SELECT * FROM NOBEL_WIN WHERE SUBJECT NOT LIKE "P%" order by YEAR desc, WINNER asc;

-- +----+------+------------+------------------------+---------+-----------+
-- | ID | YEAR | SUBJECT    | WINNER                 | COUNTRY | CATEGORY  |
-- +----+------+------------+------------------------+---------+-----------+
-- | 24 | 1994 | Literature | Kenzaburo Oe           | Japan   | Linguist  |
-- | 22 | 1994 | Economics  | Reinhard Selten        | Germany | Economist |
-- | 16 | 1987 | Chemistry  | Donald J. Cram         | USA     | Scientist |
-- | 17 | 1987 | Chemistry  | Jean-Marie Lehn        | France  | Scientist |
-- | 20 | 1987 | Literature | Joseph Brodsky         | Russia  | Linguist  |
-- | 21 | 1987 | Economics  | Robert Solow           | USA     | Economist |
-- | 10 | 1971 | Chemistry  | Gerhard Herzberg       | Germany | Scientist |
-- | 12 | 1971 | Literature | Pablo Neruda           | Chile   | Linguist  |
-- | 13 | 1971 | Economics  | Simon Kuznets          | Russia  | Economist |
-- |  6 | 1970 | Literature | Aleksandr Solzhenitsyn | Russia  | Linguist  |
-- |  3 | 1970 | Chemistry  | Luis Federico Leloir   | France  | Scientist |
-- |  7 | 1970 | Economics  | Paul Samuelson         | USA     | Economist |
-- +----+------+------------+------------------------+---------+-----------+

-- #############################################################################################################################\

-- ● Write sql query to find the details of 1970 Nobel prize winners. Order the result by
-- subject, ascending except for ‘Chemistry’ and ‘Economics’ which will come at the
-- end of the result set. Return year, subject, winner , country and category.
-- Make sure to make your clean and clear code

SELECT year, subject, winner, country, category FROM NOBEL_WIN WHERE year = 1970
ORDER BY CASE WHEN subject IN ('Chemistry', 'Economics') THEN 1  ELSE 0 END, subject ASC;

-- +------+------------+------------------------+---------+-----------+
-- | year | subject    | winner                 | country | category  |
-- +------+------------+------------------------+---------+-----------+
-- | 1970 | Literature | Aleksandr Solzhenitsyn | Russia  | Linguist  |
-- | 1970 | Physics    | Hannes Alfven          | Sweden  | Scientist |
-- | 1970 | Physics    | Louis Neel             | France  | Scientist |
-- | 1970 | Physiology | Ulf von Euler          | Sweden  | Scientist |
-- | 1970 | Physiology | Bernard Katz           | Germany | Scientist |
-- | 1970 | Physiology | Julius Axelrod         | USA     | Scientist |
-- | 1970 | Chemistry  | Luis Federico Leloir   | France  | Scientist |
-- | 1970 | Economics  | Paul Samuelson         | USA     | Economist |
-- +------+------------+------------------------+---------+-----------+

