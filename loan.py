"""
Loan model for the Library Management System.
"""

from datetime import datetime


class Loan:
    """
    Represents a loan record for a book borrowed by a member.

    Attributes:
        loan_id (str): Unique identifier for the loan
        book (Book): The book being borrowed
        member (Member): The member borrowing the book
        loan_date (datetime): Date and time when the book was borrowed
        return_date (datetime): Date and time when the book was returned (if closed)
        is_active (bool): Whether the loan is still active
    """

    def __init__(self, loan_id, book, member):
        """
        Initialize a Loan object.

        Args:
            loan_id (str): Unique identifier for the loan
            book (Book): The book being borrowed
            member (Member): The member borrowing the book
        """
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.loan_date = datetime.now()
        self.return_date = None
        self.is_active = True

    def close_loan(self):
        """Close the loan and record the return date."""
        self.is_active = False
        self.return_date = datetime.now()

    def __str__(self):
        """String representation of the loan."""
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"

    def __repr__(self):
        """Developer-friendly representation of the loan."""
        return f"Loan('{self.loan_id}', book='{self.book.book_id}', member='{self.member.member_id}', active={self.is_active})"