#At this file we are declaring all the menus related 
# to the Persons
# Clean Arquitecture Principles

def personsMenu():
    print("****************************************") 
    print("* P E R S O N S    M E N U             *")
    print("* a. Add New Person                    *")
    print("* b. Modify Existing Person            *")
    print("* c. View Person Information           *")
    print("* d. Delete Person                     *")
    print("* e. List Persons                      *")
    print("* f. Find a Person                     *")
    print("* 0. Back To The Main Menu             *")
    print("*                                      *")
    print("**************************************\n") 



def newPerson():
    print("****************************************")
    print("*        N E W   P E R S O N           *")
    print("**************************************\n")



def choosingPerson(msg):
    print("****************************************")
    print("*        Choose The Person ID          *")
    print(f"*      You Would Like to {msg}        *")
    print("**************************************\n")


def internalOptionMenu(banner, option):
    print("****************************************") 
    print(f"*       {banner}           *")
    print("****************************************") 
    print(f"* 1. {option}              *")
    print("* 0. Back To The Previous Menu         *")
    print("*                                      *")
    print("**************************************\n") 

def findPersonMenu():
    print("****************************************") 
    print("* L O O K I N G   FOR   S O M E O N E ?*")
    print("****************************************") 
    print("* 1. Find a person by the name.        *")
    print("* 2. Find a person by the ID number.   *")
    print("* 0. Back To The Previous Menu         *")
    print("*                                      *")
    print("**************************************\n") 

def writingNameMenu():
    print("****************************************")
    print("*     Please Type The Person Name      *")
    print(f"*    All Matches Would Be Listed       *")
    print("**************************************\n")

def resultsFound():
    print("********************************************")
    print("* W E  F O U N D  T H E S E   R E S U L T S*")
    print("******************************************\n")