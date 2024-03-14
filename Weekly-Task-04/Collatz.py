#Input any positive integer 
#and outputs the successive values of the following calculation:
#At each step calculate the next value by taking the current value 
#and, if it is even, divide it by two, 
#but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.

#Author Theresa Smyth

#enter number
number = int(input("enter an integer:"))

# if the number is divisible by 2 it's even, then divide by 2
if (number % 2) == 0:
    print(f"{number} is an even number your answer is:", (number / 2))
    #if number not divisible by 2 it's odd, then multipy by 3 and add 1
else:
    print(f"{number} is an odd number your answer is:", ((number * 3) +1))
    #if answer is one it ends
    while number != 1:
        break
