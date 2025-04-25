CREATE TABLE PhoneBook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(15) UNIQUE
);
COPY PhoneBook(first_name, last_name, phone_number)
FROM 'C:\Users\oleg_\Desktop\pp_2\lab_1\lab_10\sample1.csv'
DELIMITER ','
CSV HEADER;
INSERT INTO PhoneBook (first_name, last_name, phone_number)
VALUES ('Atila', 'Gridassov', '76677667'),
       ('Misha', 'Kazybek', '777777777');
UPDATE PhoneBook
SET first_name = 'Merey', phone_number = '76677667'
WHERE first_name = 'Katya' AND phone_number = '624636';
SELECT * FROM PhoneBook;
SELECT * FROM PhoneBook WHERE first_name = 'Attila';
SELECT * FROM PhoneBook WHERE phone_number = '76677667';
DELETE FROM PhoneBook WHERE phone_number = '777777777';
DELETE FROM PhoneBook WHERE first_name = 'Misha';