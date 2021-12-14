from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# Router
@app.get("/")
def root():
  return {"message": "It works !"}

@app.post("/create_company_account")
async def create_company_account():
  values_dict = await paylaod.json()
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)
  
  return True

@app.post("/create_customer_account")
async def create_customer_account():
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)
  #retrieve company ID
  return True 

@app.post("/create_quote")
async def create_quote():
  values_dict = await payload.json()
  #open DB
  dbase = sqlite3.connect('database_group43.db', isolation_level=None)
  #retrieve company ID
  return True

@app.post("/convert_quote")
async def convert_quote():
  # We will put here the code to execute
  return True

@app.post("/review_quote")
async def review_quote():
  # We will put here the code to execute
  return True

@app.post("/check_invoices")
async def check_invoices():
  # We will put here the code to execute
  return True

@app.post("/customer_payment")
async def customer_paymnent():
  # We will put here the code to execute
  return True

@app.post("/review_billing_info")
async def review_billing_info():
  # We will put here the code to execute
  return True

@app.post("/retrieve_statistics")
async def retrieve_statistics():
  # We will put here the code to execute
  return True

if __name__ == '__main__':
  uvicorn.run(app, host='127.0.0.1', port=8000)
