# Student-library-management-system
In this project, we design a student library system comprising two main classes: Library and Student. The objective is to create a system that allows students to interact with a library, borrowing and returning books from a predefined collection.

Library Class:
Attributes:

List of Books: The library class maintains a list of available books, each represented as an object with attributes like book ID, title, and author.
Methods:

Display Available Books: The library provides a method to display the current collection of available books.

Borrow Book: Students can borrow a book by providing the book's name. The system checks if the book is available and, if so, marks it as borrowed.

Return Book: Students can return a borrowed book, making it available for other students to borrow.

Student Class:
Attributes:

Student ID: Each student has a unique identifier.

Name: The name of the student.

Methods:

Request Book: Students can request a book by providing the name of the book they wish to borrow.

Return Book: Students can return a book to the library.

Main Interaction:
The main interaction involves creating instances of the Library and Student classes. The library is initialized with a predefined list of books. Students can then interact with the library by choosing options such as viewing available books, borrowing a book, returning a book, or exiting the system.

The OOP design allows for a modular and organized structure. The Library class encapsulates the book-related functionalities, and the Student class handles student-specific interactions. This separation of concerns enhances the maintainability and readability of the code. Students can easily borrow and return books through a user-friendly interface, making the library system intuitive and accessible.
