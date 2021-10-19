#General functions that will be used for all the entities
#Persons and Books

import os
import sys
import time
from datetime import date
from datetime import datetime

#Funtion for clearing the screen
def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#This function returns as a string the weekday
def days(i):
    switcher={
        0:'Monday',
        1:'Tuesday',
        2:'Wednesday',
        3:'Thursday',
        4:'Friday',
        5:'Saturday',
        6:'Sunday'
    }
    return switcher.get(i,"No Valid Day")

#This function cast the month to a string
def months(i):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(i,"No Valid Mont")

#This function evaluates the last number of the day, so we can add the correct acronym
def acronym(txt):
    number = 0
    msg = ""
    
    for x in txt:
        number = number+1

    if number == 1:
        if(txt == "1"):
            msg = "st"
        elif(txt == "2"):
            msg ="nd"
        elif(txt == "3"):
            msg ="rd"
        else:
            msg ="th"

    if number == 2:
        if x[0:2] == "1":
            if(txt == "11"):
                msg= "th"
            else:
                msg ="st"
            
        elif(x[0:2] == "2"):
            if(txt == "12"):
                msg= "th"
            else:
                msg= "nd"
            
        elif(x[0:2] == "3"):
            if(txt == "13"):
                msg ="th"
            else:
                msg ="rd"
        else:
            msg= "th"

        return msg
      

#Today Function
def today():
    today = datetime.today()
    day = today.day #Day of the month
    text = acronym(str(day))
    weekDay = (days(today.weekday())) 
    month =  (months(today.month))
    Year = today.year
    return print (f"\nToday is {weekDay}, {month} {day}{text}, {Year}\n") 



#This function receives a string and returns a notification
def message(msg):
    print(msg)

