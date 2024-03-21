#Write a program that takes a positive floating-point number as input  
#outputs an approximation of its square root.
#You should create a function called <tt>sqrt</tt> that does this.
#create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html 
 

def sqrt(number):
    #The loop continues as long as the absolute difference between 
    #the square of the guess and the original number is greater than 0.0001. 
    guess = number / 2
    while abs(guess * guess - number) > 0.0001:
        guess = (guess + number / guess) / 2
    
    return guess

def main():
    # Take input from the user
    user_query = input("Enter a positive number: ")
    
    # Converts the user input string to a floating-point number and assigns it to the variable
    number = float(user_query)

     #Checks if it's positive   
    if number > 0:
            # Approximate the square root using the custom sqrt function from input num
            approx_root = sqrt(number)
            print(f"Approximate square root of {number} is: {approx_root:.1f}")
    else:
            print("Error: Please enter a positive number.")

if __name__ == "__main__":
    main()