#! usr/bin/python3 -i   # -i is for 'interactive' mode

"""
File: library.py
A simple program for a library, that models a library as a collection of books and patrons.

"""

class Library(object):
    """Manages Book and Patron objects."""
    
    def __init__(self):
        self.books = list()
        self.patrons = {}

    def borrowBook(self, title, patron):
        """Library method called to borrow a book."""
        
        book = self.books.get(title, None)
        
        if self.getNumberBooks() == 3:                               ######
            return patron, "already has three books out"
        elif book == None: 
            return "There is no book with that title"
        else:
            return self.borrow(patron)                      #######
        

            
        
class Book(Library):
    """Manages the books, allowing borrowing and return."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.books = list()
        self.borrower = None
        self.waitList = list()
        
        super().__init__()
                
    def showStatus(self):
        """Book method called to display the status of books if checked out and
        of the patrons in the waiting list.
        """
        
        fullname = self.title + " (" + self.author + ")"
        print('{0:>50} :'.format(fullname))
        if self.borrower == None:
            print("Book not currently borrowed")
        else:
            print("Book borrowed by", self.borrower)
        if len(self.waitList) == 0:
            print("The waiting list is empty")
        else:
            print("Current waiting list:")
            for p in self.waitList:
                print(p.getName())
            print("")
            
    def getTitle(self):
        """Book method to get the title of the book created with instatialization."""
        return self.title
            
    def borrowBook(self, patron):                           #method overriding
        """Book method called to borrow a book, originally from the Library class."""
        
        book = self.title
        
        if patron.getNumberBooks() == 3:             ######
            return patron, "already has three books out"
        elif book == None: 
            return "There is no book with that title"
        else:
            return self.borrow(patron)               #######
    
    def borrow(self, patron):
        """Book method called to borrow a book."""
        
        if self.borrower == patron.getName():
            return "This patron already has this book"
        elif self.borrower != None:
            self.waitList.append(patron)
            return "This patron has been added to the wait list"
        else:
            self.borrower = patron.getName()
            patron.assignBook(self.title)                             ######
            print("{} has successfully borrowed the book".format(patron.getName()))
        
    def Return(self):
        """Book method called to return a book and assign it to the next person in line."""
        
        print("{} has returned {}".format(self.borrower, self.title) + "\n")
        self.borrower = None
        if len(self.waitList) > 0:
            i = 0
            while self.borrower == None and i < len(self.waitList):
                p = self.waitList[i]
                print(p.getName(), "would be next in line for that book" + "\n")
                print(p.getName(), "has", p.getNumberBooks(), "books borrowed" + "\n")   #######
                if p.getNumberBooks() < 3:                              #######
                    print(p.getName(), "gets the book next")
                    self.borrower = p.getName()
                    self.waitList.pop(i)
                    p.assignBook(self.title)                   #######
                    self.pendingBook = None
                    break
                i = i+1
        if self.borrower == None and len(self.waitList) > 0:
            print("Nobody on the waiting list is allowed to check out {}".format(self.title))
            
       
    
    
    
class Patron(Library):
    """Manages the patrons, allowing book designation and return of a particular book."""
    
    def __init__(self, name):
        self.name = name
        self.books = list()
        self.pendingBook = None
        self.borrower = None
        
        super().__init__()
    
    
    def assignBook(self, title):
        """Patron method called to assign books to a patron."""
        self.books.append(title) 

    def getNumberBooks(self):
        """Patron method called to get the current books count for a patron.""" 
        return len(self.books)
    
    def getName(self):
        """Patron method called to get the name of a patron from instatialization."""
        return self.name
    
    def returnBook(self, book):
        """Patron method called for a patron's return of a particular book."""
        self.book = book
        if self.name != book.borrower:
            print("You did not borrow this book, so you are unable to return it")
        else:
            book.Return()                ######
            self.books.remove(book.getTitle())
            if self.pendingBook != None:
                if self.pendingBook.waitList[0] == self:
                    print("{} is now eligible and next in line for {}".format(self.name, self.pendingBook))
                    self.pendingBook.waitList.pop(0)
                    self.assignBook(self.pendingBook)         ######
                    self.pendingBook.borrower = self
                    self.pendingBook = None
    
    def returnAllBooks(self):
        for book in self.books:
            for bk in library:
                if book == bk.getTitle():
                    bk.Return()
                    break
        del self.books[:]
    
    def showStatusPatron(self):
        print('{0:>40} :'.format("Patron"), self.name)
        if len(self.books) == 0:
            print("No books currently checked out by this patron.")
        else:
            for b in self.books:
                print("[" + b + "]")
            print("")


            

#####################################  TESTING   ####################################################### 

def showLibrary():
    for i, b in enumerate(library):
        b.showStatus()

    print('{0:*<100}'.format(""))

def showPatrons():
    for p in patrons:
        p.showStatusPatron()

    print('{0:*<100}'.format(""))

def testBookLimit():
    print("Test Book Limit:")
    
    showLibrary()
    showPatrons()
    
    b1.borrowBook(jon)
    showLibrary()
    showPatrons()

    b2.borrowBook(jon)
    showLibrary()
    showPatrons()

    b3.borrowBook(jon)
    showLibrary()
    showPatrons()

    b4.borrowBook(jon)
    showLibrary()
    showPatrons()


    jon.returnAllBooks()
    showLibrary()
    showPatrons()

def testWaitList():
    print("Test Wait List:")
    
    b1.borrowBook(don)
    showLibrary()
    showPatrons()

    b1.borrowBook(jon)
    showLibrary()
    showPatrons()

    b1.borrowBook(ted)
    showLibrary()
    showPatrons()

    b2.borrowBook(jon)
    b3.borrowBook(jon)
    b4.borrowBook(jon)
    showLibrary()
    showPatrons()

    don.returnBook(b1)
    showLibrary()
    showPatrons()

    jon.returnBook(b1)
    showLibrary()
    showPatrons()

    ted.returnBook(b1)
    showLibrary()
    showPatrons()

    jon.returnBook(b3)
    showLibrary()
    showPatrons()

    jon.returnBook(b2)
    showLibrary()
    showPatrons()

    jon.returnBook(b4)
    showLibrary()
    showPatrons()

    jon.returnBook(b1)
    showLibrary()
    showPatrons()
    
def main():
    testBookLimit()
    testWaitList()
    
b1 = Book("Kidagaa kimemwozea","Walibora, Ken")
b2 = Book("The River and Between","Ngugi, Wa Kiong'o")
b3 = Book("Betrayal In The City","Zebu, Maynyard")
b4 = Book("The 100","Gate, Winnie")
library = b1, b2, b3, b4

jon = Patron("Jon")
ted = Patron("Ted")
don = Patron("Don")

patrons = jon, ted, don

main()
