#Weekly Task 03 - Extra
#any lenght account number 
#outputs account number with first 6 digits as X's and only last 4 digits showing
#Author Theresa Smyth

#enter account number 
accountno = input ("Please enter your account number: ") 

# allows any lenght account no. and replace the first 6 numers with X
hidden_number = 'X' * 6 + accountno[6:]

print('Account Number:', hidden_number)