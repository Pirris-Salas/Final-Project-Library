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
        msg = ""
        if(name == ""):
            msg= "Book title is missing!. Please enter it"
        elif(genre == ""):
            msg= "Book genre is missing!. Please enter it"
        elif(author == ""):
            msg = "Book author is missing!. Please enter it"
        else:
            msg = ""

        return msg



#Function for adding a new book to the database
    def addBook(self):
        general.clear()
        id = int(Books().newID(booksDatabase.books))
        menu.newBook()
        bookName = input("Book Title: .......: ")
        bookGenre = input("Genre: .......: ")
        bookAuthor = input("Author: .......: ")
        
        validationMsg = Books.validationFields(bookName, bookGenre, bookAuthor)

        if(validationMsg == ""):
            savingConfirmation = input("Are you sure all data are correct? (Y/N)")
            if(savingConfirmation.upper() == "Y"):
                newBook = [bookName,bookGenre,bookAuthor, -1]
                booksDatabase.books[id] = newBook
                general.message("New Book: {bookName}. Saved Successfully.")
        else:
            print(validationMsg)

#Function for display the existing Books List
    def listBookbyID(self):
        booksList = booksDatabase.books
        for key, value in booksList.items():
            print(f"ID: {key}\nBook Title: {value[0]}\n")



#Function for modifying an existing boook
    def modifyBook(self):
        general.clear()
        Books.listBookbyID()
        menu.choosingBook("Modify")
        id = int(input("\nPlease type the book ID"))
        book = booksDatabase.books.get(int(id), "Book does not exist!. Please try again.")
        
        if book == "Book does not exist!. Please try again.":
            print(book)
            time.sleep(2)
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

            print("*************************************")
            msg = ""
            savingConfirmation = input("Are you sure all data are correct? (Y/N)")
            if(savingConfirmation.upper() == "Y"):
                book = [bookName,bookGenre,bookAuthor]
                booksDatabase.books[id] = book
                general.message("Book: {bookName}. Updated Successfully.")
            else:
                msg = ""
            input("Press Enter To Continue And Try Again...")


#Function for viewing whole details of a specific book
    def viewBook(self):
        general.clear()
        Books.listBookbyID()
        menu.choosingBook("Access")

        id = int(input("\nPlease type the book ID"))
        book = booksDatabase.books.get(int(id), "Book does not exist!. Please try again.")
        
        if book == "Book does not exist!. Please try again.":
            print(book)
            time.sleep(2)
        else:
            print("*********************************************************")
            print(f"ID: {id}\nBook Title: {book[0]}\nBook Genre: {book[1]}\nBook Author: {book[2]}\n")
            print("*********************************************************")
            msg = ""
            input("Press Enter To Continue...")


#Function for deleting a book by the ID
    def deleteBook(self):
        general.clear()
        Books.listBookbyID()
        menu.choosingBook("Remove")

        id = int(input("\nPlease type the book ID"))
        book = booksDatabase.books.get(int(id), "Book does not exist!. Please try again.")
        bookName = book[0]
        
        if book == "Book does not exist!. Please try again.":
            print(book)
            time.sleep(2)
        else:
            general.clear()
            print("*********************************************************")
            print(f"ID: {id}\nBook Title: {book[0]}\nBook Genre: {book[1]}\nBook Author: {book[2]}\n")
            print("*********************************************************")
            msg = ""
            delete = input("Are you sure you want to remove this Book? (Y/N)")
            if(delete.upper() == "Y"):
                del(booksDatabase.books[id])
                general.message("Book: {bookName}. Removed Successfully.")
            else:
                msg = ""
            input("Press Enter To Continue And Try Again...")

#Function for display the existing Books List
    def listBook(self):
        booksList = booksDatabase.books
        for key, value in booksList.items():
            print(f"ID: {key}\nBook Title: {value[0]}\nBook Genre: {value[1]}\nBook Author: {value[2]}\n")




