#Weekly Task 03
#Accounts
#reads in 10 character account number 
#outputs account number with first 6 digits as X's and only last 4 digits showing
#Author Theresa Smyth

#enter account number 
accountno = input ("Please enter your 10 digit account number: ") 

# only allows 10 numbers
if len(accountno) != 10:
    print("Error: Account number has to be 10 numbers")

else:
    #replace the first 6 numers with X
    hidden_number = 'X' * 6 + accountno[6:]
    
    print('Account Number:', hidden_number)

