import sqlite3
print('________run_________')

#-------To open the database------
dbase = sqlite3.connect('group43.db', isolation_level=None)

#---TABLES---
dbase.execute('''DROP TABLE IF EXISTS Companies''')
dbase.execute('''DROP TABLE IF EXISTS Customers''')
dbase.execute('''DROP TABLE IF EXISTS ExchangeRates''')
dbase.execute('''DROP TABLE IF EXISTS Products''')
dbase.execute('''DROP TABLE IF EXISTS CustomerAccounts''')
dbase.execute('''DROP TABLE IF EXISTS Quotes''')
dbase.execute('''DROP TABLE IF EXISTS Subscriptions''')
dbase.execute('''DROP TABLE IF EXISTS Invoices''')
dbase.execute('''DROP TABLE IF EXISTS Paymments''')
#Company table
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Companies(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        AddressCountry TEXT NOT NULL,
        AddressState TEXT NOT NULL,
        AddressCity TEXT NOT NULL,
        AddressStreet TEXT NOT NULL,
        AddressNumber TEXT NOT NULL,
        AddressPostCode TEXT NOT NULL,
        TotSubscriptions INTEGER NOT NULL,
        VATID TEXT NOT NULL, 
        BankAcc TEXT NOT NULL  
    )    
    ''')
#Customer table
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Customers(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Surname TEXT NOT NULL,
        Email TEXT NOT NULL,
        AddressCountry TEXT NOT NULL,
        AddressState TEXT NOT NULL,
        AddressCity TEXT NOT NULL,
        AddressStreet TEXT NOT NULL,
        AddressNumber TEXT NOT NULL,
        AddressPostCode TEXT NOT NULL, 
        CCNumber TEXT NOT NULL  
    )    
    ''')
#ExchangeRate table    
dbase.execute('''
    CREATE TABLE IF NOT EXISTS ExchangeRates(
        CurrencyCode CHAR PRIMARY KEY,
        Date DATE NOT NULL,
        InEuro FLOAT NOT NULL
    )
    ''')
#Product table
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CurrencyCode CHAR NOT NULL,
        ProductName TEXT NOT NULL,
        PriceEUR FLOAT NOT NULL,
        PriceLocal FLOAT NOT NULL,
        CompanyID INT NOT NULL, 
        FOREIGN KEY(CurrencyCode) REFERENCES ExchangeRates(CurrencyCode)
        FOREIGN KEY(CompanyID) REFERENCES Companies(ID)
    )    
    ''')
#CustomerAccount table
dbase.execute('''
    CREATE TABLE IF NOT EXISTS CustomerAccounts(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CompanyID INTEGER,
        CustomerID INTEGER, 
        FOREIGN KEY(CompanyID) REFERENCES Companies(ID),
        FOREIGN KEY(CustomerID) REFERENCES Customers(ID) 
    )      
    ''')
#Quote table
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Quotes(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Date DATE,
        CustomerAccountID INT NOT NULL,
        Accepted BOOLEAN DEFAULT 0,
        FOREIGN KEY(CustomerAccountID) REFERENCES CustomerAccounts(ID)
    )
    ''')
#Subscription table
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Subscriptions(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerAccountID INT,
        ProductID INT,
        QuoteID INT,
        Quantity INT NOT NULL,
        Active BOOLEAN DEFAULT 0,
        StartDate DATE,
        EndDate DATE,
        FOREIGN KEY(CustomerAccountID) REFERENCES CustomerAccounts(ID),
        FOREIGN KEY(ProductID) REFERENCES Products(ID),
        FOREIGN KEY(QuoteID) REFERENCES Quotes(ID)
    )    
    ''')
#Invoice table
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Invoices(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerAccountID INT NOT NULL,
        Date DATE,
        DueDate DATE,
        Paid BOOLEAN DEFAULT 0,
        TotalDueEuro FLOAT,
        FOREIGN KEY(CustomerAccountID) REFERENCES CustomerAccounts(ID)
    )    
    ''')
#Payment table
dbase.execute('''
    CREATE TABLE IF NOT EXISTS Payments(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        InvoiceID INT,
        Date DATE,
        Amount FLOAT,
        FOREIGN KEY(InvoiceID) REFERENCES Invoices(ID)
    )    
    ''')
