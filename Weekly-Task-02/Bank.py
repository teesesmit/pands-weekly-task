#Weekly Task 02
#Read in two amounts
#add them together
#print out as currency
#Author Theresa Smyth

#User input
#https://docs.python.org/3/library/functions.html#float
x = float(input('Enter amount 1: ')) #amount 1
y = float(input('Enter amount 2: ')) #amount 2
final_amount = (x+y) #add together

#Seperate the euro and cent
#integer for the final amount for the euro part
euro = int(final_amount)
#calculates the remainder after division by 1 for the fractional,
#and multiply by 100 to convert to cents
#https://realpython.com/python-modulo-operator/
cent = int((final_amount % 1) * 100)

#final amounts printed in euro/cent to 2 deimal places
print(f"the final amount of money is €{euro}.{cent:02}")


