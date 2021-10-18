#General functions that will be used for all the entities
#Persons and Books

import os
from datetime import date
from datetime import datetime

#Funtion for clearing the screen
def clear():
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")

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

#Today Function
def today():
    today = datetime.today()
    day = today.day #Day of the month
    weekDay = (days(today.weekday())) 
    month =  (months(today.month))
    Year = today.year
    print (f"\nHoy es {weekDay} {day} del {month} de {Year}\n") 


#This function receives a string and returns a notification
def message(msg):
    print(msg)

