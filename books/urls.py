# books/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,CategoryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'categories', CategoryViewSet, basename='category')
urlpatterns = [
    path('', include(router.urls)),
]