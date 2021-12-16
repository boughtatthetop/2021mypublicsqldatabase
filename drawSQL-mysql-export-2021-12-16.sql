CREATE TABLE `Customer`(
    `Customer_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Customer_Email` TEXT NOT NULL,
    `Customer_Name` TEXT NOT NULL,
    `Customer_Surname` TEXT NOT NULL,
    `Customer_AddressCountry` TEXT NOT NULL,
    `Customer_AddressState` TEXT NOT NULL,
    `Customer_AddressCity` TEXT NOT NULL,
    `Customer_AdressStreet` TEXT NOT NULL,
    `Customer_AddressNumber` TEXT NOT NULL,
    `Customer_AddressPostCode` TEXT NOT NULL,
    `Customer_CCNumber` TEXT NOT NULL
);
ALTER TABLE
    `Customer` ADD PRIMARY KEY `customer_customer_id_primary`(`Customer_ID`);
CREATE TABLE `Company`(
    `Company_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Company_Name` TEXT NOT NULL,
    `Company_AddressCountry` TEXT NOT NULL,
    `Company_AddressState` TEXT NOT NULL,
    `Company_AddressCity` TEXT NOT NULL,
    `Company_AddressNumber` TEXT NOT NULL,
    `Company_AddressPostCode` TEXT NOT NULL,
    `Company_VATID` TEXT NOT NULL,
    `Company_BankAccNumber` TEXT NOT NULL,
    `Company_BankAccName` TEXT NOT NULL
);
ALTER TABLE
    `Company` ADD PRIMARY KEY `company_company_id_primary`(`Company_ID`);
CREATE TABLE `Product`(
    `Product_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Product_Name` TEXT NOT NULL,
    `Product_CurrencyCode` TEXT NOT NULL COMMENT 'ex : USD, GBP, EUR...',
    `Product_Price` DOUBLE(8, 2) NOT NULL,
    `Company_ID` INT NOT NULL
);
ALTER TABLE
    `Product` ADD PRIMARY KEY `product_product_id_primary`(`Product_ID`);
CREATE TABLE `Quote`(
    `Quote_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Quote_Quantity` INT NOT NULL,
    `Quote_Date` TEXT NOT NULL,
    `ProductID` INT NOT NULL COMMENT 'Price + Prodcut name + CurrencyCode',
    `Customer_ID` INT NOT NULL,
    `Company_ID` INT NOT NULL
);
ALTER TABLE
    `Quote` ADD PRIMARY KEY `quote_quote_id_primary`(`Quote_ID`);
CREATE TABLE `Invoice`(
    `Invoice_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Invoice_Paid` TINYINT(1) NOT NULL,
    `Invoice_PaidDate` TEXT NOT NULL,
    `Customer_ID` INT NOT NULL,
    `Subscription_ID` INT NOT NULL,
    `Company_ID` INT NOT NULL
);
ALTER TABLE
    `Invoice` ADD PRIMARY KEY `invoice_invoice_id_primary`(`Invoice_ID`);
CREATE TABLE `Subscription`(
    `Subscription_ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Subscription_Active` TINYINT(1) NOT NULL,
    `Quote_ID` INT NOT NULL,
    `Customer_ID` INT NOT NULL,
    `Product_ID` INT NOT NULL,
    `Company_ID` INT NOT NULL
);
ALTER TABLE
    `Subscription` ADD PRIMARY KEY `subscription_subscription_id_primary`(`Subscription_ID`);
ALTER TABLE
    `Quote` ADD CONSTRAINT `quote_customer_id_foreign` FOREIGN KEY(`Customer_ID`) REFERENCES `Customer`(`Customer_ID`);
ALTER TABLE
    `Invoice` ADD CONSTRAINT `invoice_customer_id_foreign` FOREIGN KEY(`Customer_ID`) REFERENCES `Customer`(`Customer_ID`);
ALTER TABLE
    `Subscription` ADD CONSTRAINT `subscription_customer_id_foreign` FOREIGN KEY(`Customer_ID`) REFERENCES `Customer`(`Customer_ID`);
ALTER TABLE
    `Subscription` ADD CONSTRAINT `subscription_product_id_foreign` FOREIGN KEY(`Product_ID`) REFERENCES `Product`(`Product_ID`);
ALTER TABLE
    `Product` ADD CONSTRAINT `product_company_id_foreign` FOREIGN KEY(`Company_ID`) REFERENCES `Company`(`Company_ID`);
ALTER TABLE
    `Subscription` ADD CONSTRAINT `subscription_quote_id_foreign` FOREIGN KEY(`Quote_ID`) REFERENCES `Quote`(`Quote_ID`);
ALTER TABLE
    `Quote` ADD CONSTRAINT `quote_productid_foreign` FOREIGN KEY(`ProductID`) REFERENCES `Product`(`Product_ID`);
ALTER TABLE
    `Invoice` ADD CONSTRAINT `invoice_subscription_id_foreign` FOREIGN KEY(`Subscription_ID`) REFERENCES `Subscription`(`Subscription_ID`);