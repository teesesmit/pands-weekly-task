#Write a program that takes a positive floating-point number as input  
#outputs an approximation of its square root.
#You should create a function called <tt>sqrt</tt> that does this.
#create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x). 
 
#Input a positive integer
number = float(input("Please enter a positive number: "))
while number < 1:
    print ("This is a positive number")
    number = float(input ("This is not a positive number please try again: "))

    #Newtons method to return a square root of a number
    #initial guess for square root
    #count numbers of iterations
    #https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
def sqrt(number):
    x = number
    count = 0

    while True:
        count += 1

        root = 0.5 * (x + (number / x))

        if abs(root - x) < 1:
                break
            #update root
        x = root

        return root
    #round to 1 decimal place
n = round(sqrt(number),1)

print(f"The square root of {number} is approx {n}")
        
