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
c.execute('''DROP TABLE IF EXISTS Invocie''')
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
        
        FOREIGN KEY(Product_ID) REFERENCES Product(Product_ID),
        FOREIGN KEY(Quote_ID) REFERENCES Quote(Quote_ID)
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

        FOREIGN KEY(Quote_ID) REFERENCES Quote(Quote_ID),
        FOREIGN KEY(Customer_ID)REFERENCES Customer(Customer_ID))    
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
        Customer_ID   
        ):  
        dbase.execute('''
        INSERT INTO Quote(
        Quote_Quantity,
        Quote_Date,
        Product_ID,
        Customer_ID  
        )
        VALUES(?,?,?,?)     
        '''
        ,
        (          
        Quote_Quantity,
        Quote_Date,
        Product_ID,
        Customer_ID))

def Subscription_recorder( 
        Subscription_Active, 
        Quote_ID,   
        Customer_ID  
        ):  
        dbase.execute('''
        INSERT INTO Subscription(
        Subscription_Active, 
        Quote_ID,   
        Customer_ID 
        )
        VALUES(?,?,?)     
        '''
        ,
        (  
        Subscription_Active, 
        Quote_ID,   
        Customer_ID           
        ))

def Invoice_recorder( 
        Invoice_Paid, 
        Invoice_PaidDate,   
        Customer_ID,
        Subscription_ID
        ):  
        dbase.execute('''
        INSERT INTO Invoice(
        Invoice_Paid, 
        Invoice_PaidDate,   
        Customer_ID,
        Subscription_ID 
        )
        VALUES(?,?,?,?)     
        '''
        ,
        ( 
        Invoice_Paid, 
        Invoice_PaidDate,   
        Customer_ID,
        Subscription_ID
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

    ('Meta','USA','LA','San diego','FB street','368','1020','1364763834','128361726317823', 'Bank of America'),
    ('Microsoft','USA','LA','San diego','MSFT street','369','1021','1364763835','128361726317824', 'Bank of America'),
    ('Google','USA','LA','San diego','GOOGL street','370','1022','1364763836','128361726317824', 'Bank of America'),
    ('Nvidia','USA','LA','San diego','NVDA street','371','1023','1364763837','128361726317825', 'Bank of America'),
    ('Tesla','USA','TX','Houston','TSLA street','372','1024','1364763838','128361726317826', 'Bank of America'),
    ('Oracle','USA','LA','San diego','ORCL street','373','1025','1364763839','128361726317827', 'Bank of America'),
    ('Apple','USA','LA','San diego','AAPL street','374','1026','1364763840','128361726317828', 'Bank of America'),
    ('Spotify','Sweden','Stockholm','Stockholm','Syndrome street','375','1027','1364763841','SE128361726317823', 'Bank of Sweden'),
    ('Uber','USA','LA','San diego','UBER street','376','1028','1364763842','128361726317829', 'Bank of America'),
    ('Lyft','USA','LA','San diego','LYFT street','377','1029','1364763843','128361726317830', 'Bank of America'),
    ('Netflix','USA','LA','San diego','NFLX street','378','1030','1364763844','128361726317831', 'Bank of America'),
    ('Klarna','Sweden','Stockholm','Stockholm','Syndrome street','379','1031','1364763845','SE128361726317824', 'Bank of Sweden'),
    ('Dell','USA','LA','San diego','DELL street','380','1032','1364763846','128361726317832', 'Bank of America'),
    ('UCLA','USA','LA','San diego','UCLA street','381','1033','1364763847','128361726317833', 'Bank of America')
    ]
print("Company_List type : "+ str(type(Company_List)))
#--- to import data in bulk 

for Company_Name, Company_AddressCountry,Company_AddressState, Company_AddressCity,Company_AddressStreet,Company_AddressNumber,Company_AddressPostCode,Company_VATID, Company_BankAccNumber, Company_BankAccName in Company_List:
    record_a_new_company(Company_Name, Company_AddressCountry,Company_AddressState, Company_AddressCity,Company_AddressStreet,Company_AddressNumber,Company_AddressPostCode,Company_VATID, Company_BankAccNumber,Company_BankAccName)
print('companies imported')


Customer_List=[
    ('email1@gmail.com','Wat', 'Myring','1997-1-1' , 'Thailand', None, 'Watthana Nakhon', 'Fordem', '54659', '34230', '56022266748153064'),
    ('email2@gmail.com','Brook', 'Riby','1997-1-1' , 'Portugal', 'Viseu', 'Oliveirinha', 'South', '4', '3430-393', '3536866970807559'),
    ('email3@gmail.com','Laureen', 'Hearsum','1997-1-1' , 'Indonesia', None, 'Margotuhu Kidul', 'Lakewood', '2664', None, '675967718400894959'),
    ('email4@gmail.com','Kristal', 'Trenaman','1997-1-1' , 'Peru', None, 'Iberia', 'Londonderry', '666', None, '4911927251141051246'),
    ('email5@gmail.com','Thayne', 'Blunsen','1997-1-1' , 'Colombia', None, 'Chipaque', 'Barnett', '02', '251808', '4041591408090802'),
    ('email6@gmail.com','Marlyn', 'Guiso', '1997-1-1' ,'Indonesia', None, 'Banjaranyar', 'Jay', '29311', None, '3543136510685001'),
    ('email7@gmail.com','Camille', 'Garrard', '1997-1-1' ,'Argentina', None, 'Loreto', 'Harper', '3', '3483', '3556920445064893'),
    ('email8@gmail.com','Glenda', 'Aitchison', '1997-1-1' ,'Canada', 'Ontario', 'Amherstburg', 'Talisman', '7', 'N9V', '56022103672145941'),
    ('email9@gmail.com','Lenora', 'Birnie', '1997-1-1' ,'Sweden', 'Jönköping', 'Habo', 'Ryan', '4111', '566 24', '6382656959235858'),
    ('email10@gmail.com','Hercule', 'Scollan', '1997-1-1' ,'Finland', None, 'Längelmäki', 'Hansons', '87', '35400', '337941027101905'),
    ('email11@gmail.com','Constantine', 'Ferrarello', '1997-1-1' ,'Indonesia', None, 'Gawanan', 'Independence', '6', None, '30391983169217'),
    ('email12@gmail.com','Kacie', 'Courage', '1997-1-1' ,'Sweden', 'Västmanland', 'Västerås', 'Hintze', '3140', '721 19', '5602249221856159091'),
    ('email13@gmail.com','Heindrick', 'Harvison', '1997-1-1' ,'Colombia', None, 'Combita', 'Pepper Wood', '31', '150208', '4405412890894504'),
    ('email14@gmail.com','Julietta', 'Brockie', '1997-1-1' ,'Thailand', None, 'Si Narong', 'Fallview', '03840', '34000', '56022343096833660'),
    ('email15@gmail.com','Selby', 'Chidlow', '1997-1-1' ,'Indonesia', None, 'Sukabumi', 'Lighthouse Bay', '35718', None, '3561611257886860'),
    ('email51@gmail.com','Lottie', 'Everil','1997-1-1' , 'Indonesia', None, 'Bojongnangka', 'Burning Wood', '8', None, '3550982996750961'),
    ('email31@gmail.com','Sherm', 'Caroli', '1997-1-1' ,'China', None, 'Muzi', 'Northfield', '5959', None, '201894388602867'),
    ('email31@gmail.com','Pryce', 'Ratcliffe','1997-1-1' , 'Indonesia', None, 'Babantar', 'Marquette', '23', None, '5452721688390965'),
    ('email15@gmail.com','Chaim', 'Dwire', '1997-1-1' ,'Russia', None, 'Krasnogvardeyets', 'Sugar', '40854', '102469', '633484956762995641'),
    ('email13@gmail.com','Ginny', 'Kleewein', '1997-1-1' ,'Belarus', None, 'Loyew', 'Rieder', '05', None, '3580430987534600'),
    ('email15@gmail.com','Janaya', 'Fidelus', '1997-1-1' ,'Philippines', None, 'Tartaro', 'Mcbride', '17', '2307', '5602217254492698'),
    ('email13@gmail.com','Hinda', 'Pointing', '1997-1-1' ,'Brazil', None, 'Igaraçu do Tietê', 'Victoria', '27', '17350-000', '3559947835151565'),
    ('email135@gmail.com','Georgie', 'Drydale', '1997-1-1' ,'Indonesia', None, 'Sukamaju', 'Dryden', '546', None, '4017958478018379'),
    ('email1355@gmail.com','Edlin', 'Dondon','1997-1-1' , 'Gambia', None, 'Bambali', 'Bayside', '08209', None, '4844360692236524'),
    ('email131@gmail.com','Kinna', 'Earey', '1997-1-1' ,'Senegal', None, 'Richard-Toll', 'Nobel', '71', None, '30343069592978'),
    ('email13524@gmail.com','Skye', 'McKenzie', '1997-1-1' ,'Russia', None, 'Mikhaylovka', 'Melrose', '6', '613384', '677176040570466176'),
    ('email14545@gmail.com','Arlan', 'Rentcome', '1997-1-1' ,'China', None, 'Yangxi', 'Autumn Leaf', '44', None, '4508428266017039')]
print("Customer_List type : "+ str(type(Customer_List)))


for Customer_Email,Customer_Name, Customer_Surname, Customer_Birthdate, Customer_AddressCountry, Customer_AddressState, Customer_AddressCity, Customer_AddressStreet, Customer_AddressNumber, Customer_AddressPostCode, Customer_CCNumber in Customer_List:
    record_a_new_customer(Customer_Email,Customer_Name, Customer_Surname, Customer_Birthdate, Customer_AddressCountry, Customer_AddressState, Customer_AddressCity, Customer_AddressStreet, Customer_AddressNumber, Customer_AddressPostCode, Customer_CCNumber)
print('customers imported')

query=dbase.execute('''SELECT * FROM Company''').fetchall()
print(query)


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
    ('Office365','EUR',25,3),
    ('Office365','TRY',42,3),
    ('Office365','USD',25,3),
    ('Netflix','USD',25,3),
    ('Office365','EUR',32,3),
    ('Office365','GBP',25,2),
    ('Spotify','GBP',25,1),
    ('Office365','GBP',25,3),
    ('Youtube','GBP',66,6),
    ('Office365','EUR',25,3),
    ('BlaBla','EUR',99,8)
]
for Product_Name, Product_CurrencyCode, Product_Price, Company_ID in Product_List:
    Product_recorder(Product_Name, Product_CurrencyCode, Product_Price, Company_ID)


Quote_List=[
    (2,"2021-1-1",2,4),
    (2,"2021-1-1",2,4),
    (4,"2021-1-1",2,4),
    (5,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),   
    (1,"2021-1-1",2,4)     
]
for Quote_Quantity, Quote_Date, Product_ID, Customer_ID in Quote_List:
    Quote_recorder(Quote_Quantity, Quote_Date, Product_ID, Customer_ID)



Subscription_List=[
    (1,2,4),
    (0,2,4),
    (1,2,4),
    (0,2,4),
    (1,2,4),
    (1,2,4),
    (1,2,4),
    (1,2,4),
    (1,2,4),
    (1,2,4),   
    (1,2,4)     
]
for Subscription_Active,Quote_Quantity, Customer_ID in Subscription_List:
    Subscription_recorder(Subscription_Active,Quote_Quantity, Customer_ID)


Invoice_List=[
    (1,"2021-1-1",2,4),
    (0,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (0,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),
    (1,"2021-1-1",2,4),   
    (1,"2021-1-1",2,4)     
]
for Invoice_Paid, Invoice_PaidDate, Customer_ID, Subscription_ID in Invoice_List:
    Invoice_recorder(Invoice_Paid, Invoice_PaidDate, Customer_ID, Subscription_ID)



#-------------To close the database-------------
dbase.close()
print('database closed')
