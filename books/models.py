# books/models.py
from django.db import models
from users.models import User

class Book(models.Model):
    """
    Represents a book in the library system.

    Attributes:
    -----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    published_date : date
        The date when the book was published.
    isbn : str
        The International Standard Book Number (ISBN) of the book.
    user : User
        The user who has currently borrowed the book. This field is optional.
    created_at : datetime
        The date and time when the book record was created.
    """

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the book, which is its title.

        Returns:
        --------
        str
            The title of the book.
        """
        return self.title

