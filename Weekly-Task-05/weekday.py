#Write a program that outputs whether or not today is a weekday.
#https://docs.python.org/3/library/datetime.html
#figure out what current day it is using currenttime/weekday
#import datetime - days of the week 0-6 (Monday is 0, Sunday is 6)
#use if to see what day it is (0-5 weekday)and else if weekend and print comment
# Author Theresa Smyth

import datetime

#What is the current date today
current_date = datetime.datetime.now()

#Day of the week labes from weekday
day_of_week = current_date.weekday() 

#Is today a Monday(0) - Friday(<5)
if day_of_week < 5:
    print("Yes, unfortunately today is a weekday.")
else: 
    print("No, today is a weekend. Enjoy!")