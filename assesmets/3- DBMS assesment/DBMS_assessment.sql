create database assessment;

use assessment;

CREATE TABLE product (
    PRO_ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PRO_NAME varchar(255),
    PRO_PRICE float,
    PRO_CODE int
) AUTO_INCREMENT=101;

INSERT INTO product (PRO_NAME, PRO_PRICE, PRO_CODE) 
VALUES 
('Mother Board', 3200 , 15),
('Key Board', 450 , 16),
('zip Drive', 250 , 14),
('Speaker', 550 , 16),
('Moniter', 5000 , 11),
('DVD Drive', 900 , 12),
('CD Drive', 800, 12),
('Printer', 2600 , 13),
('Refill cartridge', 350 , 13),
('mouse', 250 , 12);

select pro_price , pro_name
from product
where PRO_PRICE>=250
order by PRO_PRICE desc,
PRO_NAME ;


SELECT PRO_NAME, PRO_PRICE
FROM product
ORDER BY PRO_PRICE
LIMIT 1;


SELECT PRO_CODE, AVG(PRO_PRICE) AS average_price
FROM product
GROUP BY PRO_CODE;

SELECT AVG(PRO_PRICE) AS average_total
FROM product;



