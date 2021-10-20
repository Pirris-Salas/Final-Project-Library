#At this file we are declaring all the menus related 
# to the Books
# Clean Arquitecture Principles

def booksMenu():
    print("****************************************") 
    print("*       B O O K S    M E N U           *")
    print("****************************************") 
    print("* a. Add New Book                      *")
    print("* b. Modify Existing Book              *")
    print("* c. View Book                         *")
    print("* d. Delete Book                       *")
    print("* e. List Books                        *")
    print("* f. Find a Book                       *")
    print("* 0. Back To The Main Menu             *")
    print("*                                      *")
    print("****************************************\n") 


def newBook():
    print("****************************************")
    print("*        N E W   B O O K               *")
    print("****************************************\n")


def choosingBook(msg):
    print("****************************************")
    print("*        Choose The Book ID            *")
    print(f"*      You Would Like to {msg}        *")
    print("****************************************\n")

def internalOptionMenu(banner, option):
    print("****************************************") 
    print(f"*       {banner}           *")
    print("****************************************") 
    print(f"* 1. {option}              *")
    print("* 0. Back To The Previous Menu         *")
    print("*                                      *")
    print("****************************************\n") 