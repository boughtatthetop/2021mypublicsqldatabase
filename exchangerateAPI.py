import requests
#
#APIKEY     c41e6b0266369b7430b1b007


url = 'https://v6.exchangerate-api.com/v6/c41e6b0266369b7430b1b007/pair/EUR/{}/{}'

def converter(currency,amountUSD):
    amountconverter= requests.get(url.format(currency,amountUSD)).json()
    amountEUR=amountconverter["conversion_result"]
    return amountEUR

#EURamount=converter("USD",'1')
#print('EUR '+ str(EURamount))

#print(requests.get('https://v6.exchangerate-api.com/v6/c41e6b0266369b7430b1b007/pair/EUR/USD/123132.3123123').json()['conversion_result'])
























#import sqlite3
#from fastapi import FastAPI, Request
#import uvicorn
#app = FastAPI() 
#
#@app.post("/create_company_account")
#async def create_company_account(payload: Request):
#  values_dict = await payload.json()
#  #open DB 
#  dbase = sqlite3.connect('database_group43.db', isolation_level=None)
#  dbase.execute('''
#        INSERT INTO Company(
#        Company_Name,
#        Company_AddressCountry,
#        Company_AddressState,
#        Company_AddressCity,
#        Company_AddressStreet,
#        Company_AddressNumber,
#        Company_AddressPostCode,
#        Company_Company_VATID, 
#        Company_BankAccName,
#        Company_BankAccNumber)
#        VALUES(
#            {Company_Name},
#            {Company_AddressCountry},
#            {Company_AddressState},
#            {Company_AddressCity},
#            {Company_AddressStreet},
#            {Company_AddressNumber},
#            {Company_AddressPostCode},
#            {Company_Company_VATID},
#            {Company_BankAccName},
#            {Company_BankAccNumber})     
#        '''.format(
#                    Company_Name=                 str(values_dict['Company_Name']),
#                    Company_AddressCountry=       str(values_dict['Company_AddressCountry']),
#                    Company_AddressState=         str(values_dict['Company_AddressState']),
#                    Company_AddressCity=          str(values_dict['Company_AddressCity']),
#                    Company_AddressStreet=        str(values_dict['Company_AddressStreet']),
#                    Company_AddressNumber=        str(values_dict['Company_AddressNumber']),
#                    Company_AddressPostCode=      str(values_dict['Company_AddressPostCode']),
#                    Company_Company_VATID=        str(values_dict['Company_Company_VATID']), 
#                    Company_BankAccName=          str(values_dict['Company_BankAccName']),
#                    Company_BankAccNumber=        str(values_dict['Company_BankAccNumber'])))
#  #close DB 
#  dbase.close()
#  return True
#
#
#
#

#if __name__ == '__main__':
#  uvicorn.run(app, host='127.0.0.1', port=8000)
