#to test:  
CCNumber='5038903899695949949'
print("CCNumber is: "+CCNumber)
def Luhn(CCNumber):
    last=CCNumber[-1]
    print("Last digit is: "+last)
    CCNumber1=CCNumber[0:-1]
    print("CCNumber without last digit is: "+CCNumber1)
    #1. extract last digit (checking digit) of CC
    CCNumber2=CCNumber1[::-1]
    print("CCNumber reverse order: "+ CCNumber2)
    #2. reverses the CCNumber order 
    CCNumber3=[]
    #empty vecotr for further applications
    for i in range(0,len(CCNumber2),2):
      if int(CCNumber2[i])*2>9:
        #if double of digit is > 9
        CCNumber3.append((int(CCNumber2[i])*2-9))
        print("CCNumber is larger than  9:  "+ str(CCNumber3))
        #subtract 9
      else:
        CCNumber3.append((int(CCNumber2[i])*2))
        #if it is not, leave it double
        print("CCNumber is smaller than  9: "+ str(CCNumber3)) 
      try:
        CCNumber3.append(int(CCNumber2[i+1]))
        #to test the number digit
        print("Testing next digit:  " + str(CCNumber3))
      except Exception:
        pass
    if (sum(CCNumber3)+int(last))%10==0:
      #checks if number can be divided by 10
      print("It is divisible with 10: "+str(sum(CCNumber3)))
      output=True
      print("YES it is")
    else:
      output=False
      print("The CCNumber is not valid")
    return(output)


Luhn(CCNumber)


#def Luhn(CCNumber):
#    last=CCNumber[-1]
#    CCNumber1=CCNumber[0:-1]
#    #1. extract last digit (checking digit) of CC
#    CCNumber2=CCNumber1[::-1]
#    #2. reverses the CCNumber order 
#    CCNumber3=[]
#    #empty vecotr for further applications
#    for i in range(0,len(CCNumber2),2):
#      if int(CCNumber2[i])*2>9:
#        #if double of digit is > 9
#        CCNumber3.append((int(CCNumber2[i])*2-9))
#        #subtract 9
#      else:
#        CCNumber3.append((int(CCNumber2[i])*2))
#        #if it is not, leave it double
#      try:
#        CCNumber3.append(int(CCNumber2[i+1]))
#        #to test the number digit
#      except Exception:
#        pass
#    if (sum(CCNumber3)+int(last))%10==0:
#      #checks if number can be divided by 10
#      output=True
#    else:
#      output=False
#    return(output)