-- Matt DeMarco

-- Insert data into CUSTOMER table
INSERT INTO CUSTOMER VALUES (1, 'Alex Fink', 'alex.fink@gmail.com', '123-456-7890');
INSERT INTO CUSTOMER VALUES (2, 'Bobby McCauley', 'b_mcc@gmail.com', '234-567-8901');
INSERT INTO CUSTOMER VALUES (3, 'Alonso Lacayo', 'lacayo.j@yahoo.com', '345-678-9012');
INSERT INTO CUSTOMER VALUES (4, 'Matt DeMarco', 'md18@bing.com', '456-789-0123');
INSERT INTO CUSTOMER VALUES (5, 'Ricky Bobby', 'iamfast@outlook.com', '567-890-1234');
INSERT INTO CUSTOMER VALUES (6, 'Chris Green', 'chris.green@gmail.com', '678-901-2345');
INSERT INTO CUSTOMER VALUES (7, 'Sarah White', 'sarah.white@gmail.com', '789-012-3456');
INSERT INTO CUSTOMER VALUES (8, 'Michael Black', 'michael.black@gmail.com', '890-123-4567');
INSERT INTO CUSTOMER VALUES (9, 'Laura Blue', 'laura.blue@gmail.com', '901-234-5678');
INSERT INTO CUSTOMER VALUES (10, 'Daniel Red', 'daniel.red@gmail.com', '012-345-6789');

-- Insert data into PRODUCT table
INSERT INTO PRODUCT VALUES (101, 'Shirt', 19.99, 'M', '123 Main St, City A', 'Nike', 'Medium', 'Blue');
INSERT INTO PRODUCT VALUES (102, 'Pants', 39.99, 'F', '456 Elm St, City B', 'ReBok', 'Large', 'Black');
INSERT INTO PRODUCT VALUES (103, 'Shoes', 59.99, 'M', '789 Oak St, City C', 'Adidas', 'Size 10', 'White');
INSERT INTO PRODUCT VALUES (104, 'Hat', 14.99, 'F', '321 Pine St, City D', 'Puma', 'One Size', 'Red');
INSERT INTO PRODUCT VALUES (105, 'Jacket', 79.99, 'M', '654 Cedar St, City E', 'North Face', 'Large', 'Green');
INSERT INTO PRODUCT VALUES (106, 'Socks', 5.99, 'M', '789 Birch St, City F', 'Nike', 'One Size', 'Gray');
INSERT INTO PRODUCT VALUES (107, 'T-Shirt', 12.99, 'F', '321 Maple St, City G', 'Clover', 'Small', 'Yellow');
INSERT INTO PRODUCT VALUES (108, 'Jeans', 45.99, 'M', '654 Spruce St, City H', 'Levis', 'Medium', 'Blue');
INSERT INTO PRODUCT VALUES (109, 'Scarf', 24.99, 'F', '987 Willow St, City I', 'Aritzia', 'One Size', 'Purple');
INSERT INTO PRODUCT VALUES (110, 'Sneakers', 74.99, 'M', '123 Poplar St, City J', 'Vans', 'Size 11', 'Black');

-- Insert data into CART table
INSERT INTO CART VALUES (201, 1, 101, 19.99, 'Credit Card', '123 Main St, City A');
INSERT INTO CART VALUES (202, 2, 102, 39.99, 'PayPal', '456 Elm St, City B');
INSERT INTO CART VALUES (203, 3, 103, 59.99, 'Debit Card', '789 Oak St, City C');
INSERT INTO CART VALUES (204, 4, 104, 14.99, 'Gift Card', '321 Pine St, City D');
INSERT INTO CART VALUES (205, 5, 105, 79.99, 'Credit Card', '654 Cedar St, City E');
INSERT INTO CART VALUES (206, 6, 106, 5.99, 'Credit Card', '789 Birch St, City F');
INSERT INTO CART VALUES (207, 7, 107, 12.99, 'PayPal', '321 Maple St, City G');
INSERT INTO CART VALUES (208, 8, 108, 45.99, 'Debit Card', '654 Spruce St, City H');
INSERT INTO CART VALUES (209, 9, 109, 24.99, 'Gift Card', '987 Willow St, City I');
INSERT INTO CART VALUES (210, 10, 110, 74.99, 'Credit Card', '123 Poplar St, City J');


-- Insert data into ADDRESS table
INSERT INTO ADDRESS VALUES (301, 123, 'Lavalette', 'Main St', 12345, 'NJ', 1);
INSERT INTO ADDRESS VALUES (302, 456, 'Wildwood', 'Elm St', 23456, 'NJ', 2);
INSERT INTO ADDRESS VALUES (303, 789, 'Cape May', 'Oak St', 34567, 'NJ', 3);
INSERT INTO ADDRESS VALUES (304, 321, 'Manchester', 'Pine St', 45678, 'NH', 4);
INSERT INTO ADDRESS VALUES (305, 654, 'San Francisco', 'Cedar St', 56789, 'CA', 5);
INSERT INTO ADDRESS VALUES (306, 789, 'Villanova', 'Birch St', 67890, 'PA', 6);
INSERT INTO ADDRESS VALUES (307, 321, 'Kansas City', 'Maple St', 78901, 'MI', 7);
INSERT INTO ADDRESS VALUES (308, 654, 'Pittsburgh', 'Spruce St', 89012, 'PA', 8);
INSERT INTO ADDRESS VALUES (309, 987, 'Danbury', 'Willow St', 90123, 'CT', 9);
INSERT INTO ADDRESS VALUES (310, 123, 'Bar Harbor', 'Poplar St', 12345, 'ME', 10);


-- Insert data into PAYMENT table
INSERT INTO PAYMENT VALUES (401, 1234, 1111222233334444, 'Credit Card', NULL, 1);
INSERT INTO PAYMENT VALUES (402, NULL, NULL, 'PayPal', NULL, 2);
INSERT INTO PAYMENT VALUES (403, 5678, 5555666677778888, 'Debit Card', NULL, 3);
INSERT INTO PAYMENT VALUES (404, NULL, NULL, 'Gift Card', 999999, 4);
INSERT INTO PAYMENT VALUES (405, 9012, 9999888877776666, 'Credit Card', NULL, 5);
INSERT INTO PAYMENT VALUES (406, 2345, 1111333344445555, 'Credit Card', NULL, 6);
INSERT INTO PAYMENT VALUES (407, NULL, NULL, 'PayPal', NULL, 7);
INSERT INTO PAYMENT VALUES (408, 6789, 2222444455556666, 'Debit Card', NULL, 8);
INSERT INTO PAYMENT VALUES (409, NULL, NULL, 'Gift Card', 888888, 9);
INSERT INTO PAYMENT VALUES (410, 3456, 3333555566667777, 'Credit Card', NULL, 10);




