#Company payload example
{ 
  "Name": "Meta",
  "AddressCountry":"USA",
  "AddressState": "LA",
  "AddressCity": "sillicon valley",
  "AddressStreet": "Beautiful Street",
  "AddressNumber": "546",
  "AddressPostCode": "10200",
  "VATID": "2131231434123",
  "BankAcc": "1225345345345"
}

#Customer payload example
{ 
  "CompanyID": "1",
  "Name": "Bond",
  "Surname":"James",
  "Email":"james.bond@gmail.com",
  "AddressCountry":"USA",
  "AddressState": "Statexyz",
  "AddressCity": "CItyxyz",
  "AddressStreet": "BStreetxyz",
  "AddressNumber": "101",
  "AddressPostCode": "1020",
  "CCNumber": "2233 4455 6677 8899",
}

#Quote payload example
{ 
  "CustomerAccountID": "1",
  "ProductID":"1",
  "Quantity": "2",
  "StartDate": "01-01-2022",
  "EndDate": "01-01-2023"
}

#Review quote payload example
{ 
  "QuoteID":"1",
  "Accepted":"1"
}

#Convert quote payload example
#We assume that the company will convert lonly quotes that are accepted
{ 
  "CustomerAccountID": "1",
  "QuoteID":"1"
}

#Create invoice payload example
{ 
  "CustomerAccountID": "1",
  "InvoiceDate": "31-12-2021"
}








