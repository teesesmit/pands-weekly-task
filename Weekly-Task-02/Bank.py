#Weekly Task 02
#Read in two amounts
#add them together
#print out as currency
#Author Theresa Smyth

x = float(input('Enter amount 1: ')) #amount 1
y = float(input('Enter amount 2: ')) #amount 2
answer = (x+y) #add together

final = "€{:,}".format(answer) #format value to euro/cent
print(final)

