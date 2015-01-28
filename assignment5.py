#!/usr/bin/env python

print "You walk into the kitchen and there is a new bowl of apples and oranges on the table! Do you pick up an apple or an orange? (type '1' for apple, type '2' or orange)"

selection = raw_input(">")

if selection == "1":
    print "You chose the apple! Do you wash it first?"
    print "1. You wash it."
    print "2. You bite right in."
    
    wash = raw_input(">")
    
    if wash == "1":
        print "Mmmmmmmm. That was a tasy apple!"
    elif wash == "2":
        print "You bite in...and there is a big fat worm! Gross."
    else:
        print "Please choose either '1' or '2'."

elif selection == "2":
    print "You chose the orange! How do you prepare it?"
    print "1. You cut it first."
    print "2. You peel it first."
    
    prep = raw_input(">")
    
    if prep == "1":
        print "Uh oh. You cut off your finger! Quick, pack it in a cooler and call 911!"
    elif prep == "2":
        print "Mmmm that was  tasty orange...but you got juice all over your shirt! FAIL."
    else:
        "Please choose either '1' or '2'"
    

