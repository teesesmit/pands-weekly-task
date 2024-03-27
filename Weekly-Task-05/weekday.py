#Write a program that outputs whether or not today is a weekday.
#https://docs.python.org/3/library/datetime.html
#figure out what current day it is using currenttime/weekday
#import datetime - days of the week 0-6 (Monday is 0, Sunday is 6)
#use if to see what day it is (0-5 weekday)and else if weekend and print comment
# Author Theresa Smyth

import datetime
#https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python
#What is the current date today
current_date = datetime.datetime.today()

#Day of the week lables from weekday
day_of_week = current_date.weekday() 

#Is today a Monday(0) - Friday(<5)
#https://pynative.com/python-get-the-day-of-week/#h-check-if-a-date-is-a-weekday-or-weekend
if day_of_week < 5:
    print("Yes, unfortunately today is a weekday.")
else: 
    print("No, today is a weekend. Enjoy!")