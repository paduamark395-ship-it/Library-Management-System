"""
LibraryService class for managing books, members, and loans.
"""

from models import Book, Member, Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


class LibraryService:
    """
    Service class for managing library operations.
    Handles books, members, and loans.
    """

    def __init__(self):
        """Initialize the LibraryService with empty storage."""
        self._books = {}  # Dictionary: book_id -> Book
        self._members = {}  # Dictionary: member_id -> Member
        self._loans = []  # List of Loan objects
        self._loan_counter = 0  # Counter for generating loan IDs

    # ==================== BOOK OPERATIONS ====================

    def add_book(self, book_id, title, author):
        """
        Add a new book to the library.

        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book

        Returns:
            Book: The newly created book object
        """
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return book

    def get_book(self, book_id):
        """
        Retrieve a book by its ID.

        Args:
            book_id (str): The book's unique identifier

        Returns:
            Book: The book object

        Raises:
            BookNotFoundError: If the book is not found
        """
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        return book

    def view_books(self):
        """
        Get a list of all books in the library.

        Returns:
            list: List of all Book objects
        """
        return list(self._books.values())

    # ==================== MEMBER OPERATIONS ====================

    def register_member(self, member_id, name, email):
        """
        Register a new member to the library.

        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member

        Returns:
            Member: The newly created member object
        """
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return member

    def get_member(self, member_id):
        """
        Retrieve a member by their ID.

        Args:
            member_id (str): The member's unique identifier

        Returns:
            Member: The member object

        Raises:
            MemberNotFoundError: If the member is not found
        """
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        return member

    def view_members(self):
        """
        Get a list of all members in the library.

        Returns:
            list: List of all Member objects
        """
        return list(self._members.values())

    # ==================== LOAN OPERATIONS ====================

    def borrow_book(self, book_id, member_id):
        """
        Create a loan record when a member borrows a book.

        Args:
            book_id (str): The book's unique identifier
            member_id (str): The member's unique identifier

        Returns:
            Loan: The newly created loan object

        Raises:
            BookNotFoundError: If the book is not found
            MemberNotFoundError: If the member is not found
            BookUnavailableError: If the book is already borrowed
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")

        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")

        # Check availability
        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")

        # Mark book as borrowed
        book.borrow()

        # Generate loan ID
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"

        # Create and store loan
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)

        return loan

    def return_book(self, loan_id):
        """
        Process the return of a borrowed book.

        Args:
            loan_id (str): The loan's unique identifier

        Returns:
            Loan: The closed loan object

        Raises:
            LoanNotFoundError: If the loan is not found
        """
        loan = self.get_loan(loan_id)

        if not loan.is_active:
            raise LoanNotFoundError(f"Loan {loan_id} is already closed.")

        # Mark book as returned
        loan.book.return_book()

        # Close the loan
        loan.close_loan()

        return loan

    def get_loan(self, loan_id):
        """
        Retrieve a loan by its ID.

        Args:
            loan_id (str): The loan's unique identifier

        Returns:
            Loan: The loan object

        Raises:
            LoanNotFoundError: If the loan is not found
        """
        for loan in self._loans:
            if loan.loan_id == loan_id:
                return loan
        raise LoanNotFoundError("Loan not found.")

    def view_loans(self):
        """
        Get a list of all loans in the library.

        Returns:
            list: List of all Loan objects
        """
        return list(self._loans)