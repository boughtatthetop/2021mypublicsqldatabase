import sqlite3 

dbase=sqlite3.connect('database_group43.db', isolation_level=None)

values_dict={
 "Product_Name"               : "TestProduct",
 "Product_CurrencyCode"       : "GBP",
 "Product_Price"              : "20",
 "Company_ID"                 : "1",
}



query_product='''
            SELECT Product_ID FROM Product
            WHERE Product_Name = {}
            AND Product_CurrencyCode = {}
            AND Product_Price = {}
            AND Company_ID = {}
            '''.format("testproduct","GBP","20","1")

print(query_product)
dbase.execute(query_product)
print(dbase.execute(query_product).fetchall())
