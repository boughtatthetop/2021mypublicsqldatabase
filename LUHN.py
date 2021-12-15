def Luhn(Customer_CCNumber):
    last=Customer_CCNumber[-1]

    Customer_CCNumber1=Customer_CCNumber[0:-1]

    #1. extract last digit (checking digit) of CC
    Customer_CCNumber2=Customer_CCNumber1[::-1]

    #2. reverses the Customer_CCNumber order 
    Customer_CCNumber3=[]
    #empty vecotr for further applications
    for i in range(0,len(Customer_CCNumber2),2):
      if int(Customer_CCNumber2[i])*2>9:
        #if double of digit is > 9
        Customer_CCNumber3.append((int(Customer_CCNumber2[i])*2-9))
        #subtract 9
      else:
        Customer_CCNumber3.append((int(Customer_CCNumber2[i])*2))
        #if it is not, leave it double
      try:
        Customer_CCNumber3.append(int(Customer_CCNumber2[i+1]))
        #to test the number digit
      except Exception:
        pass
    if (sum(Customer_CCNumber3)+int(last))%10==0:
      #checks if number can be divided by 10
      output=True
      print("The Customer_CCNumber is valid")
    else:
      output=False
      print("The Customer_CCNumber is not valid")
    return(output)
