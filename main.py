import sqlite3
from sqlite3.dbapi2 import connect
from fastapi import FastAPI, Request
import uvicorn
import LUHN as L


app = FastAPI()

# Router
@app.get("/")
def root():
  return {"message": "It works !"}














#------------------------------REQUIREMENT NUMBER 1 = COMPANY CREATE ACCOUNT -------------------------------------------- 

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




  dbase.close()
  return companyrecorded












#---------------------------------------------REQUIREMENT NUMBER 2 = CUSTOMER CREATES ACCOUNT----------------------------

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



  print("Customer is now registered")
  return  customerrecorder













#-------------------------------------------------REQUIREMENT NUMBER 3 = COMPANY Creates A QUOTE------------------

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
                Customer_ID)
                VALUES(
                  {Quote_Quantity},
                  "{Quote_Date}",
                  {Product_ID},
                  {Customer_ID})'''.format(
                    Quote_Quantity=str(values_dict['Quote_Quantity']),
                    Quote_Date=str(values_dict['Quote_Date']),
                    Product_ID=str(productid),
                    Customer_ID=str(customerid)
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
  "Product_Price"              : (values_dict['Product_Price']),
  "Product_Price_VAT_Included" :float(values_dict['Product_Price'])*1.21,
  "Company_ID"                 : (values_dict['Company_ID']),
  "Quote_Quantity"             : (values_dict['Quote_Quantity']),
  "Quote_Date"                 : str(values_dict['Quote_Date']),
  "Customer_Email"             : str(values_dict['Customer_Email'])
  }


  dbase.close()
  return quote_print














#-----------REQUIREMENT NUMBER 4: CUSTOMER ACCEPTS THE QUOTE------------------------

@app.post("/accept_quote")
async def convert_quote_to_subscription(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)                                         
  
  get_quote=''' 
      SELECT Quote_ID FROM Quote 
      WHERE Customer_ID={Customer_ID}
      AND Product_ID={Product_ID}
      '''.format(
        Customer_ID = str(values_dict["Customer_ID"]),
        Product_ID=str(values_dict["Product_ID"]))
  print(get_quote)
  
  a=dbase.execute(get_quote)
  if a==0:
    return "This Customer has not recieved a quote to accept"

  quoteid=dbase.execute(get_quote).fetchall()[0][0]
  print(quoteid)







  update_sub='''
      INSERT INTO Subscription(
      Quote_ID,
      Customer_ID,
      Product_ID
      )
      VALUES(
      {Quote_ID},
      {Customer_ID},
      {Product_ID}
      )
    '''.format(
        Quote_ID=str(quoteid),
        Customer_ID=str(values_dict["Customer_ID"]),
        Product_ID=str(values_dict["Product_ID"])
    )
  dbase.execute(update_sub)
  accept_quote='''
      UPDATE Subscription 
      SET Subscription_Active = 1 
      WHERE Quote_ID = {Quote_ID}
      AND Customer_ID = {Customer_ID}      
      '''.format( 
        Quote_ID=str(quoteid),
        Customer_ID=str(values_dict["Customer_ID"])
        
      )
  print(accept_quote)
  dbase.execute(accept_quote)
  query_name='''SELECT Customer.Customer_Name, Customer.Customer_Surname
                FROM Customer
                WHERE Customer_ID="{Customer_ID}"
                '''.format(Customer_ID=str(values_dict['Customer_ID']))
  query_customer_name_surname=dbase.execute(query_name).fetchall()
  name=query_customer_name_surname[0][0]
  surname=query_customer_name_surname[0][1]


  dbase.close()
  return "Customer {} {} has accepted the quote".format(name,surname)




















#-------------------------Customer requests to see Inovice 

@app.post("/create_invoice")
async def create_invoice(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)
  query_active_subs ='''
                    SELECT Subscription.Subscription_ID 
                    FROM Subscription
                    WHERE Subscription_Active = 1 
                    AND Subscription.Customer_ID = {Customer_ID}
                    '''.format(Customer_ID=values_dict['Customer_ID'])
  print(query_active_subs)
  a=dbase.execute(query_active_subs).fetchall()
  print(a)

  if len(a)==0:
    print("This customer does not have a subscription")
    return 'This customer does not have a subscription'
    
  
  subscriptionid=a[0][0]

  query_insert_invoice='''
                    INSERT INTO Invoice(
                      Customer_ID,
                      Subscription_ID
                    ) 
                    VALUES({Customer_ID},{Subscription_ID})       
                    '''.format(
                      Customer_ID=str(values_dict['Customer_ID']),
                      Subscription_ID=str(subscriptionid)
                    )
  print(query_insert_invoice)
  insert_invoice=dbase.execute(query_insert_invoice).fetchall()
  print(insert_invoice)

  query_name='''SELECT Customer.Customer_Name, Customer.Customer_Surname
                FROM Customer
                WHERE Customer_ID="{Customer_ID}"
                '''.format(Customer_ID=str(values_dict['Customer_ID']))
  query_customer_name_surname=dbase.execute(query_name).fetchall()
  name=query_customer_name_surname[0][0]
  surname=query_customer_name_surname[0][1]

  dbase.close()     
  return "New invoice created for customer  {} {}".format(name,surname)































#----------------Customer pay inovoice 

@app.post("/update_invoice")
async def update_invoice(payload: Request):
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)


  query_invoice_update='''
                        SELECT Invoice.Invoice_ID 
                        FROM Invoice
                        WHERE Customer_ID={Customer_ID}
                        AND Subscription_ID={Subscription_ID}
                        AND Invoice_Paid=0
                        OR Invoice_Paid="NULL"
                        '''.format(
                          Customer_ID=str(values_dict['Customer_ID']),
                          Subscription_ID=str(values_dict['Subscription_ID']))
  print(query_invoice_update)
  a=dbase.execute(query_invoice_update).fetchall()
  print(a)
  if a==None:
    print("Customer doesn't have any pending Invoice")
    return "Customer doesn't have any pending Invoice"
  elif a[0][0]:
    print("Customer doesn't have any pending Invoice")
    return "Customer doesn't have any pending Invoice"


  invoiceid=a[0][0]
  print(invoiceid)
  
  
  
  
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
