"""
Custom exceptions for the Library Management System.
"""


class BookNotFoundError(Exception):
    """Raised when a book with the specified ID is not found."""
    pass


class MemberNotFoundError(Exception):
    """Raised when a member with the specified ID is not found."""
    pass


class BookUnavailableError(Exception):
    """Raised when attempting to borrow a book that is already borrowed."""
    pass


class LoanNotFoundError(Exception):
    """Raised when a loan with the specified ID is not found."""
    pass