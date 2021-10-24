#This file controls all the workflow for Books
#Here we manage the events and secuency according to the user actions
#Model View ViewModel Arquitecture
#Clean Arquitecture Principles

import time
from datetime import date

import Books.Ui.BooksMenu as booksMenu
import GeneralMethods as general
import Books.Model.ClsBooks as clsBook


def opcBooks(opc):
    msg=""
    while opc != "0":
        if(msg!= ""):
            general.clear()
            general.message(msg)
            time.sleep(2)
            general.clear()
        else:
            general.clear()

        general.today()
        booksMenu.booksMenu() #Books Main Menu
        opc = input("\nPlease Pick a Letter: ")

        if (opc.lower() == "a"):
            general.clear()
            clsBook.Books().addBook()
            general.clear()

        elif(opc.lower() == "b"):
            general.clear()
            clsBook.Books().modifyBook()
            general.clear()

        elif(opc.lower() == "c"):
            general.clear()
            clsBook.Books().viewBook()
            general.clear()
        
        elif(opc.lower() == "d"):
            general.clear()
            clsBook.Books().deleteBook()
            general.clear()

        elif(opc.lower() == "e"):
            general.clear()
            clsBook.Books().listBook()
            space = ""
            input("Please Press Enter To Continue...")
            general.clear()

        elif(opc.lower() == "f"):
            general.clear()
            clsBook.Books().findBook()
            general.clear()

        elif(opc == "0"):
            general.clear()
            general.message("\nL o a d i n g   S c r e e n")
            time.sleep(2)
            general.clear()
            break
        else:
            general.clear()
            general.message("\nWrong pick.\nPlease Try Again\n\nCleaning Screen...\n")
            time.sleep(2)
            general.clear()
            continue