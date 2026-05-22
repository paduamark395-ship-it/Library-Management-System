"""
Book model for the Library Management System.
"""


class Book:
    """
    Represents a book in the library.

    Attributes:
        book_id (str): Unique identifier for the book
        title (str): Title of the book
        author (str): Author of the book
        available (bool): Availability status of the book
    """

    def __init__(self, book_id, title, author):
        """
        Initialize a Book object.

        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        """Mark the book as borrowed (unavailable)."""
        self.available = False

    def return_book(self):
        """Mark the book as returned (available)."""
        self.available = True

    def __str__(self):
        """String representation of the book."""
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"

    def __repr__(self):
        """Developer-friendly representation of the book."""
        return f"Book('{self.book_id}', '{self.title}', '{self.author}', available={self.available})"