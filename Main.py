#Main file where the code must be executed
#Model View ViewModel Arquitecture
#Clean Arquitecture Principles

import time
from datetime import date
from datetime import datetime
from Books.Ui.BooksMenu import booksMenu
import Ui.MainMenu as mainMenu
import GeneralMethods as general
import Books.BooksLogic as booksLogic

def start():
    opc=""
    msg=""

    while(opc != "0"):
        if(msg != ""):
            general.clear()
            general.message(msg)
            time.sleep(2)
            general.clear()
        else:
            general.clear()
        
        general.today()
        mainMenu.mainMenu()  #Displaying Main Menu
        opc = input("\nPlease Pick a Number: ")

        if(opc == "2"):
            general.clear()
            booksLogic.opcBooks("")
            msg=""
        
        elif(opc == "0"):
            general.clear()
            mainMenu.byeNotification()
            time.sleep(2)
        else:
            msg="Wrong pick.\n\nCleaning Screen...\n"

#Executing main function
start()