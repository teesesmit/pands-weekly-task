#Weekly Task 03
#Accounts
#reads in 10 character account number 
#outputs account number with first 6 as X's and only last 4 digits showing
#Author Theresa Smyth

accountno = input("Please enter your 10 digit account number: ")) #enter account number 
if len(accountno) != 10:

print (accountno[6:])

