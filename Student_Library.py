'''Implement a student libreary system using oops
where students can borrow a book from the list of books.
create a seprate Library and Student class.

'''
class Library:
    def __init__(self,listofBook):
        self.Book=listofBook
    def displayAvailableBook(self):
        print("Books present in this library are: ")
        for Book in self.Book:
            print("*" + Book)

    def borrowBook(self,Bookname):
        if Bookname in self.Book:
            print(f"You have been issued {Bookname}. Plese keep it safe and return it within 30  days")    
            self.Book.remove(Bookname)  
            return True  
        else:
            print("Sorry,This book has already has been issued to someone else.Plese wait until the book is returned") 
            return False
           
    def returnBook(self,Bookname):
        self.Book.append(Bookname)
        print("Thanks for returning book")


class student:
    def requestBook(self):
        self.Book=input("Enter the name of the book you want to issued: ")
        return self.Book
    
    def returnBook(self):
        self.Book=input("Enter the book you want to return: ")
        return self.Book

if __name__=="__main__":
    centraLibrary=Library(["Algorithem","Django","Clrs","Python notes"])
    student =student()
    centraLibrary.displayAvailableBook()
    while(True):
        WelcomeMsg='''
        ===Welcome to central library===
        plese choose an option:
        1. Listing all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        '''
        print(WelcomeMsg)
        a=int(input("Enter a choice:"))
        if a==1:
            centraLibrary.displayAvailableBook()
        elif a==2:
            centraLibrary.borrowBook(student.requestBook())
        elif a==3:
            centraLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing central Library! Have a great day ahead")
            exit()
        else:
            print("invalid Choice")




