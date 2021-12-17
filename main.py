from os import truncate
import sqlite3
from sqlite3.dbapi2 import connect
from typing import Counter
from fastapi import FastAPI, Request
import uvicorn
import LUHN as L
import pandas as pd
import datetime
import json
import requests
from database_rest_and_creation import Subscription_ID
from exchangerateAPI import converter 

app = FastAPI()

# Router
@app.get("/")
def root():
  return {"message": "It works !"}











#--------REQUIREMENT NUMBER 1 = COMPANY CREATE ACCOUNT ------------------ #--------REQUIREMENT NUMBER 1 = COMPANY CREATE ACCOUNT ------------------ #--------REQUIREMENT NUMBER 1 = COMPANY CREATE ACCOUNT ------------------ 
#--------REQUIREMENT NUMBER 1 = COMPANY CREATE ACCOUNT ------------------ 
#--------REQUIREMENT NUMBER 1 = COMPANY CREATE ACCOUNT ------------------ 
#--------REQUIREMENT NUMBER 1 = COMPANY CREATE ACCOUNT ------------------ 

@app.post("/create_company_account")
async def create_company_account(payload: Request):
  values_dict = await payload.json()
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)
  companies_with_this_vat=dbase.execute('''
    SELECT Company_ID FROM Company
    WHERE Company_VATID=?
    ''',(str(values_dict['Company_VATID']),))
  query_vatid=(companies_with_this_vat.fetchall())
  print(query_vatid)
  print(str(values_dict['Company_VATID']))
  if query_vatid:
    print("Company is already registered")
    return "Company is already registered"

  aaaa=dbase.execute('''INSERT INTO Company(
                      Company_Name,
                      Company_AddressCountry,
                      Company_AddressState,
                      Company_AddressCity,
                      Company_AddressStreet,
                      Company_AddressNumber,
                      Company_AddressPostCode,
                      Company_VATID,
                      Company_BankAccName,
                      Company_BankAccNumber) 
                      VALUES(?,?,?,?,?,?,?,?,?,?)''',(
                          str(values_dict["Company_Name"]), 
                          str(values_dict["Company_AddressCountry"]), 
                          str(values_dict["Company_AddressState"]),
                          str(values_dict["Company_AddressCity"]),
                          str(values_dict["Company_AddressStreet"]),
                          str(values_dict["Company_AddressNumber"]),
                          str(values_dict["Company_AddressPostCode"]),
                          str(values_dict["Company_VATID"]), 
                          str(values_dict["Company_BankAccName"]),
                          str(values_dict["Company_BankAccNumber"])))
  
  companyrecorded={
  "Company_Name": str(values_dict["Company_Name"]), 
   "Company_AddressCountry":   str(values_dict["Company_AddressCountry"]), 
   "Company_AddressState"  :  str(values_dict["Company_AddressState"]),
   "Company_AddressCity"     :             str(values_dict["Company_AddressCity"]),
   "Company_AddressStreet"   :               str(values_dict["Company_AddressStreet"]),
   "Company_AddressNumber"   :               str(values_dict["Company_AddressNumber"]),
   "Company_AddressPostCode" :                 str(values_dict["Company_AddressPostCode"]),
   "Company_VATID"        :               str(values_dict["Company_VATID"]),                   
   "Company_BankAccName"   :               str(values_dict["Company_BankAccName"]),
   "Company_BankAccNumber"   :               str(values_dict["Company_BankAccNumber"])
  }


 

  print(json.dumps(companyrecorded, indent = 1))


  dbase.close()
  return companyrecorded












#----------REQUIREMENT NUMBER 2 = CUSTOMER CREATES ACCOUNT------------
#----------REQUIREMENT NUMBER 2 = CUSTOMER CREATES ACCOUNT------------
#----------REQUIREMENT NUMBER 2 = CUSTOMER CREATES ACCOUNT------------
#----------REQUIREMENT NUMBER 2 = CUSTOMER CREATES ACCOUNT------------
#----------REQUIREMENT NUMBER 2 = CUSTOMER CREATES ACCOUNT------------
#----------REQUIREMENT NUMBER 2 = CUSTOMER CREATES ACCOUNT------------
#----------REQUIREMENT NUMBER 2 = CUSTOMER CREATES ACCOUNT------------
#----------REQUIREMENT NUMBER 2 = CUSTOMER CREATES ACCOUNT------------
@app.post("/create_customer_account")
async def create_customer_account(payload: Request):
  values_dict = await payload.json()
  #open DB 
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)
  
  customers_with_this_email=dbase.execute('''
    SELECT Customer_ID FROM Customer
    WHERE Customer_Email=?
    ''',(str(values_dict['Customer_Email']),))
  query_email=(customers_with_this_email.fetchall())
  print(query_email)
  print("Customer email is "+ str(values_dict['Customer_Email']))
  if query_email:
    return "Customer email has been already registered"
  else:
    print("Registering the Customer...")
    print("Checking Credit Card number...")

  print(str(values_dict['Customer_CCNumber']))
  print(L.Luhn(str(values_dict['Customer_CCNumber'])))

  if L.Luhn(str(values_dict['Customer_CCNumber']))==False:
    print("Credit card number is not valid")
    return "Credit card number is not valid"

  dbase.execute('''
        INSERT INTO Customer(
        Customer_Email,
        Customer_Name,
        Customer_Surname,
        Customer_AddressCountry,
        Customer_AddressState,
        Customer_AddressCity,
        Customer_AddressStreet,
        Customer_AddressNumber,
        Customer_AddressPostCode, 
        Customer_CCNumber)
        VALUES(?,?,?,?,?,?,?,?,?,?)'''
        ,
        (
          str(values_dict['Customer_Email']),
          str(values_dict['Customer_Name']),
          str(values_dict['Customer_Surname']),
          str(values_dict['Customer_AddressCountry']),
          str(values_dict['Customer_AddressState']),
          str(values_dict['Customer_AddressCity']),
          str(values_dict['Customer_AddressStreet']),
          str(values_dict['Customer_AddressNumber']),
          str(values_dict['Customer_AddressPostCode']),
          str(values_dict['Customer_CCNumber'])))
  dbase.close()

  customerrecorder={
   'Customer_Email'           :           str(values_dict['Customer_Email']),            
   'Customer_Name'            :           str(values_dict['Customer_Name']),     
   'Customer_Surname'         :           str(values_dict['Customer_Surname']),   
   'Customer_AddressCountry'  :           str(values_dict['Customer_AddressCountry']),               
   'Customer_AddressState'    :           str(values_dict['Customer_AddressState']),           
   'Customer_AddressCity'     :           str(values_dict['Customer_AddressCity']),       
   'Customer_AddressStreet'   :           str(values_dict['Customer_AddressStreet']),        
   'Customer_AddressNumber'   :           str(values_dict['Customer_AddressNumber']),            
   'Customer_AddressPostCode' :           str(values_dict['Customer_AddressPostCode']),                
   'Customer_CCNumber'        :           str(values_dict['Customer_CCNumber'])     
  }

  print(json.dumps(customerrecorder, indent = 3))

  print("Customer is now registered")
  return  customerrecorder













#---------------REQUIREMENT NUMBER 3 = COMPANY Creates A QUOTE------------------
#---------------REQUIREMENT NUMBER 3 = COMPANY Creates A QUOTE------------------
#---------------REQUIREMENT NUMBER 3 = COMPANY Creates A QUOTE------------------
#---------------REQUIREMENT NUMBER 3 = COMPANY Creates A QUOTE------------------
#---------------REQUIREMENT NUMBER 3 = COMPANY Creates A QUOTE------------------
#---------------REQUIREMENT NUMBER 3 = COMPANY Creates A QUOTE------------------
#---------------REQUIREMENT NUMBER 3 = COMPANY Creates A QUOTE------------------
#---------------REQUIREMENT NUMBER 3 = COMPANY Creates A QUOTE------------------

@app.post("/create_quote")
async def review_quote(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)
  #To post a quote company enters its product details and id
  query_new_product='''
                INSERT INTO Product(
                  Product_Name,
                  Product_CurrencyCode,
                  Product_Price,
                  Company_ID

                )
                VALUES(
                  "{Product_Name}",
                  "{Product_CurrencyCode}",
                  {Product_Price},
                  {Company_ID}
                )                
                '''.format(
                  Product_Name=str(values_dict['Product_Name']),
                  Product_CurrencyCode=str(values_dict['Product_CurrencyCode']),
                  Product_Price=str(values_dict['Product_Price']),
                  Company_ID=str(values_dict['Company_ID'])
                )
  dbase.execute(query_new_product)





  #---Filter for product_id using name, currency, price and company 
  query_product='''
                SELECT Product_ID FROM Product
                WHERE Product_Name="{Product_Name}"
                AND Product_CurrencyCode="{Product_CurrencyCode}"
                AND Product_Price ={Product_Price}
                AND Company_ID={Company_ID}
                '''.format(
                      Product_Name=str(values_dict['Product_Name']),
                      Product_CurrencyCode=str(values_dict['Product_CurrencyCode']),
                      Product_Price =str(values_dict['Product_Price']),
                      Company_ID=str(values_dict['Company_ID']))
  
  print(query_product)
  test_query=dbase.execute(query_product).fetchall()
  print(test_query)
  #if test_query:
  #  return "Company doesn't have that product"
  #  
  #else:
  productid=dbase.execute(query_product).fetchall()[0][0]
  print("productid = " + str(productid))


#--- filter for cusomter_id using the email
  query_customerid='''
                SELECT Customer_ID FROM Customer
                WHERE Customer_Email="{Customer_Email}"
                '''.format(
                      Customer_Email=str(values_dict['Customer_Email']))
  
  print(query_customerid)
  print_query_customer_if_list=dbase.execute(query_customerid).fetchall()
  if len(print_query_customer_if_list)==0:
    print("This customer has no account in our database")
    return "This customer has no account in our database"
  print(print_query_customer_if_list)
  customerid=dbase.execute(query_customerid).fetchall()[0][0]
  print(customerid)

#--- record the quote
  query_quote='''
              INSERT INTO Quote(
                Quote_Quantity,
                Quote_Date,
                Product_ID,
                Customer_ID,
                Company_ID)
                VALUES(
                  {Quote_Quantity},
                  "{Quote_Date}",
                  {Product_ID},
                  {Customer_ID},
                  {Company_ID})'''.format(
                    Quote_Quantity=str(values_dict['Quote_Quantity']),
                    Quote_Date=str(values_dict['Quote_Date']),
                    Product_ID=str(productid),
                    Customer_ID=str(customerid),
                    Company_ID=str(values_dict['Company_ID'])
                  )
  print(query_quote)
  results_quote=(dbase.execute(query_quote).fetchall())
  print(results_quote)

  last_quote='''SELECT * FROM Quote ORDER BY Quote_ID DESC LIMIT 1'''
  last_quoate_print=dbase.execute(last_quote).fetchall()
  print(last_quoate_print)

  VAT=float(values_dict['Product_Price'])*0.21
  print(VAT)
  VAT_Excluded=float(values_dict['Product_Price'])
  VAT_Included=float(values_dict['Product_Price'])*1.21


  quote_print={
  "Product_Name"               : str(values_dict['Product_Name']),
  "Product_CurrencyCode"       : str(values_dict['Product_CurrencyCode']),
  "Product_Price"              : float(values_dict['Product_Price']),
  "Product_Price_VAT_Included" :float(values_dict['Product_Price'])*1.21,
  "Company_ID"                 : (values_dict['Company_ID']),
  "Quote_Quantity"             : (values_dict['Quote_Quantity']),
  "Quote_Date"                 : str(values_dict['Quote_Date']),
  "Customer_Email"             : str(values_dict['Customer_Email'])
  }

  print(json.dumps(quote_print, indent = 3))
  dbase.close()
  return quote_print
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------








#-----------REQUIREMENT NUMBER 4: CUSTOMER ACCEPTS THE QUOTE------------
#-----------REQUIREMENT NUMBER 4: CUSTOMER ACCEPTS THE QUOTE------------
#-----------REQUIREMENT NUMBER 4: CUSTOMER ACCEPTS THE QUOTE------------
#-----------REQUIREMENT NUMBER 4: CUSTOMER ACCEPTS THE QUOTE------------
#-----------REQUIREMENT NUMBER 4: CUSTOMER ACCEPTS THE QUOTE------------
#-----------REQUIREMENT NUMBER 4: CUSTOMER ACCEPTS THE QUOTE------------
#-----------REQUIREMENT NUMBER 4: CUSTOMER ACCEPTS THE QUOTE------------

@app.post("/accept_quote")
async def convert_quote_to_subscription(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)                                         
  get_companyid=''' 
      SELECT Quote.Company_ID, Quote.Product_ID FROM Quote 
      WHERE Quote_ID={Quote_ID}
      '''.format(
               Quote_ID=str(values_dict["Quote_ID"]))
  print(get_companyid)
  
  comapnyid=dbase.execute(get_companyid).fetchall()[0][0]
  productid=dbase.execute(get_companyid).fetchall()[0][1]
  




  insert_into='''
              INSERT INTO Subscription(Quote_ID,Customer_ID,Company_ID,Product_ID)
              VALUES({Quote_ID},{Customer_ID},{Company_ID},{Product_ID})
              '''.format(Customer_ID = str(values_dict["Customer_ID"]),
        Quote_ID=str(values_dict["Quote_ID"]),
        Company_ID=str(comapnyid),
        Product_ID=str(productid))
  dbase.execute(insert_into)







  get_sub=''' 
      SELECT Subscription.Subscription_ID FROM Subscription 
      WHERE Subscription.Customer_ID={Customer_ID}
      AND Subscription.Quote_ID={Quote_ID}
      '''.format(
        Customer_ID = str(values_dict["Customer_ID"]),
        Quote_ID=str(values_dict["Quote_ID"]))
  print(get_sub)
  
  sub=dbase.execute(get_sub).fetchall()
  print(sub)
  if len(sub)==0:
    print("This Customer has not recieved a quote to accept on this product")
    return "This Customer has not recieved a quote to accept on this product"
  elif sub[0][0]==None:
    print("This Customer has not recieved a quote to accept on this product")
    return "This Customer has not recieved a quote to accept on this product"

  sub=dbase.execute(get_sub).fetchall()[0][0]
  print(sub)

  get_companyid=''' 
      SELECT Product.Company_ID FROM Product 
      WHERE Product_ID={Product_ID}
      '''.format(
               Product_ID=str(productid))
  print(get_companyid)
  
  comapnyid=dbase.execute(get_companyid).fetchall()[0][0]





  update_sub='''
      INSERT INTO Subscription(
      Quote_ID,
      Customer_ID,
      Product_ID,
      Company_ID
      )
      VALUES(
      {Quote_ID},
      {Customer_ID},
      {Product_ID},
      {Company_ID}
      )
    '''.format(
        Quote_ID=str(values_dict["Quote_ID"]),
        Customer_ID=str(values_dict["Customer_ID"]),
        Product_ID=str(productid),
        Company_ID=str(comapnyid)
    )
  dbase.execute(update_sub)
  accept_sub='''
      UPDATE Subscription 
      SET Subscription_Active = 1 
      WHERE Subscription_ID = {Subscription_ID}
      AND Customer_ID = {Customer_ID}      
      '''.format( 
        Subscription_ID=str(sub),
        Customer_ID=str(values_dict["Customer_ID"])
        
      )
  print(accept_sub)
  dbase.execute(accept_sub)
  query_name='''SELECT Customer.Customer_Name, Customer.Customer_Surname
                FROM Customer
                WHERE Customer_ID="{Customer_ID}"
                '''.format(Customer_ID=str(values_dict['Customer_ID']))
  query_customer_name_surname=dbase.execute(query_name).fetchall()
  name=query_customer_name_surname[0][0]
  surname=query_customer_name_surname[0][1]

  print("Customer {} {} has accepted the quote".format(name,surname))

  customer_email_query='''SELECT Customer_Email FROM Customer 
                          WHERE Customer_ID={Customer_ID}'''.format(
                            Customer_ID=str(values_dict['Customer_ID']))
  customeremail=dbase.execute(customer_email_query).fetchall()[0][0]
  query_name='''SELECT Customer.Customer_Name, Customer.Customer_Surname
                FROM Customer
                WHERE Customer_ID="{Customer_ID}"
                '''.format(Customer_ID=str(values_dict['Customer_ID']))
  query_customer_name_surname=dbase.execute(query_name).fetchall()
  name=query_customer_name_surname[0][0]
  surname=query_customer_name_surname[0][1]

  query_prduct='''  
              SELECT Product_Name,Product_CurrencyCode,Product_Price 
              FROM Product
              WHERE Product_ID={Product_ID}
              '''.format(
              
                Product_ID=str(productid))
  product=dbase.execute(query_prduct).fetchall()
  productname=product[0][0]
  productcurrency=product[0][1]
  productprice=product[0][2]      



  query_quote='''
            SELECT Quote_Quantity, Quote_Date
            FROM Quote
            WHERE Quote_ID = {Quote_ID}
            '''.format(Quote_ID=str(values_dict["Quote_ID"]))
  quantity=dbase.execute(query_quote).fetchall()[0][0]
  quotedate=dbase.execute(query_quote).fetchall()[0][1]

  customeraccepted={
   'Customer_Email'           :   customeremail,            
   'Customer_Name'            :   name,     
   'Customer_Surname'         :   surname,     
   "Product_Name"            :   str(productname),
  "Product_CurrencyCode"       : str(productcurrency),
  "Product_Price"              : float(productprice),
  "Product_Price_VAT_Included" :float(productprice)*1.21,
  "Quote_Quantity"             : int(quantity),
  "Quote_Date"                 : str(quotedate)


  }
  print(json.dumps(customeraccepted, indent = 3))


  dbase.close()
  return customeraccepted

#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------






#----------------INVOICE CREATION-------------------
#----------------INVOICE CREATION-------------------
#----------------INVOICE CREATION-------------------
#----------------INVOICE CREATION-------------------
#----------------INVOICE CREATION-------------------
#----------------INVOICE CREATION-------------------
#----------------INVOICE CREATION-------------------
#----------------INVOICE CREATION-------------------
#----------------INVOICE CREATION-------------------
#----------------INVOICE CREATION-------------------

#-------------------------Customer requests to see Inovice 

@app.post("/create_invoice")
async def create_invoice(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)

      
  values=str(values_dict['Subscription_ID'])
  subscriptionid=values[0][0]



  get_companyid=''' 
      SELECT Subscription.Company_ID FROM Subscription 
      WHERE Subscription_ID={Subscription_ID}
      '''.format(
               Subscription_ID=str(subscriptionid))
  print(get_companyid)
  
  comapnyid=dbase.execute(get_companyid).fetchall()[0][0]



  query_insert_invoice='''
                    INSERT INTO Invoice(
                      Customer_ID,
                      Subscription_ID,
                      Company_ID
                    ) 
                    VALUES({Customer_ID},{Subscription_ID},{Company_ID})       
                    '''.format(
                      Customer_ID=str(values_dict['Customer_ID']),
                      Subscription_ID=str(subscriptionid),
                      Company_ID=str(comapnyid)
                    )
  print(query_insert_invoice)
  insert_invoice=dbase.execute(query_insert_invoice).fetchall()
  print(insert_invoice)

  query_product_id='''SELECT Product_ID
                FROM Subscription
                WHERE Subscription_ID="{Subscription_ID}"
                '''.format(Subscription_ID=str(subscriptionid))
  query_product_id_result=dbase.execute(query_product_id).fetchall()
  productid=query_product_id_result[0][0]


  query_name='''SELECT Customer.Customer_Name, Customer.Customer_Surname
                FROM Customer
                WHERE Customer_ID="{Customer_ID}"
                '''.format(Customer_ID=str(values_dict['Customer_ID']))
  query_customer_name_surname=dbase.execute(query_name).fetchall()
  name=query_customer_name_surname[0][0]
  surname=query_customer_name_surname[0][1]

  query_name='''SELECT Customer.Customer_Name, Customer.Customer_Surname
                FROM Customer
                WHERE Customer_ID="{Customer_ID}"
                '''.format(Customer_ID=str(values_dict['Customer_ID']))
  query_customer_name_surname=dbase.execute(query_name).fetchall()
  name=query_customer_name_surname[0][0]
  surname=query_customer_name_surname[0][1]



  customer_email_query='''SELECT Customer_Email FROM Customer 
                          WHERE Customer_ID={Customer_ID}'''.format(
                            Customer_ID=str(values_dict['Customer_ID']))
  customeremail=dbase.execute(customer_email_query).fetchall()[0][0]
  query_name='''SELECT Customer.Customer_Name, Customer.Customer_Surname
                FROM Customer
                WHERE Customer_ID="{Customer_ID}"
                '''.format(Customer_ID=str(values_dict['Customer_ID']))
  query_customer_name_surname=dbase.execute(query_name).fetchall()
  name=query_customer_name_surname[0][0]
  surname=query_customer_name_surname[0][1]

  query_prduct='''  
              SELECT Product_Name,Product_CurrencyCode,Product_Price 
              FROM Product
              WHERE Product_ID={Product_ID}
              '''.format(
              
                Product_ID=str(productid))
  product=dbase.execute(query_prduct).fetchall()
  productname=product[0][0]
  productcurrency=product[0][1]
  productprice=product[0][2]  


  get_quote=''' 
      SELECT Quote_ID FROM Quote 
      WHERE Customer_ID={Customer_ID}
      AND Product_ID={Product_ID}
      '''.format(
        Customer_ID = str(values_dict["Customer_ID"]),
        Product_ID=str(productid))
  print(get_quote)
  
  a=dbase.execute(get_quote).fetchall()
  print(a)
  if len(a)==0:
    print("This Customer has not recieved a quote to accept on this product")
    return "This Customer has not recieved a quote to accept on this product"
  elif a[0][0]==None:
    print("This Customer has not recieved a quote to accept on this product")
    return "This Customer has not recieved a quote to accept on this product"

  quoteid=dbase.execute(get_quote).fetchall()[0][0]
  print(quoteid)
  query_quote='''
            SELECT Quote_Quantity, Quote_Date
            FROM Quote
            WHERE Quote_ID = {Quote_ID}
            '''.format(Quote_ID=str(quoteid))
  quantity=dbase.execute(query_quote).fetchall()[0][0]

  thismonthslastday = pd.Period(pd.Timestamp.today().strftime('%Y-%m-%d'),freq='M').end_time.date() 
  print(thismonthslastday) 
  
  customer_email_query='''SELECT Customer_Email FROM Customer 
                          WHERE Customer_ID={Customer_ID}'''.format(
                            Customer_ID=str(values_dict['Customer_ID']))
  customeremail=dbase.execute(customer_email_query).fetchall()[0][0]
  print(customeremail)


  query_prduct='''  
              SELECT Product_Name,Product_CurrencyCode,Product_Price 
              FROM Product
              WHERE Product_ID={Product_ID}
              '''.format(
                Product_ID=str(productid))
  product=dbase.execute(query_prduct).fetchall()
  productname=product[0][0]



  inovicedetails={
   'Customer_Email'           :   str(customeremail),            
   'Customer_Name'            :   str(name),     
   'Customer_Surname'         :   str(surname),     
   "Product_Name"            :   str(productname),
  "Product_CurrencyCode"       : str(productcurrency),
  "Product_Price"              : float(productprice),
  "Product_Price_VAT_Included" :float(productprice)*1.21,
  "Total amount"              : float(productprice)*1.21*float(quantity),
  "Quote_Quantity"             : int(quantity),
  "Due_Date"                 : str(thismonthslastday)


  } 

 
  print(json.dumps(inovicedetails, indent = 3))


  dbase.close()     
  return inovicedetails 


#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------



















#------------------------SET INVOICE ACTIVE AND PRINT RESULTS---------------------
#------------------------SET INVOICE ACTIVE AND PRINT RESULTS---------------------
#------------------------SET INVOICE ACTIVE AND PRINT RESULTS---------------------
#------------------------SET INVOICE ACTIVE AND PRINT RESULTS---------------------
#------------------------SET INVOICE ACTIVE AND PRINT RESULTS---------------------
#------------------------SET INVOICE ACTIVE AND PRINT RESULTS---------------------
#------------------------SET INVOICE ACTIVE AND PRINT RESULTS---------------------
#------------------------SET INVOICE ACTIVE AND PRINT RESULTS---------------------
#------------------------SET INVOICE ACTIVE AND PRINT RESULTS---------------------

@app.post("/update_invoice")
async def update_invoice(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)


  query_invoice_update='''
                        SELECT Invoice.Invoice_ID, Invoice.Invoice_Paid 
                        FROM Invoice
                        WHERE Customer_ID={Customer_ID}
                        AND Subscription_ID={Subscription_ID}
                        '''.format(
                          Customer_ID=str(values_dict['Customer_ID']),
                          Subscription_ID=str(values_dict['Subscription_ID']))
  print(query_invoice_update)
  a=dbase.execute(query_invoice_update).fetchall()
  print(a)

  paidstatusornot=a[0][1]
  print(paidstatusornot)
  

  if not paidstatusornot:
    print("Customer doesn't have any pending Invoice")
    return "Customer doesn't have any pending Invoice"
  elif paidstatusornot==1:
    print('This invoice has already been paid')
  elif paidstatusornot==0:
    return True
  elif paidstatusornot is None:
    return True



  invoiceid=a[0][0]

  customer_email_query='''SELECT Customer_Email FROM Customer 
                          WHERE Customer_ID={Customer_ID}'''.format(
                            Customer_ID=str(values_dict['Customer_ID']))
  customeremail=dbase.execute(customer_email_query).fetchall()[0][0]
  print(customeremail)
  
  
  
  query_invoice_update='''
                        UPDATE Invoice
                        SET Invoice_Paid=1,
                        Invoice_PaidDate= "{Invoice_PaidDate}"
                        WHERE Invoice_ID={Invoice_ID}
                        '''.format(
                          Invoice_PaidDate=str(values_dict['Invoice_PaidDate']),
                          Invoice_ID=str(invoiceid))
  print(query_invoice_update)
  dbase.execute(query_invoice_update)

  query_name='''SELECT Customer.Customer_Name, Customer.Customer_Surname
                FROM Customer
                WHERE Customer_ID="{Customer_ID}"
                '''.format(Customer_ID=str(values_dict['Customer_ID']))
  query_customer_name_surname=dbase.execute(query_name).fetchall()
  name=query_customer_name_surname[0][0]
  surname=query_customer_name_surname[0][1]


  query_productid='''SELECT Subscription.Product_ID
                  FROM Invoice 
                  LEFT JOIN Subscription ON Subscription.Subscription_ID=Invoice.Subscription_ID
                  WHERE Subscription.Subscription_ID={Subscription_ID}
                  '''.format(Subscription_ID=str(values_dict['Subscription_ID']))
  productid=dbase.execute(query_productid).fetchall()[0][0]



  query_prduct='''  
              SELECT Product_Name,Product_CurrencyCode,Product_Price 
              FROM Product
              WHERE Product_ID={Product_ID}
              '''.format(
              
                Product_ID=str(productid))
  product=dbase.execute(query_prduct).fetchall()
  productname=product[0][0]

  get_quote=''' 
      SELECT Quote_ID FROM Quote 
      WHERE Customer_ID={Customer_ID}
      AND Product_ID={Product_ID}
      '''.format(
        Customer_ID = str(values_dict["Customer_ID"]),
        Product_ID=str(productid))
  print(get_quote)


  productcurrency=product[0][1]
  productprice=product[0][2]  
  quoteid=dbase.execute(get_quote).fetchall()[0][0]
  print(quoteid)
  query_quote='''
            SELECT Quote_Quantity, Quote_Date
            FROM Quote
            WHERE Quote_ID = {Quote_ID}
            '''.format(Quote_ID=str(quoteid))
  quantity=dbase.execute(query_quote).fetchall()[0][0]
  thismonthslastday = (pd.Timestamp.today()).date() 
  print(thismonthslastday) 

  query_invoice_status='''
                        SELECT Invoice_Paid
                        FROM Invoice
                        WHERE Invoice_PaidDate="{Invoice_PaidDate}"
                        AND Invoice_ID={Invoice_ID}
                        '''.format(
                          Invoice_PaidDate=str(values_dict['Invoice_PaidDate']),
                          Invoice_ID=str(invoiceid))
  print(query_invoice_status)
  dbase.execute(query_invoice_status)
  invoicestate=dbase.execute(query_invoice_status).fetchall()[0][0]
  print(invoicestate)

  if invoicestate is None:
    print("Invoice number {} has not been paid".format(invoiceid))
    invoicepaidyes=invoicestate
  elif not invoicestate:
    print(" This customer invoice does not exists") 
  elif invoicestate==1:
    invoicepaidyes="Paid"
    print("The invoice has been paid")




  paidinvoice={
   'Customer_Email'           :   customeremail,            
   'Customer_Name'            :   name,     
   'Customer_Surname'         :   surname,     
   "Product_Name"            :   str(productname),
    "Product_CurrencyCode"       : str(productcurrency),
    "Product_Price"              : float(productprice),
    "Product_Price_VAT_Included" :float(productprice)*1.21,
    "Total amount"              : float(productprice)*1.21*float(quantity),
    "Quote_Quantity"             : int(quantity),
    "Paid_Date"                 : str(thismonthslastday),
    "Paid status"         : str(invoicepaidyes)



  } 

 
  print(json.dumps(paidinvoice, indent = 3))




  dbase.close()
  return paidinvoice










#------------------------ANALYTICS---------------------
#------------------------ANALYTICS---------------------
#------------------------ANALYTICS---------------------
#------------------------ANALYTICS---------------------
#------------------------ANALYTICS---------------------
#------------------------ANALYTICS---------------------
#------------------------ANALYTICS---------------------








#---------------GET MRR ------------------------

@app.get("/ask_mrr")
async def update_invoice(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)

  query_product='''
                SELECT Company.Company_ID, Product.Product_ID, Product.Product_CurrencyCode, Product.Product_Price, Quote.Quote_Quantity   
                FROM Product
                LEFT JOIN Company ON Company.Company_ID=Product.Company_ID
                LEFT JOIN Subscription ON Subscription.Product_ID=Product.Product_ID
                LEFT JOIN Quote ON Quote.Product_ID=Product.Product_ID 
                WHERE Subscription.Subscription_Active=1
                AND Company.Company_ID={Company_ID}
                '''.format(
                      Company_ID=str(values_dict['Company_ID']))
  
  print(query_product)
  test_query=dbase.execute(query_product).fetchall()
  print(test_query)
  
  companyid=str(values_dict['Company_ID'])
  productid=[]
  productcurrency=[]
  productprice=[]
  quotequantity=[]



  for i in dbase.execute(query_product).fetchall():
    productid.append(i[1])

  for i in dbase.execute(query_product).fetchall():
    productcurrency.append(i[2])


  for i in dbase.execute(query_product).fetchall():
    productprice.append(i[3])

  
  for i in dbase.execute(query_product).fetchall():
    quotequantity.append(i[4])

  print(productid,productcurrency,productprice,quotequantity)

  currencies_and_sum = {str(row[2]): 0 for row in test_query}
  for row in test_query:
    currencies_and_sum[str(row[2])] += row[3] * row[4]


  totalsales=[]
  for cur in list(currencies_and_sum.items()):
    print(str(cur[0]),cur[1])
    totalsales.append(converter(str(cur[0]),cur[1]))
  print(totalsales) 
  print(sum(totalsales))
  sumvar=sum(totalsales)





  mrr={

    "MRR in EUR"       : (sumvar),
   } 

 
  print(json.dumps(mrr, indent = 3))



  
  dbase.close()
  return mrr
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------















#--------------------------ARR--------------------
#--------------------------ARR--------------------
#--------------------------ARR--------------------
#--------------------------ARR--------------------
#--------------------------ARR--------------------
#--------------------------ARR--------------------
#--------------------------ARR--------------------
#--------------------------ARR--------------------
#--------------------------ARR--------------------

@app.get("/ask_arr")
async def update_invoice(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)

  query_product='''
                SELECT Company.Company_ID, Product.Product_ID, Product.Product_CurrencyCode, Product.Product_Price, Quote.Quote_Quantity   
                FROM Product
                LEFT JOIN Company ON Company.Company_ID=Product.Company_ID
                LEFT JOIN Subscription ON Subscription.Product_ID=Product.Product_ID
                LEFT JOIN Quote ON Quote.Product_ID=Product.Product_ID 
                WHERE Subscription.Subscription_Active=1
                AND Company.Company_ID={Company_ID}
                '''.format(
                      Company_ID=str(values_dict['Company_ID']))
  
  print(query_product)
  test_query=dbase.execute(query_product).fetchall()
  print(test_query)
  
  companyid=str(values_dict['Company_ID'])
  productid=[]
  productcurrency=[]
  productprice=[]
  quotequantity=[]



  for i in dbase.execute(query_product).fetchall():
    productid.append(i[1])

  for i in dbase.execute(query_product).fetchall():
    productcurrency.append(i[2])


  for i in dbase.execute(query_product).fetchall():
    productprice.append(i[3])

  
  for i in dbase.execute(query_product).fetchall():
    quotequantity.append(i[4])

  print(productid,productcurrency,productprice,quotequantity)

  currencies_and_sum = {str(row[2]): 0 for row in test_query}
  for row in test_query:
    currencies_and_sum[str(row[2])] += row[3] * row[4]


  totalsales=[]
  for cur in list(currencies_and_sum.items()):
    print(str(cur[0]),cur[1])
    totalsales.append(converter(str(cur[0]),cur[1]))
  print(totalsales) 
  print(sum(totalsales))
  sumvar=sum(totalsales)*12





  arr={

    "ARR in EUR"       : (sumvar),
   } 

 
  print(json.dumps(arr, indent = 3))



  
  dbase.close()
  return arr



#-------------------------- 
#--------------------------
#--------------------------
#--------------------------
#--------------------------
#--------------------------
#--------------------------
#--------------------------
#--------------------------
#--------------------------



















#-------------------------- # of customers & average annual revenue per customer
#-------------------------- # of customers & average annual revenue per customer
#-------------------------- # of customers & average annual revenue per customer
#-------------------------- # of customers & average annual revenue per customer
#-------------------------- # of customers & average annual revenue per customer
#-------------------------- # of customers & average annual revenue per customer

@app.get("/number_of_customers")
async def update_invoice(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)

  query_product='''
                SELECT Company.Company_ID, Subscription.Subscription_ID  
                FROM Product
                LEFT JOIN Company ON Company.Company_ID=Product.Company_ID
                LEFT JOIN Subscription ON Subscription.Product_ID=Product.Product_ID
                LEFT JOIN Quote ON Quote.Product_ID=Product.Product_ID 
                WHERE Subscription.Subscription_Active=1
                AND Company.Company_ID={Company_ID}
                '''.format(
                      Company_ID=str(values_dict['Company_ID']))
  
  print(query_product)
  test_query=dbase.execute(query_product).fetchall()
  print(test_query)
  
  companyid=str(values_dict['Company_ID'])
  
  numberofsubs=[]
  for i in test_query:
    numberofsubs.append(i[1])
  
  print(numberofsubs)
  productid=[]
  productcurrency=[]
  productprice=[]
  quotequantity=[]

  sumcus=len(numberofsubs)


  averagerevenuepercustomer=sumcus
  revdetail={

    "Total active customers"       : (sumcus),

   } 

 
  print(json.dumps(revdetail, indent = 3))
 
  dbase.close()
  return revdetail







@app.get("/customers_all")
async def update_invoice(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)

  query_customer='''
                SELECT Customer.Customer_ID, Customer.Customer_Name, Customer.Customer_Surname, Subscription.Subscription_ID, Product.Product_Name, Company.Company_ID 
                FROM Customer
                LEFT JOIN Subscription ON Subscription.Customer_ID=Customer.Customer_ID
                LEFT JOIN Product ON Product.Product_ID=Subscription.Product_ID
                LEFT JOIN Company ON Company.Company_ID=Product.Company_ID
                WHERE Subscription.Subscription_Active={active}
                '''.format(active=str(values_dict['Subscription_Active']))
  
  print(query_customer)
  test_query=dbase.execute(query_customer).fetchall()
  print(test_query)
  results = pd.read_sql_query(query_customer, dbase)
  print(results)

 

 
  dbase.close()
  return True




































#-------------EXTRA STUFF 


@app.get("/see_customer_account")
async def see_customer_account(payload: Request):
  values_dict = await payload.json()
  #open DB 
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)   

  customer_records='''
    SELECT Customer.Customer_Name, Customer.Customer_Surname
    FROM Customer
    WHERE Customer_Email = "{a}"
    '''.format(a=str(values_dict['Customer_Email'])
    )
  print(customer_records)
  dbase.execute(customer_records)
  print(dbase.execute(customer_records).fetchall())
  print(customer_records)
  a = (dbase.execute(customer_records).fetchall())

  dbase.close()
  return a







if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=8000)
