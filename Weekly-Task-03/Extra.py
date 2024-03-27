#Weekly Task 03 - Extra
#any lenght account number and replace the first 6 numers with X
#Author Theresa Smyth

#enter account number 
accountno = input ("Please enter your account number: ") 

# allows any lenght account no. and replace the first 6 numers with X
#remove len
#https://www.educative.io/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python#
masked_char = 'X' * 6 + accountno[6:]

print('Account Number:', masked_char)