# books/models.py
from django.db import models
from users.models import User


class Category(models.Model):
    """
    Represents a category or genre of books.

    Attributes:
    -----------
    name : str
        The name of the category.
    description : str
        A brief description of the category.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)



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
    reserved : bool
        Indicates whether the book is reserved. Defaults to False.
    created_at : datetime
        The date and time when the book record was created.
    """

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE, null=True, blank=True)
    reserved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_status(self):
        if self.user:
            return "borrowed"
        elif self.reserved:
            return "reserved"
        return "available"