#!/usr/bin/env python

import time

#variables
my_name = 'Ellen'
school = 'UNC'
year = 'Senior'
class_hours = 15
grad_month = 05
grad_day = 10

todays_day = float(time.strftime("%d"))
todays_month = float(time.strftime("%m"))

countdown = (grad_month - todays_month)*30  + (grad_day - todays_day)

print 'Hello, my name is.', my_name
print 'I am a %s at %s.' % (year, school)
print 'I am in %d hours this semester, which means I am in %d classes.' % (class_hours, class_hours/3)
print 'I graduate on %d/%d...which is in about %d days!' % (grad_month, grad_day, countdown)