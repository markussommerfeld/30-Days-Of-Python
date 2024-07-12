# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:40:16 2024

@author: marku
"""

"""   
    Get the current day, month, year, hour, minute and timestamp from datetime module
    Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
    Today is 5 December, 2019. Change this time string to time.
    Calculate the time difference between now and new year.
    Calculate the time difference between 1 January 1970 and now.
    Think, what can you use the datetime module for? Examples:
        Time series analysis
        To get a timestamp of any activities in an application
        Adding posts on a blog
"""

#1 done
import datetime 

now = datetime.datetime.now()
print(now)

#2 done
t = now.strftime('%m/%d/%Y, %H:%M:%S')
print(t)

#3 done
str_date = '5 December, 2019'
date_object = datetime.datetime.strptime(str_date, "%d %B, %Y")

#4 done
t_newyear = datetime.datetime(year =2025, month = 1, day = 1, hour = 0, minute = 0, second = 0)
till_newyear = t_newyear - now
print(till_newyear)

#5 done
timestamp = now.timestamp()
print(datetime.timedelta(days=0, hours=0, minutes=0, seconds=timestamp) )

#6 done. is just thinking