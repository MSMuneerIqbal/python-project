import streamlit as st
import json
import os
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.due_date = None

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []
        self.data_file = "library_data.json"
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()
        return f"Added: {book}"

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_data()
                return f"Removed: {book}"
        return "Book not found."

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.due_date = datetime.now() + timedelta(days=14)
                    self.save_data()
                    return f"Borrowed: {book}\nDue date: {book.due_date.strftime('%Y-%m-%d')}"
                else:
                    return "Book is already borrowed."
        return "Book not found."

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    book.due_date = None
                    self.save_data()
                    return f"Returned: {book}"
                else:
                    return "Book is not borrowed."
        return "Book not found."

    def list_books(self):
        if not self.books:
            return "No books in the library."
        else:
            return "\n".join([f"{book} - {'Available' if not book.is_borrowed else f'Borrowed (Due: {book.due_date.strftime('%Y-%m-%d')})'}" for book in self.books])

    def save_data(self):
        data = []
        for book in self.books:
            book_data = {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "is_borrowed": book.is_borrowed,
                "due_date": book.due_date.isoformat() if book.due_date else None
            }
            data.append(book_data)
        
        with open(self.data_file, "w") as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
            
            for book_data in data:
                book = Book(book_data["title"], book_data["author"], book_data["isbn"])
                book.is_borrowed = book_data["is_borrowed"]
                book.due_date = datetime.fromisoformat(book_data["due_date"]) if book_data["due_date"] else None
                self.books.append(book)

def main():
    st.title("Library Management System")

    library = Library()

    menu = ["Add Book", "Remove Book", "Borrow Book", "Return Book", "List Books"]
    choice = st.sidebar.selectbox("Select an action", menu)

    if choice == "Add Book":
        st.subheader("Add a New Book")
        title = st.text_input("Enter book title")
        author = st.text_input("Enter book author")
        isbn = st.text_input("Enter book ISBN")
        if st.button("Add Book"):
            result = library.add_book(Book(title, author, isbn))
            st.success(result)

    elif choice == "Remove Book":
        st.subheader("Remove a Book")
        isbn = st.text_input("Enter book ISBN to remove")
        if st.button("Remove Book"):
            result = library.remove_book(isbn)
            st.success(result)

    elif choice == "Borrow Book":
        st.subheader("Borrow a Book")
        isbn = st.text_input("Enter book ISBN to borrow")
        if st.button("Borrow Book"):
            result = library.borrow_book(isbn)
            st.success(result)

    elif choice == "Return Book":
        st.subheader("Return a Book")
        isbn = st.text_input("Enter book ISBN to return")
        if st.button("Return Book"):
            result = library.return_book(isbn)
            st.success(result)

    elif choice == "List Books":
        st.subheader("List of Books")
        books = library.list_books()
        st.text(books)

if __name__ == "__main__":
    main()