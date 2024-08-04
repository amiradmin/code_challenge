# books/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Book
from .serializers import BookSerializer

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

    # def get_permissions(self):
    #     if self.action in ['update', 'partial_update']:
    #         self.permission_classes = [IsAdminUser]
    #     return super().get_permissions()

