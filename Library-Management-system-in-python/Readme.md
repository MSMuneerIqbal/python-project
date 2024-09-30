# Library Management System

## Overview

This Library Management System is a simple Python application with a Streamlit front-end. It allows users to manage a library's book inventory, including adding books, removing books, borrowing books, returning books, and listing all books in the library.

## Features

- Add new books to the library
- Remove books from the library
- Borrow books with automatic due date calculation
- Return borrowed books
- List all books in the library with their status (available or borrowed)
- Persistent data storage using JSON

## Requirements

- Python 3.7+
- Streamlit

## Installation

1. Clone this repository:
2. Install the required packages:
## Usage

To run the application, use the following command in your terminal:

This will start the Streamlit server and open the application in your default web browser.

## How to Use

1. **Add a Book**: Enter the book's title, author, and ISBN, then click "Add Book".
2. **Remove a Book**: Enter the ISBN of the book you want to remove, then click "Remove Book".
3. **Borrow a Book**: Enter the ISBN of the book you want to borrow, then click "Borrow Book".
4. **Return a Book**: Enter the ISBN of the book you want to return, then click "Return Book".
5. **List Books**: Click on "List Books" in the sidebar to see all books in the library.

## Data Persistence

The application uses a JSON file (`library_data.json`) to store the library data. This ensures that your library inventory persists between application restarts.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.