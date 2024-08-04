# users/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import UserRegistrationSerializer,UserSerializer
from django.contrib.auth.models import User
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]



class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user