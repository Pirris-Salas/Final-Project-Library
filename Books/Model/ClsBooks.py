#ClsBooks is used for modeling all input data from the user
#Also all CRUD functions are stated here

import time
import Books.Repository.BooksRepository as booksDatabase
import GeneralMethods as general
import Books.Ui.BooksMenu as menu
import Ui.MainMenu as generalNotifications

class Books:
    
    def _init_(self):
        pass
    
#This function is for adding an autoincremental ID for the Books Database
    def newID(self, books):
        id = 0
        for x in books:
            if(x > id):
                id = x
        return id+1


#Funtion for validating blank fields
    def validationFields(name, genre, author):
        msg =""

        if(name == "" or name == " "):
           msg= "\nBook title is missing!. Please try again, new book not saved"
        if(genre == "" or genre == " "):
            msg= f"{msg}\nBook genre is missing!. Please try again, new book not saved"
        if(author == "" or author == " "):
            msg= f"{msg}\nBook author is missing!. Please try again, new book not saved"
        
        return msg

        



#Function for adding a new book to the database
    def addBook(self):
        general.clear()
        opc = ""
        msg = ""
        while opc != "0":
            general.clear()
            if(msg != ""):
                general.clear()
                general.message(msg)
                time.sleep(2)
                general.clear()
                continue
            else:
                general.clear()
                general.today()
                menu.internalOptionMenu("A D D  NEW   B O O K", "Add a New Book      ")

                opc = input("\nPlease Pick a Number: ")

                if(opc == "1"):
                    general.clear()
                    id = int(Books().newID(booksDatabase.books))
                    menu.newBook()
                    bookName = input("Book Title: .......: ")
                    bookGenre = input("Genre: .......: ")
                    bookAuthor = input("Author: .......: ")
        
                    validationMsg = Books.validationFields(bookName, bookGenre, bookAuthor)

                    if(validationMsg != ""):
                       print(validationMsg)
                       time.sleep(1)
                       input("\nPlease Press Enter To Continue ...")
                       general.clear()
                       continue
            
                    else:
                       savingConfirmation = input("Are you sure all data are correct? (Y/N): ")
                       
                       if(savingConfirmation.upper() == "Y"):
                           newBook = [bookName,bookGenre,bookAuthor, -1]
                           booksDatabase.books[id] = newBook
                           general.message(f"\nNew Book: '{bookName}'. Saved Successfully.")
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


        

#Function for display the existing Books List
    def listBookbyID(self):
        general.clear()
        booksList = booksDatabase.books
        for key, value in booksList.items():
            print(f"ID: {key}\nBook Title: {value[0]}\n")
       


#Function for modifying an existing boook
    def modifyBook(self):
        general.clear()
        opc =""
        msg = ""
        while opc != "0":
            if(msg != ""):
                general.clear()
                general.message(msg)
                time.sleep(2)
                general.clear()
                continue
            else:
                general.clear()
                general.today()
                menu.internalOptionMenu("M O D I F Y  B O O K", "Update Book Info    ")

                opc = input("\nPlease Pick a Number: ")

                if(opc == "1"):
                    general.clear()
                    Books().listBookbyID()
                    menu.choosingBook("Modify")

                    try:
                        id = int(input("\nPlease type the book ID you would like to update: "))
                    except ValueError:
                        id = int(Books().newID(booksDatabase.books))
                    
                    book = booksDatabase.books.get(int(id), "Book does not exist!. Please try again.")

                    if book == "Book does not exist!. Please try again.":
                        general.clear()
                        print(book)
                        time.sleep(2)
                        general.clear()
                        continue
                    else:
                        general.clear()
                        generalNotifications.updatingInstruction()

                        bookName = input("Book Title: .......: ")
                        if not bookName:
                            bookName = book[0]

                        bookGenre = input("Genre: .......: ")
                        if not bookGenre:
                            bookGenre = book[1]

                        bookAuthor = input("Author: .......: ")
                        if not bookAuthor:
                            bookAuthor = book[2]

                        print("\n*************************************")
                        
                        savingConfirmation = input("\nAre you sure all data are correct? (Y/N): ")
                        if(savingConfirmation.upper() == "Y"):
                            book = [bookName,bookGenre,bookAuthor]
                            booksDatabase.books[id] = book
                            general.message(f"\nBook: {bookName}. Updated Successfully.")
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
        


#Function for viewing whole details of a specific book
    def viewBook(self):
       general.clear()
       opc = ""
       msg=""
       while opc != "0":
           general.clear()
           if(msg != ""):
               general.clear()
               general.message(msg)
               time.sleep(2)
               general.clear()
               Books().viewBook()
           else:
                general.clear()
                general.today()
                menu.internalOptionMenu("V I E W      B O O K", "Get Book Information")

           opc = input("\nPlease Pick a Number: ")
                
           if(opc == "1"):
               Books().listBookbyID()
               menu.choosingBook("Access")

               try:
                   id = int(input("\nPlease type the book ID: "))
               except ValueError:
                    id = int(Books().newID(booksDatabase.books))

               book = booksDatabase.books.get(int(id), "Book does not exist!. Please try again.")
               if book == "Book does not exist!. Please try again.":
                    print(book)
                    time.sleep(2)
                    general.clear()
                    continue 
               else:
                    general.clear()
                    print("*********************************************************")
                    print(f"ID: {id}\nBook Title: {book[0]}\nBook Genre: {book[1]}\nBook Author: {book[2]}\n")
                    print("*********************************************************")
                    msg = ""
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
                
                    



#Function for deleting a book by the ID
    def deleteBook(self):
        general.clear()
        opc =""
        
        while opc != "0":
            general.clear()
            general.today()
            menu.internalOptionMenu("R E M O V E  B O O K", "Delete Book Info    ")

            opc = input("\nPlease Pick a Number: ")

            if(opc == "1"):
                general.clear()
                Books().listBookbyID()
                menu.choosingBook("Remove")

                try:
                    id = int(input("\nPlease type the book ID: "))
                except ValueError:
                    id = int(Books().newID(booksDatabase.books))

                book = booksDatabase.books.get(int(id), "Book does not exist!. Please try again.")
                bookName = book[0]
        
                if book == "Book does not exist!. Please try again.":
                    general.clear()
                    print(book)
                    time.sleep(2)
                    general.clear()
                    continue
                else:
                    general.clear()
                    print("*********************************************************")
                    print(f"ID: {id}\nBook Title: {book[0]}\nBook Genre: {book[1]}\nBook Author: {book[2]}\n")
                    print("*********************************************************")
            
                    delete = input("Are you sure you want to remove this Book? (Y/N): ")
                    if(delete.upper() == "Y"):
                        del(booksDatabase.books[id])
                        general.message(f"\nBook: {bookName}. Removed Successfully.")
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
                
            
        




#Function for display the existing Books List
    def listBook(self):
        booksList = booksDatabase.books
        for key, value in booksList.items():
            print(f"ID: {key}\nBook Title: {value[0]}\nBook Genre: {value[1]}\nBook Author: {value[2]}\n")




