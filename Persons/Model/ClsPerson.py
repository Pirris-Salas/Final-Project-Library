#ClsPerson is used for modeling all input data from the user
#Also all CRUD functions are stated here

import time
import Persons.Repository.PersonsRepository as personsDatabase
import GeneralMethods as general
import Persons.Ui.PersonsMenu as menu
import Ui.MainMenu as generalNotifications

class Persons:

    def _init_(self):
        pass

#This function is for adding an autoincremental ID for the Persons Database
    def newID(self, persons):
        id = 0
        for x in persons:
            if(x > id):
                id = x
        return id+1


#Funtion for validating blank fields
    def validationFields(name, email):
        msg =""

        if(name == "" or name == " "):
           msg= "\nPerson's name is missing!. Please try again, new book not saved"
        if(email == "" or email == " "):
            msg= f"{msg}\nEmail is missing!. Please try again, new book not saved"
        
        return msg


#Function for adding a new person to the database
    def addPerson(self):
        general.clear()
        opc = ""
        
        while opc != "0":
            general.clear()
            
            general.clear()
            general.today()
            menu.internalOptionMenu("N E W    P E R S O N", "Add a New Person    ")

            opc = input("\nPlease Pick a Number: ")

            if(opc == "1"):
                general.clear()
                id = int(Persons().newID(personsDatabase.persons))
                menu.newPerson()
                personName = input("Name: .......: ")
                email = input("Email: .......: ")
                    
        
                validationMsg = Persons.validationFields(personName, email)

                if(validationMsg != ""):
                    print(validationMsg)
                    time.sleep(1)
                    input("\nPlease Press Enter To Continue ...")
                    general.clear()
                    continue
            
                else:
                    savingConfirmation = input("Are you sure all data are correct? (Y/N): ")
                       
                    if(savingConfirmation.upper() == "Y"):
                        newPerson = [personName,email, -1]
                        personsDatabase.persons[id] = newPerson
                        general.message(f"\nPerson: '{personName}'. Saved Successfully.")
                        time.sleep(2)
                        input("Please Press Enter To Continue ...")
                    elif (savingConfirmation.upper() == "N"):
                        input("\nPress Enter To Continue And Try Again...")
                        time.sleep(1)
                        general.clear()
                        continue
                    else:
                        general.clear()
                        general.message("\nWrong letter.\nPlease Try Again\n\nCleaning Screen...\n")
                        time.sleep(1)
                        general.clear()
                        continue
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


#Function for display the existing Persons List
    def listPersonbyID(self):
        general.clear()
        personsList = personsDatabase.persons
        for key, value in personsList.items():
            print(f"ID: {key}\nPerson Name: {value[0]}\n")


#Function for modifying an existing Person Information
    def modifyPerson(self):
        general.clear()
        opc =""

        while opc != "0":
            general.clear()
            general.today()
            menu.internalOptionMenu("M O D I F Y  M E N U", "Update Person Info  ")

            opc = input("\nPlease Pick a Number: ")

            if(opc == "1"):
                general.clear()
                Persons().listPersonbyID()
                menu.choosingPerson("Update")

                try:
                    id = int(input("\nPlease type the person ID you would like to update: "))
                except ValueError:
                    id = int(Persons().newID(personsDatabase.persons))
                    
                person = personsDatabase.persons.get(int(id), "Person does not exist!. Please try again.")

                if person == "Person does not exist!. Please try again.":
                    general.clear()
                    print(person)
                    time.sleep(2)
                    general.clear()
                    continue
                else:
                    general.clear()
                    generalNotifications.updatingInstruction()

                    personName = input("Name: .......: ")
                    if not personName:
                        personName = person[0]

                    email = input("Email: .......: ")
                    if not email:
                        email = person[1]

                    print("\n*************************************")
                        
                    savingConfirmation = input("\nAre you sure all data are correct? (Y/N): ")
                    if(savingConfirmation.upper() == "Y"):
                        person = [personName,email]
                        personsDatabase.persons[id] = person
                        general.message(f"\nPerson: {personName}. Updated Successfully.")
                        time.sleep(2)
                        input("Please Press Enter To Continue ...")
                        time.sleep(1)
                        general.clear()
                
                    elif (savingConfirmation.upper() == "N"):
                        input("\nPress Enter To Continue And Try Again...")
                        time.sleep(1)
                        general.clear()
                        continue
                    else:
                        general.clear()
                        general.message("\nWrong letter.\nPlease Try Again\n\nCleaning Screen...\n")
                        time.sleep(1)
                        general.clear()
                        continue
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


#Function for viewing whole details of a specific Person Info
    def viewPerson(self):
       general.clear()
       opc = ""
       
       while opc != "0":
           general.clear()
           
           general.today()
           menu.internalOptionMenu("V I E W  P E R S O N", "Get Person Info     ")

           opc = input("\nPlease Pick a Number: ")
                
           if(opc == "1"):
               Persons().listPersonbyID()
               menu.choosingPerson("Access")

               try:
                   id = int(input("\nPlease type the person ID: "))
               except ValueError:
                    id = int(Persons().newID(personsDatabase.persons))

               person = personsDatabase.persons.get(int(id), "Person does not exist!. Please try again.")
               if person == "Person does not exist!. Please try again.":
                   print(person)
                   time.sleep(2)
                   general.clear()
                   continue 
               else:
                   general.clear()
                   print("*********************************************************")
                   print(f"ID: {id}\nName: {person[0]}\nEmail: {person[1]}\n")
                   print("*********************************************************")
                   input("Press Enter To Continue...")

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


#Function for deleting a person by the ID from the database
    def deletePerson(self):
        general.clear()
        opc =""
        
        while opc != "0":
            general.clear()
            general.today()
            menu.internalOptionMenu("R E M O V E  P E R S O N", "Delete Person Info  ")

            opc = input("\nPlease Pick a Number: ")

            if(opc == "1"):
                general.clear()
                Persons().listPersonbyID()
                menu.choosingPerson("Remove")

                try:
                    id = int(input("\nPlease type the person ID: "))
                except ValueError:
                    id = int(Persons().newID(personsDatabase.persons))

                person = personsDatabase.persons.get(int(id), "Person does not exist!. Please try again.")
                personName = person[0]
        
                if person == "Person does not exist!. Please try again.":
                    general.clear()
                    print(person)
                    time.sleep(2)
                    general.clear()
                    continue
                else:
                    general.clear()
                    print("*********************************************************")
                    print(f"ID: {id}\nName: {person[0]}\nEmail: {person[1]}\n")
                    print("*********************************************************")
            
                    delete = input("Are you sure you want to remove this Person? (Y/N): ")
                    if(delete.upper() == "Y"):
                        del(personsDatabase.persons[id])
                        general.message(f"\nPerson: {personName}. Removed Successfully.")
                        time.sleep(2)
                        general.clear()
                        continue

                    elif (delete.upper() == "N"):
                        input("\nPress Enter To Continue And Try Again...")
                        time.sleep(1)
                        general.clear()
                        continue
                    else:
                        general.clear()
                        general.message("\nWrong letter.\nPlease Try Again\n\nCleaning Screen...\n")
                        time.sleep(1)
                        general.clear()
                        continue
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

#Function for displaying the existing Persons List
    def listPersons(self):
        personsList = personsDatabase.persons
        for key, value in personsList.items():
            print(f"ID: {key}\nName: {value[0]}\nEmail: {value[1]}\n")
        time.sleep(2)
    

 