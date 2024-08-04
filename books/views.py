# books/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Book,Category
from .serializers import BookSerializer,CategorySerializer

# class BookViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     A viewset for viewing a list of books.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]