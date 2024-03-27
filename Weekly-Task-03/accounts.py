#Weekly Task 03
#Accounts
#reads in 10 character account number 
#outputs account number with first 6 digits as X's and only last 4 digits showing
#Author Theresa Smyth

#enter account number 
accountno = input ("Please enter your 10 digit account number: ") 

# only allows 10 numbers 
#https://stackoverflow.com/questions/29656173/how-can-i-limit-the-amount-of-digits-in-an-input¸
if len(accountno) != 10:
    print("Error: Account number has to be 10 numbers")

else:
    #replace the first 6 numers with X
    #https://www.educative.io/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python#
    masked_char = 'X' * 6 + accountno[6:]
    
    print('Account Number:', masked_char)

