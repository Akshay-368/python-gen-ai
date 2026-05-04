# problem 8 
# library management system 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if ( self.available ) :
            self.available = False
            print("Book borrowed successfully.")
        else:
            print("Book not available")
    
    def return_book(self):
        self.available = True
        print("Book returned successfully.")

book = Book("Python Essentials", "Mark")
book.borrow()
book.return_book()