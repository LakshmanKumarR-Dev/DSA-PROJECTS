import tkinter as tk
from tkinter import messagebox, simpledialog

class Book:
    def __init__ (self, ID, Name, Author):
        self.id = ID
        self.name = Name
        self.author = Author
        self.available = True
        self.next = None

class Library:
    def __init__ (self):
        self.head = None

    def add(self, id, name, author):
        new_book = Book(id, name, author)
        new_book.next = self.head
        self.head = new_book
        messagebox.showinfo("Succes", f"Book {name} by author {author} is added")

    def display(self):
        book = []
        temp = self.head
        while temp:
            x = "Available" if temp.available else "Issued"
            book.append(f"ID: {temp.id} , Name : {temp.name}, Author : {temp.author}, Status : {x}")
            temp = temp.next
        return "\n".join(book) if book else "No books in Library"
    
    def borrow(self, id):
        temp = self.head
        while temp:
            if temp.id == id:
                if temp.available:
                    temp.available = False
                    return f"Book {temp.name} is Borrowed succesfully"
                else:
                    return "Book is already Borrowed"
            temp = temp.next
        return "Book is not found"
    
    def return_book(self, id):
        temp = self.head
        while temp:
            if temp.id == id:
                if temp.available:
                    temp.available = True
                    return f"Book {temp.name} is Returned succesfully"
                else:
                    return "Book is already available"
            temp = temp.next
        return "Book is not found"
    
    def search(self, id):
        temp = self.head
        while temp:
            if temp.id == id:
                return f"{temp.name} by {temp.author} is - {"available" if temp.available else "issued"}"
            temp = temp.next
        return "Book is not found"
    
lib = Library()
root = tk.Tk()
root.title("Library Management")

def add_mess():
    id = simpledialog.askstring("Input", "Enter Book ID no: ")
    name = simpledialog.askstring("Input", "Enter Book Name: ")
    author = simpledialog.askstring("Input", "Enter Book Author: ")
    if id and name and author:
        lib.add(id, name, author)
    
def display_mess():
    books = lib.display()
    messagebox.showinfo("Books in the Library", books)

def borrow_mess():
    id = simpledialog.askstring("Input", "Enter the Book ID to Borrow: ")
    if id:
        res = lib.borrow(id)
        messagebox.showinfo("Borrow Book", res)

def return_mess():
    id = simpledialog.askstring("Input", "Enter the Book ID to Return: ")
    if id:
        res = lib.return_book(id)
        messagebox.showinfo("Return Book", res)

def search_mess():
    id = simpledialog.askstring("Input", "Enter the Book ID to Search: ")
    if id:
        res = lib.search(id)
        messagebox.showinfo("Search Book", res)

tk.Button(root, text = "ADD BOOK", width = 20, command = add_mess).pack(pady = 10)
tk.Button(root, text = "SEARCH BOOK", width = 20, command = search_mess).pack(pady = 10)
tk.Button(root, text = "RETURN BOOK", width = 20, command = return_mess).pack(pady = 10)
tk.Button(root, text = "BORROW BOOK", width = 20, command = borrow_mess).pack(pady = 10)
tk.Button(root, text = "DISPLAY BOOK", width = 20, command = display_mess).pack(pady = 10)

root.mainloop()