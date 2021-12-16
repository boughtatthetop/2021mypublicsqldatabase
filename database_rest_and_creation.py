import sqlite3
import pandas as pd 
import os
import csv

print('________run_________')

#-------To open the database------
#--- changed the database name to be able to easily distinguish between the .py itself 

dbase = sqlite3.connect('database_group43.db', isolation_level=None)
c=dbase.cursor()

#---TABLES---

#---Total number of tables are as follows: 

#---Company: These are the (actual customers) companies that use our service 
#---Customer: These are the customers of our customers 
#---CustomerAccount: This table will create a combination of Company-Customer
#---Products: These are the variety of avaliable products provided by our customers  
#---Subscriptions: This table keeps track of subscriptions 
#---Invocie: This table tracks the date, paid/no paid details 
#---Payments: This table keeps track of payments 

#---Table refresher
c.execute('''DROP TABLE IF EXISTS Companies''')
c.execute('''DROP TABLE IF EXISTS Company''')
c.execute('''DROP TABLE IF EXISTS Customers''')
c.execute('''DROP TABLE IF EXISTS Customer''')
c.execute('''DROP TABLE IF EXISTS ExchangeRate''')
c.execute('''DROP TABLE IF EXISTS Product''')
c.execute('''DROP TABLE IF EXISTS CustomerAccounts''')
c.execute('''DROP TABLE IF EXISTS Quote''')
c.execute('''DROP TABLE IF EXISTS Subscription''')
c.execute('''DROP TABLE IF EXISTS Invoice''')
c.execute('''DROP TABLE IF EXISTS Payment''')
print("All tables DROPPED")


#---Data types 
#---NULL
#---INTEGER
#---REAL
#---TEXT
#---BLOB
#---BOLEAN
#---


#---Company
 
c.execute('''
    CREATE TABLE IF NOT EXISTS Company(
        Company_ID                   INTEGER PRIMARY KEY AUTOINCREMENT,
        
        Company_Name                 TEXT NOT NULL,
        Company_AddressCountry       TEXT NOT NULL,
        Company_AddressState         TEXT,
        Company_AddressCity          TEXT NOT NULL,
        Company_AddressStreet        TEXT NOT NULL,
        Company_AddressNumber        TEXT NOT NULL,
        Company_AddressPostCode      TEXT NOT NULL,
        Company_VATID                TEXT NOT NULL, 
        Company_BankAccNumber        TEXT NOT NULL,
        Company_BankAccName          TEXT NOT NULL 
    )    
    ''')
print("Company table created")

#---the code below calls the following functions
#---Deletes Customer table
#---Creates table customer
#---Imports 1000 lines worth of customer data  

c.execute('''
    CREATE TABLE IF NOT EXISTS Customer(
        Customer_ID                  INTEGER PRIMARY KEY AUTOINCREMENT,
        
        Customer_Email               TEXT NOT NULL,
        Customer_Name                TEXT NOT NULL,
        Customer_Surname             TEXT NOT NULL,
        Customer_Birthdate           DATE,
        Customer_AddressCountry      TEXT NOT NULL,
        Customer_AddressState        TEXT,
        Customer_AddressCity         TEXT NOT NULL,
        Customer_AddressStreet       TEXT NOT NULL,
        Customer_AddressNumber       TEXT NOT NULL,
        Customer_AddressPostCode     TEXT, 
        Customer_CCNumber            TEXT NOT NULL  
    )    
    ''')
print("Customer table created")




#ExchangeRate   
#c.execute('''
#    CREATE TABLE IF NOT EXISTS ExchangeRate(
#        ExchangeRateID              INTEGER PRIMARY KEY,
#        CurrencyCode                TEXT,
#        Date                        DATE,
#        InEuro                      FLOAT
#    )
#    ''')
#print("ExchangeRate table created")

#Product 
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Product(
        Product_ID                  INTEGER PRIMARY KEY AUTOINCREMENT,
        
        Product_Name                TEXT NOT NULL,
        Product_CurrencyCode        TEXT NOT NULL,
        Product_Price               FLOAT NOT NULL,
        Company_ID                  INTEGER NOT NULL, 
        
        FOREIGN KEY(Company_ID)REFERENCES Company(Company_ID))    
    ''')
print("Product table created")

#CustomerAccount 
#dbase.execute('''
#    CREATE TABLE IF NOT EXISTS CustomerAccounts(
#        CustomerAccountID           INTEGER PRIMARY KEY AUTOINCREMENT,
#        Company_ID                  INTEGER,
#        Customer_ID                 INTEGER, 
#        FOREIGN KEY(Company_ID)REFERENCES Company(Company_ID)
#        FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID) 
#    )      
#    ''')
#print("CustomerAccounts table created")


#Subscription 
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Quote(
        Quote_ID                    INTEGER PRIMARY KEY AUTOINCREMENT,

        Quote_Quantity              INTEGER NOT NULL,
        Quote_Date                  DATE NOT NULL,
        Product_ID                  INTEGER NOT NULL,
        Customer_ID                 INTEGER NOT NULL,
        Company_ID                  INTEGER NOT NULL, 
        
        FOREIGN KEY(Company_ID)REFERENCES Company(Company_ID), 
        FOREIGN KEY(Product_ID) REFERENCES Product(Product_ID),
        FOREIGN KEY(Customer_ID) REFERENCES Quote(Customer_ID)
    )    
    ''')
print("Quote table created")

#Subscription
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Subscription(
        Subscription_ID             INTEGER PRIMARY KEY AUTOINCREMENT,
        
        Subscription_Active         BOOLEAN,
        Quote_ID                    INTEGER,
        Customer_ID                 INTEGER,
        Product_ID                  INTEGER,
        Company_ID                  INTEGER NOT NULL, 
        
        FOREIGN KEY(Company_ID)REFERENCES Company(Company_ID), 
        FOREIGN KEY(Quote_ID) REFERENCES Quote(Quote_ID),
        FOREIGN KEY(Customer_ID)REFERENCES Customer(Customer_ID),
        FOREIGN KEY(Product_ID)REFERENCES Product(Product_ID))    
    ''')
print("Subscription table created")

#Invoice 
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Invoice(
        Invoice_ID                  INTEGER PRIMARY KEY AUTOINCREMENT,
        
        Invoice_Paid                BOOLEAN,
        Invoice_PaidDate            DATE,      
        Customer_ID                 INTEGER,
        Subscription_ID             INTEGER,
        Company_ID                  INTEGER NOT NULL, 
        
        FOREIGN KEY(Company_ID)REFERENCES Company(Company_ID),
        FOREIGN KEY(Customer_ID) REFERENCES Customer(Customer_ID),
        FOREIGN KEY(Subscription_ID)REFERENCES Subscription(Subscription_ID)    )    
    ''')
print("Invoice table created")

#Payment 
#dbase.execute('''
#    CREATE TABLE IF NOT EXISTS Payment(
#        PaymentID                   INTEGER PRIMARY KEY AUTOINCREMENT,
#        InvoiceID                   INTEGER,
#        Date                        DATE,
#        Amount                      FLOAT,
#        FOREIGN KEY(InvoiceID) REFERENCES Invoice(InvoiceID)
#    )    
#    ''')
#print("Payment table created")
#-----------------

#---Functions of INSERT INTO---

#---Company

def record_a_new_company(
        Company_Name,           
        Company_AddressCountry,  
        Company_AddressState, 
        Company_AddressCity,
        Company_AddressStreet,
        Company_AddressNumber,
        Company_AddressPostCode,
        Company_VATID,           
        Company_BankAccNumber,
        Company_BankAccName):
    dbase.execute('''
        INSERT INTO Company(
        Company_Name,           
        Company_AddressCountry,  
        Company_AddressState, 
        Company_AddressCity,
        Company_AddressStreet,
        Company_AddressNumber,
        Company_AddressPostCode,
        Company_VATID,           
        Company_BankAccNumber,
        Company_BankAccName)
        VALUES(?,?,?,?,?,?,?,?,?,?)     
        '''
        ,
        (
        Company_Name,           
        Company_AddressCountry,  
        Company_AddressState, 
        Company_AddressCity,
        Company_AddressStreet,
        Company_AddressNumber,
        Company_AddressPostCode,
        Company_VATID,           
        Company_BankAccNumber,
        Company_BankAccName))

#---Customer

def record_a_new_customer( 
        Customer_Email,
        Customer_Name,           
        Customer_Surname,
        Customer_Birthdate,        
        Customer_AddressCountry, 
        Customer_AddressState,
        Customer_AddressCity,   
        Customer_AddressStreet,  
        Customer_AddressNumber,  
        Customer_AddressPostCode,
        Customer_CCNumber       
        ):
        dbase.execute('''
        INSERT INTO Customer(
        Customer_Email,
        Customer_Name,           
        Customer_Surname,
        Customer_Birthdate,        
        Customer_AddressCountry, 
        Customer_AddressState,
        Customer_AddressCity, 
        Customer_AddressStreet,  
        Customer_AddressNumber,  
        Customer_AddressPostCode,
        Customer_CCNumber)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)     
        '''
        ,
        (          
        Customer_Email,
        Customer_Name,           
        Customer_Surname,
        Customer_Birthdate,         
        Customer_AddressCountry, 
        Customer_AddressState,
        Customer_AddressCity,   
        Customer_AddressStreet,  
        Customer_AddressNumber,  
        Customer_AddressPostCode,
        Customer_CCNumber))

#---CustomerAccounts
#def record_a_new_customeraccount(
#        Company_ID,        Customer_ID
#        ):
#        dbase.execute('''
#        INSERT INTO CustomerAccounts(
#        Company_ID,        Customer_ID 
#        )
#        VALUES(?,?)      
#        '''
#        ,
#        (
#        Company_ID,        Customer_ID
#        ))




#def ExchangeRate_recorder( 
#        CurrencyCode,
#        Date  
#        ):
#        dbase.execute('''
#        INSERT INTO ExchangeRate(
#            CurrencyCode,
#            Date  
#        )
#        VALUES(?,?)     
#        '''
#        ,
#        (          
#        CurrencyCode,
#        Date,        
#       ))

def Product_recorder( 
        Product_Name,  
        Product_CurrencyCode,     
        Product_Price,
        Company_ID   
        ):  
        dbase.execute('''
        INSERT INTO Product(
            Product_Name,  
            Product_CurrencyCode,     
            Product_Price,
            Company_ID
        )
        VALUES(?,?,?,?)     
        '''
        ,
        (          
        Product_Name,  
        Product_CurrencyCode,     
        Product_Price,
        Company_ID))

def Quote_recorder( 
        Quote_Quantity,
        Quote_Date,
        Product_ID,
        Customer_ID,
        Company_ID   
        ):  
        dbase.execute('''
        INSERT INTO Quote(
        Quote_Quantity,
        Quote_Date,
        Product_ID,
        Customer_ID,
        Company_ID  
        )
        VALUES(?,?,?,?,?)     
        '''
        ,
        (          
        Quote_Quantity,
        Quote_Date,
        Product_ID,
        Customer_ID,
        Company_ID))

def Subscription_recorder( 
        Subscription_Active, 
        Quote_ID,   
        Customer_ID,
        Product_ID,
        Company_ID  
        ):  
        dbase.execute('''
        INSERT INTO Subscription(
        Subscription_Active, 
        Quote_ID,   
        Customer_ID,
        Product_ID,
        Company_ID 

        )
        VALUES(?,?,?,?,?)     
        '''
        ,
        (  
        Subscription_Active, 
        Quote_ID,   
        Customer_ID,
        Product_ID,
        Company_ID           
        ))

def Invoice_recorder( 
        Invoice_Paid, 
        Invoice_PaidDate,   
        Customer_ID,
        Subscription_ID,
        Company_ID
        ):  
        dbase.execute('''
        INSERT INTO Invoice(
        Invoice_Paid, 
        Invoice_PaidDate,   
        Customer_ID,
        Subscription_ID,
        Company_ID 
        )
        VALUES(?,?,?,?,?)     
        '''
        ,
        ( 
        Invoice_Paid, 
        Invoice_PaidDate,   
        Customer_ID,
        Subscription_ID,
        Company_ID
        ))

#def Invocie_recorder( 
#        Date, 
#        Amount,
#        ):  
#        dbase.execute('''
#        INSERT INTO Invoice(
#            Date, 
#            Amount,   
#        )
#        VALUES(?,?)     
#        '''
#        ,
#        ( 
#        Date, 
#        Amount,
#        ))

#---Filling the database 
#---You will need to populate your database to be able to test your code 
#---create a variable to be able to write down all the companies at once
Company_List=[

    ('company1','country1','state1','city1','street1','number1','postcode1','vatid1','bankaccount1', 'bank1')
    ]

#--- to import data in bulk 

for Company_Name, Company_AddressCountry,Company_AddressState, Company_AddressCity,Company_AddressStreet,Company_AddressNumber,Company_AddressPostCode,Company_VATID, Company_BankAccNumber, Company_BankAccName in Company_List:
    record_a_new_company(Company_Name, Company_AddressCountry,Company_AddressState, Company_AddressCity,Company_AddressStreet,Company_AddressNumber,Company_AddressPostCode,Company_VATID, Company_BankAccNumber,Company_BankAccName)
print('companies imported')


Customer_List=[
    ('email1@gmail.com','name1', 'surname1','birthday1' , 'country1', None, 'city1', 'street1', 'number1', 'postcode1', '56022266748153064')]



for Customer_Email,Customer_Name, Customer_Surname, Customer_Birthdate, Customer_AddressCountry, Customer_AddressState, Customer_AddressCity, Customer_AddressStreet, Customer_AddressNumber, Customer_AddressPostCode, Customer_CCNumber in Customer_List:
    record_a_new_customer(Customer_Email,Customer_Name, Customer_Surname, Customer_Birthdate, Customer_AddressCountry, Customer_AddressState, Customer_AddressCity, Customer_AddressStreet, Customer_AddressNumber, Customer_AddressPostCode, Customer_CCNumber)
print('customers imported')




#CustomerAccounts population
#CustomerAccounts_List=[
#    (1,2),
#    (3,2),
#    (4,4),
#    (6,14),
#    (2,2),
#    (1,3),
#    (1,7),
#    (1,1),
#    (5,3),
#    (6,2),
#    ]
#for Company_ID,Customer_ID in CustomerAccounts_List: 
#    record_a_new_customeraccount(Company_ID,Customer_ID)




Product_List=[
    ('product1','GBP',1,1)
]
for Product_Name, Product_CurrencyCode, Product_Price, Company_ID in Product_List:
    Product_recorder(Product_Name, Product_CurrencyCode, Product_Price, Company_ID)


Quote_List=[
    (1,"2021-01-01",1,1,1)     
]
for Quote_Quantity, Quote_Date, Product_ID, Customer_ID,Company_ID in Quote_List:
    Quote_recorder(Quote_Quantity, Quote_Date, Product_ID, Customer_ID,Company_ID)



Subscription_List=[
    (1,1,1,1,1)    
]
for Subscription_Active,Quote_Quantity, Customer_ID, Product_ID,Company_ID in Subscription_List:
    Subscription_recorder(Subscription_Active,Quote_Quantity, Customer_ID, Product_ID,Company_ID)


Invoice_List=[
    (1,"2021-1-1",1,1,1)]
for Invoice_Paid, Invoice_PaidDate, Customer_ID, Subscription_ID,Company_ID in Invoice_List:
    Invoice_recorder(Invoice_Paid, Invoice_PaidDate, Customer_ID, Subscription_ID,Company_ID)



#-------------To close the database-------------
dbase.close()
print('database closed')
