#This file controls all the workflow for Persons
#Here we manage the events and secuency according to the user actions
#Model View ViewModel Arquitecture
#Clean Arquitecture Principles

import time
from datetime import date
import Persons.Ui.PersonsMenu as personsMenu
import GeneralMethods as general
import Persons.Model.ClsPerson as clsPerson

#At this function we manage the logic for the PersonsMenu
def opcPersons(opc):
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
        personsMenu.personsMenu() #Persons Main Menu
        opc = input("\nPlease Pick a Letter: ")

        if (opc.lower() == "a"):
            general.clear()
            clsPerson.Persons().addPerson()
            general.clear()

        elif(opc.lower() == "b"):
            general.clear()
            clsPerson.Persons().modifyPerson()
            general.clear()

        elif(opc.lower() == "c"):
            general.clear()
            clsPerson.Persons().viewPerson()
            general.clear()
        
        elif(opc.lower() == "d"):
            general.clear()
            clsPerson.Persons().deletePerson()
            general.clear()

        elif(opc.lower() == "e"):
            general.clear()
            clsPerson.Persons().listPersons()
            space = ""
            input("Please Press Enter To Continue...")
            general.clear()
            

        elif(opc.lower() == "f"):
            general.clear()
            clsPerson.Persons().findPerson()
            general.clear()

        elif(opc == "0"):
            general.clear()
            general.message("\nL o a d i n g   S c r e e n")
            time.sleep(2)
            break
        else:
            general.clear()
            general.message("\nWrong pick.\nPlease Try Again\n\nCleaning Screen...\n")
            time.sleep(2)
            general.clear()
            continue