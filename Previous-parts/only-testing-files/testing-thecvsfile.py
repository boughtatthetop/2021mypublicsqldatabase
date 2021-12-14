#https://www.stuartsplace.com/computing/programming/python/python-and-sqlite-importing-data/


import csv
import os
import sqlite3

filePath = 'C:\Users\Eghez\OneDrive - Université Libre de Bruxelles\Fall 21\GESTS482 The Digital firm\GESTS482 Project - Group 43\project43\Customerdatasource.csv.csv'

database = 'C:\Users\Eghez\OneDrive - Université Libre de Bruxelles\Fall 21\GESTS482 The Digital firm\GESTS482 Project - Group 43\project43\database_group43.db'

connect = None

if not os.path.isfile(database):
    print("Error locating database.")
    quit()
try:
    connect = sqlite3.connect(database)

except sqlite3.DatabaseError as e:
    print("Database connection unsuccessful.")
    quit()

if os.path.isfile(filePath):
    cursor = connect.cursor()
    reader = csv.DictReader(open(filePath))
    recordCount = 0
    for row in reader:
        sqlInsert = \
            "INSERT INTO ExchangeRate (CurrencyCode, Date, InEuro)  \
             VALUES (?, ?, ?)"
        try:
            cursor.execute(sqlInsert, (row['CurrencyCode'],
                                       row['Date'],
                                       row['InEuro']))
            connect.commit()
            recordCount += 1

